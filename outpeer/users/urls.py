from django.urls import path
from .views import register, verify_email, user_login, user_logout, users_list


urlpatterns = [
    path("register/", register, name="register"),
    path("verify-email/<int:user_id>/", verify_email, name="verify_email"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("users/", users_list, name="users_list")
]