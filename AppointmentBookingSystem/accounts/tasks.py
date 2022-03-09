from celery.app import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.checks import messages
from django.core.mail import send_mail, EmailMessage
from AppointmentBookingSystem import settings
from allauth.account.models import EmailAddress

@shared_task(bind=True)
def send_invitation_email(self, userdata, *args, **kwargs):
    mail_subject = "AppointmentBookingSystem platform Invitation"
    message = "if rgjnvvvvvvvvvvvvvvvvvvvvvvvvvvvfjkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
    to_email = self.userdata.email
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True,
    )
    # userd = EmailAddress.objects.get_or_create(user=userdata,
    #                                            email=userdata.email,
    #                                            verified=True,
    #                                            primary=True)
    return "Done!!!!"
