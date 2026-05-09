"""
Admin configuration for the Expenses App.

Registering models here makes them accessible via Django's built-in
admin panel at /admin/ — very useful for managing data as a superuser.
"""

from django.contrib import admin
from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    """
    Custom admin view for the Expense model.
    Adds search, filter, and column display features to the admin panel.
    """

    # Columns shown in the list view
    list_display = ['title', 'user', 'amount', 'category', 'date', 'created_at']

    # Sidebar filter options
    list_filter = ['category', 'date', 'user']

    # Fields that are searchable
    search_fields = ['title', 'description', 'user__username']

    # Order by most recent date first
    ordering = ['-date']

    # Fields shown when editing an expense in admin
    readonly_fields = ['created_at', 'updated_at']
