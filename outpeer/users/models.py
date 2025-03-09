from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class RoleChoices(models.TextChoices):
        STUDENT = "Student", "Студент"
        MANAGER = "Manager", "Менеджер"
        ADMINISTRATOR = "Administrator", "Администратор"
        TEACHER = "Teacher", "Учитель"

    email = models.EmailField(
        max_length=60, unique=True, verbose_name="Email"
    )  
    username = models.CharField(
        max_length=150, unique=True, verbose_name="Имя пользователя"
    )  
    role = models.CharField(
        max_length=20,
        choices=RoleChoices.choices,
        default=RoleChoices.STUDENT,
        verbose_name="Роль"
    )

    # Определяем, какое поле будет использоваться для аутентификации
    USERNAME_FIELD = "email"  # Теперь логин будет происходить по email
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.username} ({self.role})"