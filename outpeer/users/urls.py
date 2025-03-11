from django.urls import path
from .views import RegisterView, index, user_list, CustomLogoutView, VerifyEmailView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("", index, name="home"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("users/", user_list, name="user_list"),
    path("verify-email/<int:user_id>/", VerifyEmailView.as_view(), name="verify_email"),
]
