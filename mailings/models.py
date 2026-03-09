from django.db import models
from django.conf import settings
from django.utils import timezone


# =====================
# Recipient
# =====================

class Recipient(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=255)
    comment = models.TextField(blank=True)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recipients"
    )

    class Meta:
        ordering = ["email"]

        permissions = [
            ("view_all_recipients", "Can view all recipients"),
        ]

    def __str__(self):
        return f"{self.email} ({self.full_name})"


# =====================
# Message
# =====================

class Message(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="messages"
    )

    class Meta:
        ordering = ["subject"]

        permissions = [
            ("view_all_messages", "Can view all messages"),
        ]

    def __str__(self):
        return self.subject


# =====================
# Mailing
# =====================

class Mailing(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name="mailings"
    )

    recipients = models.ManyToManyField(
        Recipient,
        related_name="mailings"
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="mailings"
    )

    class Meta:
        ordering = ["-start_time"]

        permissions = [
            ("view_all_mailings", "Can view all mailings"),
        ]

    def __str__(self):
        return f"Mailing #{self.id}"

    @property
    def status(self):
        now = timezone.now()

        if now < self.start_time:
            return "Создана"

        elif self.start_time <= now <= self.end_time:
            return "Запущена"

        return "Завершена"


# =====================
# Attempt
# =====================

class Attempt(models.Model):

    STATUS_CHOICES = [
        ("SUCCESS", "Успешно"),
        ("FAILED", "Не успешно"),
    ]

    attempt_time = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
    )

    server_response = models.TextField()

    mailing = models.ForeignKey(
        Mailing,
        on_delete=models.CASCADE,
        related_name="attempts"
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="attempts"
    )

    class Meta:
        ordering = ["-attempt_time"]

    def __str__(self):
        return f"Attempt {self.id} - {self.status}"