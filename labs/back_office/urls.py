
from django.urls import path , include
from . import views
app_name  = 'home'
urlpatterns = [
    path('', views.home , name='main'),
    path('client-list/', views.client_list , name='client_list'),
    path('update/<int:pk>', views.update , name='update'),
    path('delete/<int:pk>', views.delete , name='delete'),
]
