Thank you for the clarification!

Here's an updated version of your README file that includes:

* 🔐 Salt & Pepper-based password hashing using bcrypt
* 🕵️‍♂️ Audit logging
* 📊 SonarQube integration

---

````markdown
# CRMProjecet (Django-based CRM System)

A lightweight Customer Relationship Management (CRM) system built using Django. This app includes user role management (customer, superadmin, subscriber), order processing, audit logging, secure password handling, and SonarQube integration.

---

## 🚀 Features

- User registration, login, logout
- Role-based access (Customer, Superadmin, Subscriber)
- Create, update, delete orders (permissions enforced)
- Profile management for customers
- Secure password storage using bcrypt with salt and pepper
- Audit logging of critical actions
- SonarQube integration for code quality analysis

---

## 🛡️ Security Highlights

### 🔐 Password Hashing with Salt & Pepper (bcrypt)

- Uses bcrypt for hashing passwords.
- Salt is generated per password by bcrypt itself.
- An application-level pepper is added before hashing.
- Pepper is stored securely in environment variables using `python-decouple`.

```python
from decouple import config
import bcrypt

PEPPER = config("PASSWORD_PEPPER")

def hash_password(raw_password):
    peppered = (raw_password + PEPPER).encode()
    return bcrypt.hashpw(peppered, bcrypt.gensalt())
````

---

## 🕵️ Audit Logging

* Tracks user actions such as login, logout, order changes.
* Implemented using Django signals + `auditlog` package.
* Stores timestamps, actor, and changed fields.

---

## 📊 Code Quality: SonarQube Integration

* SonarScanner is integrated for continuous code analysis.
* Tracks bugs, vulnerabilities, code smells, and security hotspots.
* Configuration available in `sonar-project.properties`.

Example:

```properties
sonar.projectKey=crmproject
sonar.sources=.
sonar.host.url=http://localhost:9000
sonar.token=<your_token_here>
```

---

## 🧰 Setup Instructions

1. Clone the project:

```bash
git clone https://github.com/yourusername/crmproject.git
cd crmproject
```

2. Create and activate virtual environment:

```bash
python3 -m venv env
source env/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure environment variables (in `.env` file):

```env
DEBUG=True
SECRET_KEY=your-secret
DATABASE_URL=postgres://user:pass@localhost:5432/dbname
PASSWORD_PEPPER=your-secure-pepper-string
```

5. Run migrations:

```bash
python manage.py migrate
```

6. Run development server:

```bash
python manage.py runserver
```

---

## 🐘 Database Support

* SQLite (default for development)
* PostgreSQL (for production or staging)
* Supports multiple databases using Django’s `DATABASES` config

---

## 🔍 Future Improvements

* Add Docker support
* REST API endpoints
* CI/CD pipeline with GitHub Actions
* Notification system for order updates

---

