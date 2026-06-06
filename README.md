<<<<<<< HEAD
# NAATCOOPS Cooperative Management System

NAATCOOPS is a modern cooperative management web application built using Flask, PostgreSQL, and Tailwind CSS.

The system helps cooperative organizations manage:

* Member registrations
* Savings contributions
* Loan applications
* Loan approvals/rejections
* Announcements
* Financial tracking

---

# Features

## Member Features

* Register as a cooperative member
* Login securely
* Add and manage savings
* Apply for loans
* Track loan application status
* View announcements from admin
* View financial dashboard

---

## Admin Features

* Approve member registrations
* View all cooperative members
* View and manage savings
* Approve or reject loans
* Post announcements
* Monitor cooperative activities
* Receive notifications

---

# Technologies Used

## Backend

* Flask
* Flask-SQLAlchemy
* Flask-Login
* Flask-Migrate
* Flask-WTF

## Frontend

* Tailwind CSS
* HTML5
* JavaScript

## Database

* PostgreSQL

## Deployment

* Render
* Gunicorn

---

# Project Structure

```bash
naatcoops/
│
├── app/
│   ├── admin/
│   ├── auth/
│   ├── member/
│   ├── static/
│   ├── templates/
│   ├── models.py
│   ├── config.py
│   ├── extensions.py
│   └── __init__.py
│
├── migrations/
├── requirements.txt
├── render.yaml
├── package.json
├── tailwind.config.js
├── run.py
└── README.md
```

---

# Installation Guide

## 1. Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

```bash
cd naatcoops
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

```bash
venv\\Scripts\\activate
```

### Linux/Mac

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

# Tailwind CSS Setup

## Install Node Modules

```bash
npm install
```

---

## Build Tailwind CSS

```bash
npx tailwindcss -i ./app/static/css/input.css -o ./app/static/css/output.css --watch
```

---

# PostgreSQL Database Setup

Create a PostgreSQL database named:

```bash
naatcoops
```

---

# Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_secret_key

DATABASE_URL=postgresql://postgres:password@localhost/naatcoops
```

---

# Database Migration

## Initialize Migration

```bash
flask db init
```

---

## Create Migration

```bash
flask db migrate -m "Initial Migration"
```

---

## Upgrade Database

```bash
flask db upgrade
```

---

# Create Admin Account

Open Python shell:

```bash
python
```

Then run:

```python
from app import create_app
from app.extensions import db
from app.models import User

app = create_app()

with app.app_context():

    admin = User(
        pf_number='ADMIN001',
        full_name='System Admin',
        email='admin@gmail.com',
        role='admin',
        approved=True
    )

    admin.set_password('admin123')

    db.session.add(admin)
    db.session.commit()
```

---

# Run Application

```bash
python run.py
```

Application will run on:

```bash
http://127.0.0.1:5000
```

---

# Deployment on Render

## Push Code to GitHub

```bash
git init
```

```bash
git add .
```

```bash
git commit -m "Initial commit"
```

```bash
git remote add origin YOUR_GITHUB_REPOSITORY
```

```bash
git push -u origin main
```

---

## Render Deployment Steps

1. Create a Render account
2. Connect GitHub repository
3. Create PostgreSQL database on Render
4. Add environment variables:

   * SECRET_KEY
   * DATABASE_URL
5. Deploy application

---

# Default Admin Login

```text
Email: admin@gmail.com
Password: admin123
```

---

# Future Improvements

* Email verification
* Loan repayment tracking
* PDF report generation
* SMS notifications
* Financial analytics dashboard
* Member profile pictures
* Transaction history
* Dark mode
* Audit logs

---

# License

This project is for educational and organizational use.

---

# Developer

Developed using:

* Flask
* PostgreSQL
* Tailwind CSS

For Cooperative Financial Management Systems.
=======
# naatcoops
>>>>>>> 6c0de2ce767d5078119f61dc262bff4586e7cdae
