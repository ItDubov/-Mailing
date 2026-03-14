from django.views.generic import (
    ListView, CreateView, UpdateView,
    DeleteView, DetailView, TemplateView
)
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Mailing, Recipient, Message, Attempt


# =========================
# HOME
# =========================
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["total_mailings"] = Mailing.objects.count()
        context["active_mailings"] = Mailing.objects.filter(
            start_time__lte=now,
            end_time__gte=now,
        ).count()
        context["recipients_count"] = Recipient.objects.count()
        return context


# =========================
# MAILING CRUD
# =========================
class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    template_name = "mailings/mailing_list.html"

    def get_queryset(self):
        if self.request.user.has_perm("mailings.view_all_mailings"):
            return Mailing.objects.all()
        return Mailing.objects.filter(owner=self.request.user)


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    template_name = "mailings/mailing_detail.html"


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    fields = ["start_time", "end_time", "message", "recipients"]
    template_name = "mailings/mailing_form.html"
    success_url = reverse_lazy("mailing_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    fields = ["start_time", "end_time", "message", "recipients"]
    template_name = "mailings/mailing_form.html"
    success_url = reverse_lazy("mailing_list")

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    template_name = "mailings/mailing_confirm_delete.html"
    success_url = reverse_lazy("mailing_list")

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)


# =========================
# RECIPIENT CRUD
# =========================
class RecipientListView(LoginRequiredMixin, ListView):
    model = Recipient
    template_name = "mailings/recipient_list.html"  # <- список
    context_object_name = "recipients"

    def get_queryset(self):
        return Recipient.objects.filter(owner=self.request.user)


class RecipientCreateView(LoginRequiredMixin, CreateView):
    model = Recipient
    fields = ["email", "full_name", "comment"]
    template_name = "mailings/recipient_form.html"
    success_url = reverse_lazy("recipient_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class RecipientUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipient
    fields = ["email", "full_name", "comment"]
    template_name = "mailings/recipient_form.html"
    success_url = reverse_lazy("recipient_list")

    def get_queryset(self):
        return Recipient.objects.filter(owner=self.request.user)


class RecipientDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipient
    template_name = "mailings/recipient_confirm_delete.html"
    success_url = reverse_lazy("recipient_list")

    def get_queryset(self):
        return Recipient.objects.filter(owner=self.request.user)


# =========================
# MESSAGE CRUD
# =========================
class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = "mailings/message_list.html"  # <- список
    context_object_name = "messages"

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ["subject", "body"]
    template_name = "mailings/message_form.html"
    success_url = reverse_lazy("message_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    fields = ["subject", "body"]
    template_name = "mailings/message_form.html"
    success_url = reverse_lazy("message_list")

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = "mailings/message_confirm_delete.html"
    success_url = reverse_lazy("message_list")

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)

class AttemptListView(LoginRequiredMixin, ListView):
    model = Attempt
    template_name = "mailings/attempt_list.html"

    def get_queryset(self):
        return Attempt.objects.filter(
            mailing__owner=self.request.user
        )
