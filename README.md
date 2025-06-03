# CRM Project

A Django-based CRM (Customer Relationship Management) system with user roles, order management, and PostgreSQL integration. It includes role-based access control, secure password hashing (bcrypt with salt and pepper), and audit logging.

## 🚀 Features

* User authentication and registration
* Role-based dashboards (Customer, Superadmin, Subscriber)
* Order creation and management
* Profile editing
* Order status updates by Superadmin only
* PostgreSQL and SQLite support
* Audit logging for key actions
* SonarQube integration for static code analysis
* Secure password hashing using bcrypt with salt and pepper

## 📦 Technologies Used

* Python 3.12
* Django 4.x
* PostgreSQL
* SQLite (default, for dev)
* SonarQube
* bcrypt (with salt & pepper)

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/shamim93/secure-crm.git
cd crmproject
```

### 2. Create Virtual Environment

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
PASSWORD_PEPPER=your_pepper_string
```

### 5. Database Setup

Run migrations:

```bash
python manage.py migrate
```

> ⚠️ Make sure the database user has permission to create tables and databases during testing.

### 6. Run Server

```bash
python manage.py runserver
```

## 🔐 Security: Salt and Pepper Password Hashing

This project uses **bcrypt** with both salt and pepper:

* **Salt** is generated per password (handled by bcrypt).
* **Pepper** is a secret global string stored in environment variables.

### Example:

```python
import bcrypt
import os

PEPPER = os.environ.get('PASSWORD_PEPPER')

def hash_password(raw_password):
    combined = (raw_password + PEPPER).encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(combined, salt)
```

## 📊 SonarQube Integration

To run code analysis:

1. Start SonarQube:

```bash
cd sonarqube/bin/linux-x86-64
./sonar.sh start
```

2. Run scanner:

```bash
sonar-scanner -Dsonar.projectKey=YourProject \
              -Dsonar.sources=. \
              -Dsonar.host.url=http://localhost:9000 \
              -Dsonar.token=your_token_here
```

## 📜 Audit Logging

All key actions (like order creation, update, deletion) are tracked using an audit logging middleware for better traceability and debugging.

## 🧪 Testing

Run Django tests:

```bash
python manage.py test
```

> 🔒 Ensure the database user has sufficient permissions to create and destroy test databases.

Sample unit tests are implemented for order functionality including:

* Customer can create order
* Subscriber cannot create order
* Customer sees their own orders
