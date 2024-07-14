from django.views.generic import TemplateView
from users.models import User



class IndexView(TemplateView):
    template_name = 'portfolio/index.html'
