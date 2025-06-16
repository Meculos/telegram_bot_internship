from celery import shared_task
from django.core.mail import send_mail
from intern_project.settings import DEFAULT_FROM_EMAIL

@shared_task
def send_welcome_email(username, email):
    subject = "Welcome to Our Platform"
    message = f"Hi {username}, thanks for registering!"
    from_email = DEFAULT_FROM_EMAIL
    
    send_mail(subject, message, from_email, [email])
