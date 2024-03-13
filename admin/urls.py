from django.urls import path
from . import views

app_name = 'admin'

urlpatterns = [
    # path('',views.index, name="index"),
    path('request/', views.submit_admin_request, name='submit_admin_request'),
    path('manage/', views.manage_admin_requests, name='manage_admin_requests'),
    path('approve/<int:request_id>/', views.approve_request, name='approve_request'),
    path('reject/<int:request_id>/', views.reject_request, name='reject_request'),
]