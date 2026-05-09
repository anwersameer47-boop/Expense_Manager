"""
Forms for the Expenses App.

Django forms handle user input, validation, and rendering.
We define two forms:
  1. UserRegistrationForm — for creating a new account
  2. ExpenseForm          — for adding/editing expenses
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Expense


class UserRegistrationForm(UserCreationForm):
    """
    Extended registration form that includes an email field.
    Inherits from Django's built-in UserCreationForm which handles
    password hashing and validation automatically.
    """
    # Add email field (optional but good practice)
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email (optional)'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add Bootstrap CSS classes and placeholders to all fields
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Choose a username'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Create a password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        })


class ExpenseForm(forms.ModelForm):
    """
    Form for creating and editing expenses.
    ModelForm automatically generates fields from the Expense model.
    """

    class Meta:
        model = Expense
        # Fields to show in the form (exclude 'user' — it's set automatically)
        fields = ['title', 'amount', 'category', 'date', 'description']

        # Custom widgets add Bootstrap classes and HTML attributes
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Lunch at restaurant'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'  # HTML5 date picker
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Optional notes about this expense...',
                'rows': 3
            }),
        }
