from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    # path('',views.index, name="index"),
    path("", views.landing_page, name="landing_page"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
