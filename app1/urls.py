from django.urls import path
from . import views
urlpatterns = [
path('login',views.login_registration,name='login_registration'),
    ]