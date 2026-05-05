# account/notifications.py

from twilio.rest import Client
from django.core.mail import send_mail
from django.conf import settings


def send_whatsapp(to_number, message):
    """
    to_number: just the digits, e.g. "923001234567" (with country code, no +)
    """
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    client.messages.create(
        from_=settings.TWILIO_WHATSAPP_FROM,
        to=f"whatsapp:+{to_number}",
        body=message
    )


def send_email(to_email, subject, message):
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[to_email],
    )


def send_activation_token(user_email, whatsapp_number, token):
    """
    Sends the activation token via both email and WhatsApp.
    """
    subject = "Activate your account"
    message = f"Your activation token is: {token}\n\nThis token expires in 1 hour."

    send_email(user_email, subject, message)
    send_whatsapp(whatsapp_number, message)