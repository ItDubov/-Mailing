from django.core.mail import send_mail
from django.utils import timezone
from .models import Attempt


def send_mailing(mailing):
    now = timezone.now()

    if not (mailing.start_time <= now <= mailing.end_time):
        raise ValueError("Рассылка вне допустимого периода")

    for recipient in mailing.recipients.all():
        try:
            send_mail(
                mailing.message.subject,
                mailing.message.body,
                None,
                [recipient.email],
                fail_silently=False
            )
            Attempt.objects.create(
                mailing=mailing,
                status='Успешно',
                server_response='OK'
            )
        except Exception as e:
            Attempt.objects.create(
                mailing=mailing,
                status='Не успешно',
                server_response=str(e)
            )