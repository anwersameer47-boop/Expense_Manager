# 💰 Expense Tracker Web Application

A beginner-friendly Django web application for tracking personal expenses.
Built as a college minor project using Python Django, SQLite, Bootstrap 5, and Django Templates.

---

## 📋 Features

- **User Authentication** — Register, Login, Logout
- **Dashboard** — Total expenses, monthly expenses, category breakdown, recent activity
- **Expense Management** — Add, Edit, Delete, View all expenses
- **7 Categories** — Food, Travel, Shopping, Bills, Education, Entertainment, Other
- **Responsive Design** — Works on mobile, tablet, and desktop
- **Flash Messages** — Instant feedback for every action
- **Form Validation** — Client and server-side validation
- **Empty States** — Friendly messages when no data exists
- **Admin Panel** — Manage all data via Django's built-in admin

---

## 🛠️ Tech Stack

| Layer      | Technology             |
|------------|------------------------|
| Backend    | Python Django 4.2      |
| Database   | SQLite (built-in)      |
| Frontend   | HTML, CSS, Bootstrap 5 |
| Templates  | Django Templates       |
| Icons      | Bootstrap Icons        |

---

## 📁 Project Structure

```
expense-tracker/
│
├── manage.py                    # Django management utility
├── requirements.txt             # Python dependencies
├── db.sqlite3                   # SQLite database (auto-created)
├── .gitignore                   # Files to ignore in Git
├── README.md                    # This file
│
├── expense_tracker/             # Django project settings
│   ├── __init__.py
│   ├── settings.py              # Project configuration
│   ├── urls.py                  # Root URL routing
│   ├── wsgi.py
│   └── asgi.py
│
├── expenses/                    # Main Django app
│   ├── __init__.py
│   ├── models.py                # Database models (Expense)
│   ├── views.py                 # Page logic / controllers
│   ├── urls.py                  # App URL patterns
│   ├── forms.py                 # Django forms (Registration, Expense)
│   ├── admin.py                 # Admin panel configuration
│   └── migrations/              # Database migration files
│
├── templates/                   # HTML templates
│   ├── base.html                # Base layout (navbar, footer, messages)
│   ├── home.html                # Landing / home page
│   ├── registration/
│   │   ├── login.html           # Login page
│   │   └── register.html        # Registration page
│   └── expenses/
│       ├── dashboard.html       # Main dashboard
│       ├── expense_list.html    # All expenses table
│       ├── expense_form.html    # Add / Edit expense form
│       └── expense_confirm_delete.html  # Delete confirmation
│
└── static/
    └── css/
        └── style.css            # Custom CSS styles
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1 — Clone or Download the Project

```bash
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
```

### Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3 — Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4 — Create a Superuser (Admin Access)

```bash
python manage.py createsuperuser
# Enter: username, email (optional), password
```

### Step 5 — Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit: **http://127.0.0.1:8000/**

Admin panel: **http://127.0.0.1:8000/admin/**

---

## 🖥️ How to Run on Replit

1. Open the project in Replit
2. The app starts automatically via the configured workflow
3. Click the **Run** button or visit the preview URL
4. Register a new account and start tracking expenses!

To create a superuser on Replit:
- Open the **Shell** tab
- Navigate to the project: `cd expense-tracker`
- Run: `python manage.py createsuperuser`

---

## 📤 Upload to GitHub

```bash
# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit — Expense Tracker Django App"

# Create a new repo on github.com, then:
git remote add origin https://github.com/yourusername/expense-tracker.git
git branch -M main
git push -u origin main
```

---

## 📱 Pages & Routes

| URL                        | Page                  | Auth Required |
|----------------------------|-----------------------|---------------|
| `/`                        | Home / Landing        | No            |
| `/register/`               | Register              | No            |
| `/login/`                  | Login                 | No            |
| `/logout/`                 | Logout                | Yes           |
| `/dashboard/`              | Dashboard             | Yes           |
| `/expenses/`               | All Expenses          | Yes           |
| `/expenses/add/`           | Add Expense           | Yes           |
| `/expenses/<id>/edit/`     | Edit Expense          | Yes           |
| `/expenses/<id>/delete/`   | Delete Expense        | Yes           |
| `/admin/`                  | Admin Panel           | Superuser     |

---

## 🔧 Key Commands

```bash
# Run migrations after model changes
python manage.py makemigrations
python manage.py migrate

# Create admin superuser
python manage.py createsuperuser

# Start the server
python manage.py runserver

# Start on a specific port
python manage.py runserver 0.0.0.0:8000

# Collect static files (for production)
python manage.py collectstatic
```

---

## 👨‍🎓 About

Built as a college minor project to demonstrate:
- Django MVC architecture
- User authentication with Django's built-in auth system
- CRUD operations with Django ORM
- Bootstrap 5 responsive design
- Django forms and validation
- SQLite database management

---

*Made with ❤️ using Python Django*
