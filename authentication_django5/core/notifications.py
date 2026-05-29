from twilio.rest import Client
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings


def send_whatsapp(to_number, message):
    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        response = client.messages.create(
            from_=settings.TWILIO_WHATSAPP_FROM,
            to=f"whatsapp:+{to_number}",
            body=message
        )
        print(f"WhatsApp SID: {response.sid}")
        print(f"WhatsApp Status: {response.status}")
    except Exception as e:
        print(f"Twilio error: {e}")


def send_email(to_email, subject, body):
    message = Mail(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_emails=to_email,
        subject=subject,
        plain_text_content=body
    )
    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return response.status_code
    except Exception as e:
        print(f"SendGrid error: {e}")


def send_activation_token(user_email, whatsapp_number, token):
    subject = "Activate your account"
    message = f"Your activation token is: {token}\n\nThis token expires in 1 hour."

    # send_email(user_email, subject, message)
    send_whatsapp(whatsapp_number, message)