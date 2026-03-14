from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegisterForm

User = get_user_model()


# =========================
# REGISTER
# =========================

class RegisterView(CreateView):

    model = User
    form_class = RegisterForm
    template_name = "registration/register.html"

    success_url = reverse_lazy("login")


# =========================
# PROFILE
# =========================

class ProfileView(LoginRequiredMixin, UpdateView):

    model = User

    fields = [
        "email",
        "phone",
        "country",
        "avatar",
    ]

    template_name = "users/profile.html"

    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user
