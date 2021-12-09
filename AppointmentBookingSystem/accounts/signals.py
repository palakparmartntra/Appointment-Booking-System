from allauth.account.signals import email_confirmed
from django.dispatch import receiver
from accounts.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save
from AppointmentBookingSystem.settings import EMAIL_HOST_USER

SIGNUP_SUBJECT = (
    'Tntra: Appointment Booking'
)

SIGNUP_MESSAGES = (
    'Your Email address is Login Password. NOTE: Once you login then Reset Your password'
)
SUBJECT=SIGNUP_SUBJECT
MESSAGES = SIGNUP_MESSAGES


@receiver(email_confirmed)
def email_confirmed_(request, email_address, **kwargs):
    user = User.objects.get(email=email_address.email)
    user.email_verified = True
    user.save()


@receiver(post_save, sender=User)
def mail_send(sender, instance, **kwargs):
    if kwargs['created'] and instance.email_verified:
        send_mail(
            SUBJECT,
            MESSAGES,
            EMAIL_HOST_USER,
            [instance.email],
        )