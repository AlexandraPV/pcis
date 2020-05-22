
from django.urls import path
from . import views
app_name  = 'dao'
urlpatterns = [
    path('find-one/<int:pk>', views.get_one , name='get_one'),
    path('delete_booking/<int:pk>', views.delete_booking , name='delete_booking'),
]
