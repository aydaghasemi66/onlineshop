from django.urls import path
from .views import *
urlpatterns = [ 
    path("logout/",logout,name="logout"),
    #path('login/',login , name='account_login'),
]