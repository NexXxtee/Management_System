from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class RoleChoices(models.TextChoices):
        STUDENT = "student", "Студент"
        MANAGER = "manager", "Менеджер"
        TEACHER = "teacher", "Учитель"

    email = models.EmailField(unique=True, verbose_name="Email")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    role = models.CharField(max_length=20, choices=RoleChoices.choices, default=RoleChoices.STUDENT)
    is_active = models.BooleanField(default=True, verbose_name="Активен")  
    is_staff = models.BooleanField(default=False, verbose_name="Сотрудник")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username 
