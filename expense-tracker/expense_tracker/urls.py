"""
URL Configuration for the Expense Tracker Project.

This file maps URL patterns to the correct views/apps.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django Admin Panel
    path('admin/', admin.site.urls),

    # All expense app URLs (includes auth, dashboard, CRUD)
    path('', include('expenses.urls')),
]
