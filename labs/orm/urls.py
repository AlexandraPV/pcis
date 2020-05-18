
from django.urls import path , include
from . import views
app_name  = 'orm'
urlpatterns = [
    path('create/', views.create_order , name='create_order'),
    path('all_orders/', views.all_orders , name='all_orders'),
    path('delete_order/<int:pk>', views.delete_order , name='delete_order'),
    path('update_order/<int:pk>', views.update_order , name='update_order'),
    path('approve/<int:pk>', views.approve , name='approve'),
    path('update_approve/<int:pk>', views.update_approve , name='update_approve'),
]
