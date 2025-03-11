from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["email", "username", "role", "password1", "password2"]

    role = forms.ChoiceField(
        choices=CustomUser.RoleChoices.choices, 
        label="Роль", 
        widget=forms.Select()
    )