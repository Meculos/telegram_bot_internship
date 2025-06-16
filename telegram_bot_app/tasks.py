from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_welcome_email(username, email):
    subject = "Welcome to Our Platform"
    message = f"Hi {username}, thanks for registering!"
    from_email = settings.EMAIL_HOST_USER
    
    send_mail(subject, message, from_email, [email])
