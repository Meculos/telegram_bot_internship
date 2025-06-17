# Telegram Bot API with Django, DRF, Celery, Redis, and Brevo Email Integration

This project is a Django-based Telegram Bot API that allows users to register, authenticate, and receive welcome emails via Brevo (formerly Sendinblue). It uses Django REST Framework (DRF) for API endpoints, JWT for authentication, Celery with Redis for background tasks, and drf-spectacular for API documentation.

---

## 🚀 Features

- ✅ User Registration & Authentication (JWT-based)
- 📬 Email delivery using **Brevo SMTP**
- 🤖 Telegram Bot integration to register Telegram usernames
- 🧵 Celery + Redis for asynchronous task processing
- 🧪 Protected and public API routes
- 📘 Auto-generated Swagger & Redoc documentation via drf-spectacular

---

## 🗂️ Project Structure

## 🗂️ Project Structure

```text
telegram_bot/
│
├── intern_project/             # Django project settings
│   └── settings.py
│
├── telegram_bot_app/           # Core Django app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── tasks.py                # Celery tasks (e.g., email)
│
├── telegram_bot.py             # Telegram bot entry point
├── manage.py
├── .env                        # Environment variables (not committed)
└── api.http                    # API testing with VS Code REST Client
```


---

## 🧪 API Endpoints

### 🔐 JWT Authentication
| Method | URL | Description |
|--------|-----|-------------|
| POST | `/api/login_token/` | Obtain JWT access & refresh token |
| POST | `/api/token/refresh/` | Refresh access token |

### 👤 User Routes
| Method | URL | Description |
|--------|-----|-------------|
| POST | `/register/` | Register new user |
| POST | `/login/` | Login user |
| POST | `/logout/` | Logout and blacklist token |

### 🌐 API Access Control
| Method | URL | Description |
|--------|-----|-------------|
| GET | `/public_api/` | Open to all users |
| GET | `/private_api/` | Requires JWT auth |

---

## 📑 API Documentation

Using **drf-spectacular**, available at:

- [Swagger UI](http://localhost:8000/api/schema/swagger-ui/)
- [ReDoc](http://localhost:8000/api/schema/redoc/)
- [Raw Schema (OpenAPI JSON)](http://localhost:8000/api/schema/)

To enable, make sure `drf-spectacular` is installed and added to your URLs in `urls.py`.

---

## ⚙️ Setup Instructions

### 1. 🔧 Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Create virtual environment
Create a .env file in your project root with the following structure:

```bash
python -m venv t_bot
t_bot\Scripts\activate     # On Windows
pip install -r requirements.txt
```

### 3. Environment variables

```bash
SECRET_KEY='your-secret-key'
DEBUG='False'

# Email configuration via Brevo
EMAIL_HOST_USER='YOUR_BREVO_SMTP_USER'  
EMAIL_HOST_PASSWORD='YOUR_BREVO_SMTP_KEY'  
DEFAULT_FROM_EMAIL='your_verified_sender@example.com'

# Database
DB_NAME='your_db_name'
DB_USER='your_db_user'
DB_PASSWORD='your_db_password'
DB_HOST='localhost'
DB_PORT=5432

# Telegram Bot
TELEGRAM_BOT_TOKEN='your_telegram_bot_token'
```
Email notes:

SMTP integration is handled via Brevo.

You need to create an SMTP key from your Brevo dashboard and use that as EMAIL_HOST_PASSWORD.

EMAIL_HOST_USER is usually like 8fd231001@smtp-brevo.com.

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

Running the App Locally

1. 🌐 Run Django Development Server

```bash
python manage.py runserver
```

2. 🧠 Start Redis Server
Make sure Redis is installed. If using Windows, you can run it using:

```bash
redis-server --port 6380
```
Modify the port as needed.

3. 🌀 Start Celery Worker (with solo pool for Windows)

```bash
celery -A intern_project worker --pool=solo -l info
```
This handles background tasks like sending welcome emails.

4. 🤖 Run the Telegram Bot

```bash
python telegram_bot.py
```
The bot will listen for /start commands and register users in the database.


### Testing API Endpoints
You can test your endpoints using:

Postman

Curl

VS Code’s REST Client extension using the provided api.http file

### Additional Notes
api.http is included in the repo and serves as a test sheet for your endpoints.

Make sure your .env is never pushed to GitHub — add it to your .gitignore.

### Resources
Django REST Framework

drf-spectacular

Brevo SMTP Docs

Celery Documentation

Telegram Bot API





