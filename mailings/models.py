from django.db import models
from django.conf import settings
from django.utils import timezone


class Recipient(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    comment = models.TextField(blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("view_all_recipients", "Can view all recipients"),
        ]

    def __str__(self):
        return self.email

#Сообщение
class Message(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("view_all_messages", "Can view all messages"),
        ]

    def __str__(self):
        return self.subject

#Рассылка
class Mailing(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    recipients = models.ManyToManyField(Recipient)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    @property
    def status(self):
        now = timezone.now()
        if now < self.start_time:
            return 'Создана'
        elif self.start_time <= now <= self.end_time:
            return 'Запущена'
        return 'Завершена'

    class Meta:
        permissions = [
            ("view_all_mailings", "Can view all mailings"),
        ]


#Попытка
class Attempt(models.Model):
    STATUS_CHOICES = [
        ('Успешно', 'Успешно'),
        ('Не успешно', 'Не успешно'),
    ]

    attempt_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    server_response = models.TextField()
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)