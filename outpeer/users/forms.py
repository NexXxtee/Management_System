from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    username = forms.CharField(max_length=50, label="Имя пользователя")
    role = forms.ChoiceField(choices=CustomUser.RoleChoices.choices, label="Роль")

    class Meta:
        model = CustomUser
        fields = ["email", "username", "role", "password1", "password2"]