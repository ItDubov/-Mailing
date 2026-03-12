from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from .forms import RegisterForm

User = get_user_model()


class RegisterView(CreateView):

    model = User
    form_class = RegisterForm
    template_name = "registration/register.html"

    success_url = reverse_lazy("login")