from django.urls import path
from .views import RegisterView, index, user_list, custom_logout
from django.contrib.auth.views import LoginView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path('', index, name='home'),
    path("logout/", custom_logout, name="logout"),
    path('users/', user_list, name='user_list'),
]