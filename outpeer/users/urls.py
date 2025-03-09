from django.urls import path
from .views import RegisterView, index, user_list
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path('', index, name='home'),
    path('users/', user_list, name='user_list')
]