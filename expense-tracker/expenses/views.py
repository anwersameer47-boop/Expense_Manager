"""
Views for the Expenses App.

Views handle the logic for each page:
  - What data to fetch from the database
  - What template to render
  - How to process form submissions
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from django.utils import timezone
from datetime import date

from .models import Expense
from .forms import UserRegistrationForm, ExpenseForm


# -------------------------------------------------------------------
# Home Page
# -------------------------------------------------------------------
def home(request):
    """
    Public home/landing page.
    If user is already logged in, redirect to dashboard.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'home.html')


# -------------------------------------------------------------------
# User Authentication Views
# -------------------------------------------------------------------

def register_view(request):
    """
    Registration page — lets new users create an account.

    GET:  Show the registration form.
    POST: Validate and create the new user account.
    """
    # Already logged in? Go to dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Save the user to the database
            user = form.save()
            # Automatically log in the new user
            login(request, user)
            messages.success(request, f"Welcome, {user.username}! Your account has been created.")
            return redirect('dashboard')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        # GET request — show empty form
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    """
    Login page — authenticates existing users.

    GET:  Show the login form.
    POST: Check credentials and log the user in.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's authenticate() checks username/password against the database
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            # If user was trying to visit a page before login, go there
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, 'registration/login.html')


def logout_view(request):
    """
    Log the user out and redirect to home page.
    Works with both GET and POST requests.
    """
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('home')


# -------------------------------------------------------------------
# Dashboard View
# -------------------------------------------------------------------

@login_required  # User must be logged in to access this page
def dashboard(request):
    """
    Dashboard page — shows expense summary statistics.

    Displays:
      - Total expenses (all time)
      - Monthly expenses (current month)
      - Expenses by category
      - Recent 5 expenses
    """
    # Get only the current user's expenses
    user_expenses = Expense.objects.filter(user=request.user)

    # --- Total all-time expenses ---
    total_expenses = user_expenses.aggregate(total=Sum('amount'))['total'] or 0

    # --- Monthly expenses (current month) ---
    today = date.today()
    monthly_expenses = user_expenses.filter(
        date__year=today.year,
        date__month=today.month
    ).aggregate(total=Sum('amount'))['total'] or 0

    # --- Expenses by category (for summary) ---
    category_totals = {}
    for category, _ in Expense.CATEGORY_CHOICES:
        cat_total = user_expenses.filter(category=category).aggregate(
            total=Sum('amount')
        )['total'] or 0
        if cat_total > 0:
            category_totals[category] = cat_total

    # --- Recent 5 expenses ---
    recent_expenses = user_expenses[:5]

    # --- Total count ---
    total_count = user_expenses.count()

    context = {
        'total_expenses': total_expenses,
        'monthly_expenses': monthly_expenses,
        'recent_expenses': recent_expenses,
        'category_totals': category_totals,
        'total_count': total_count,
        'current_month': today.strftime('%B %Y'),  # e.g. "May 2025"
    }
    return render(request, 'expenses/dashboard.html', context)


# -------------------------------------------------------------------
# Expense List View
# -------------------------------------------------------------------

@login_required
def expense_list(request):
    """
    Expense list page — shows all expenses in a table.
    Supports filtering by category.
    """
    # Start with all expenses for this user
    expenses = Expense.objects.filter(user=request.user)

    # Filter by category if provided in URL query string (?category=Food)
    selected_category = request.GET.get('category', '')
    if selected_category:
        expenses = expenses.filter(category=selected_category)

    # Total for the filtered results
    total = expenses.aggregate(total=Sum('amount'))['total'] or 0

    context = {
        'expenses': expenses,
        'categories': Expense.CATEGORY_CHOICES,
        'selected_category': selected_category,
        'total': total,
    }
    return render(request, 'expenses/expense_list.html', context)


# -------------------------------------------------------------------
# Add Expense View
# -------------------------------------------------------------------

@login_required
def add_expense(request):
    """
    Add expense page — lets users create a new expense.

    GET:  Show empty form with today's date pre-filled.
    POST: Validate and save the new expense.
    """
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            # Don't save to DB yet — we need to add the user first
            expense = form.save(commit=False)
            expense.user = request.user  # Assign to logged-in user
            expense.save()
            messages.success(request, f"Expense '{expense.title}' added successfully!")
            return redirect('expense_list')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        # Pre-fill today's date for convenience
        form = ExpenseForm(initial={'date': date.today()})

    return render(request, 'expenses/expense_form.html', {
        'form': form,
        'form_title': 'Add New Expense',
        'btn_label': 'Add Expense',
    })


# -------------------------------------------------------------------
# Edit Expense View
# -------------------------------------------------------------------

@login_required
def edit_expense(request, pk):
    """
    Edit expense page — lets users update an existing expense.

    pk: The primary key (ID) of the expense to edit.

    get_object_or_404 — returns the expense if found, or a 404 error
    if the expense doesn't exist OR belongs to another user (security!).
    """
    expense = get_object_or_404(Expense, pk=pk, user=request.user)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, f"Expense '{expense.title}' updated successfully!")
            return redirect('expense_list')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        # Pre-fill the form with existing expense data
        form = ExpenseForm(instance=expense)

    return render(request, 'expenses/expense_form.html', {
        'form': form,
        'form_title': f'Edit Expense: {expense.title}',
        'btn_label': 'Update Expense',
        'expense': expense,
    })


# -------------------------------------------------------------------
# Delete Expense View
# -------------------------------------------------------------------

@login_required
def delete_expense(request, pk):
    """
    Delete expense page — asks for confirmation before deleting.

    GET:  Show confirmation page.
    POST: Delete the expense and redirect to list.
    """
    expense = get_object_or_404(Expense, pk=pk, user=request.user)

    if request.method == 'POST':
        title = expense.title
        expense.delete()
        messages.success(request, f"Expense '{title}' deleted successfully!")
        return redirect('expense_list')

    return render(request, 'expenses/expense_confirm_delete.html', {'expense': expense})
