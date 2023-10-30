from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'root/index.html'

class UserView(TemplateView):
    template_name = 'profile/personal-info.html'