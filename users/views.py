from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')