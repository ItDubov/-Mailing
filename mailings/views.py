from django.views.decorators.cache import cache_page
from django.shortcuts import render
from django.utils import timezone
from .models import Mailing, Recipient


def home(request):
    total_mailings = Mailing.objects.count()
    active_mailings = Mailing.objects.filter(
        start_time__lte=timezone.now(),
        end_time__gte=timezone.now()
    ).count()
    recipients_count = Recipient.objects.count()

    return render(request, 'home.html', {
        'total_mailings': total_mailings,
        'active_mailings': active_mailings,
        'recipients_count': recipients_count,
    })

@cache_page(60)
def home(request):
    total_mailings = Mailing.objects.count()
    active_mailings = Mailing.objects.filter(
        start_time__lte=timezone.now(),
        end_time__gte=timezone.now()
    ).count()
    recipients_count = Recipient.objects.count()

    return render(request, 'home.html', {
        'total_mailings': total_mailings,
        'active_mailings': active_mailings,
        'recipients_count': recipients_count,
    })