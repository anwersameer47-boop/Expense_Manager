"""
Models for the Expenses App.

This file defines the database structure for our expense records.
Each Expense is linked to a specific user so users only see their own data.
"""

from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    """
    Expense model — represents a single expense record.

    Fields:
        user        — The user who owns this expense (ForeignKey to User)
        title       — Short description / name of the expense
        amount      — How much was spent (decimal number)
        category    — Type of expense (Food, Travel, etc.)
        date        — When the expense occurred
        description — Optional detailed notes about the expense
        created_at  — Automatically set when the record is created
    """

    # Category choices — predefined list shown in the dropdown
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Shopping', 'Shopping'),
        ('Bills', 'Bills'),
        ('Education', 'Education'),
        ('Entertainment', 'Entertainment'),
        ('Other', 'Other'),
    ]

    # Link each expense to a user; deleting the user removes their expenses
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')

    # Expense details
    title = models.CharField(max_length=200, help_text="Name or title of the expense")
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Amount in your currency")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    date = models.DateField(help_text="Date when the expense occurred")
    description = models.TextField(blank=True, null=True, help_text="Optional notes about the expense")

    # Auto-set timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Show most recent expenses first
        ordering = ['-date', '-created_at']
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'

    def __str__(self):
        return f"{self.title} — ₹{self.amount} ({self.category})"
