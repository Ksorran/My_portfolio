from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from my_portfolio import settings
from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/user_form.html'
    extra_context = {'button': 'Войти', 'title': "Вход"}


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:login')
    extra_context = {'button': 'Регистрация', 'title': "Регистрация"}


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = "users/profile.html"
    extra_context = {'title': "Профиль", 'button': 'Сохранить', 'default_image': settings.DEFAULT_USER_IMAGE}

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/user_form.html"
    extra_context = {'title': "Изменение пароля", 'button': 'Сохранить'}
