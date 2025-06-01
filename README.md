# CRM Project with Django

This is a customer relationship management (CRM) web application built with Django. It includes user registration, login, order management, and role-based access control.

## 🚀 Features

* User Registration & Authentication
* Role-based Access Control (Customer, Superadmin)
* Order Creation, Update, and Deletion
* Profile Management
* Admin Dashboard
* Order Status Management (Superadmin only)

## 💠 Tech Stack

* Python 3.12
* Django
* PostgreSQL (optional alongside default SQLite)
* SonarQube (Code Quality Analysis)
* Salt & Pepper (Remote automation with SaltStack)

## ⚖️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2. Create and activate a virtual environment:

```bash
python3 -m venv env
source env/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables securely using `python-decouple`:

```bash
# .env file
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/dbname
SONAR_TOKEN=your_sonar_token
```

5. Run migrations:

```bash
python manage.py migrate --database=default  # SQLite
# or
python manage.py migrate --database=postgres  # PostgreSQL (if configured in settings)
```

6. Start the development server:

```bash
python manage.py runserver
```

## 🧪 Run Tests

```bash
python manage.py test
```

## 📊 SonarQube Integration

To analyze code quality using SonarQube:

1. Start SonarQube server:

```bash
cd sonarqube/bin/linux-x86-64
./sonar.sh start
```

2. Run the scanner:

```bash
sonar-scanner -Dsonar.projectKey=crmproject \
              -Dsonar.sources=. \
              -Dsonar.host.url=http://localhost:9000 \
              -Dsonar.token=your_sonar_token
```

> Make sure you have SonarQube running and `sonar.token` configured correctly.

## 🡢🔐 Salt & Pepper Integration with SonarQube

This project uses [SaltStack](https://saltproject.io) via its Python interface `pepper` for managing remote execution and optionally automating SonarQube scans across environments.

### Setup Instructions

#### 1. Install Pepper

```bash
pip install pepper
```

#### 2. Configure Pepper (`~/.pepperrc`)

```ini
[main]
USERNAME = your_salt_user
PASSWORD = your_salt_password
EAUTH = pam
SERVER = https://your-salt-api-url
```

#### 3. Trigger SonarQube Scan via Salt

```bash
pepper --client local 'webserver*' cmd.run 'cd /srv/myapp && sonar-scanner'
```

Or using Salt state:

```yaml
sonar_scan:
  cmd.run:
    - name: "cd /home/app && sonar-scanner"
    - cwd: /home/app
```

```bash
salt 'myminion' state.apply sonar
```

### Security Notes

* Do **not** store Salt credentials in the codebase.
* Use secure authentication and access control.

## 📁 Project Structure

```
crmproject/
├── manage.py
├── users/
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│   ├── templates/
│   └── ...
├── crmproject/
│   └── settings.py
└── requirements.txt
```

## 🧑‍💻 Author

Developed by Shamim.

---

Feel free to contribute or open issues for enhancements!
