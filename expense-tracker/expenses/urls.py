"""
URL patterns for the Expenses App.

This maps URL paths to the corresponding view functions.
"""

from django.urls import path
from . import views

urlpatterns = [
    # --- Public Pages ---
    path('', views.home, name='home'),                           # Home / Landing page

    # --- Authentication ---
    path('register/', views.register_view, name='register'),     # Registration page
    path('login/', views.login_view, name='login'),              # Login page
    path('logout/', views.logout_view, name='logout'),           # Logout

    # --- Dashboard ---
    path('dashboard/', views.dashboard, name='dashboard'),       # Main dashboard

    # --- Expense Management (CRUD) ---
    path('expenses/', views.expense_list, name='expense_list'),       # View all expenses
    path('expenses/add/', views.add_expense, name='add_expense'),     # Add new expense
    path('expenses/<int:pk>/edit/', views.edit_expense, name='edit_expense'),      # Edit expense
    path('expenses/<int:pk>/delete/', views.delete_expense, name='delete_expense'),# Delete expense
]
