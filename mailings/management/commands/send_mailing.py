from django.core.management.base import BaseCommand
from mailings.models import Mailing
from mailings.services import send_mailing


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('mailing_id', type=int)

    def handle(self, *args, **kwargs):
        mailing = Mailing.objects.get(id=kwargs['mailing_id'])
        send_mailing(mailing)
        self.stdout.write("Рассылка отправлена")