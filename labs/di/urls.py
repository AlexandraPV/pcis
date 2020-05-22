from django.urls import path
from . import views

app_name = 'di'
urlpatterns = [
    path('', views.di_home)
]
