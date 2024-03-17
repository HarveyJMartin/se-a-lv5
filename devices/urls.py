from django.urls import path
from . import views


app_name = 'devices'

urlpatterns = [
    # path('',views.index, name="index"),
    path('', views.all_devices, name='all_devices'),
    path('new/', views.create_device, name='create_device'),
    path('<int:pk>/edit/', views.edit_device, name='edit_device'),
    path('<int:pk>/delete/', views.delete_device, name='delete_device'),
]