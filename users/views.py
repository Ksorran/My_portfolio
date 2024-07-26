from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from .forms import LoginUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'


def logout_user(request):
    return HttpResponse("logout")
