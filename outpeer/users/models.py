from django.db import models
from django.contrib.auth.models import AbstractUser
import random

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

    def generate_verification_code(self):
        """Генерирует случайный 6-значный код"""
        code = str(random.randint(100000, 999999))
        self.verification_code = code
        self.save()
        return code
    
    def __str__(self):
        return self.username 


class EmailConfirmationCode(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="confirmation_code")
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Код для {self.user.email}: {self.code}"