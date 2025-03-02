from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Имя")
    email = models.EmailField(max_length=200, unique=True, verbose_name="Email")
    position = models.OneToOneField(
        "Position",
        verbose_name="Должность",
        on_delete=models.CASCADE,
        related_name="roles",
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Position(models.Model):
    class RoleChoices(models.TextChoices):
        STUDENT = "student", "студент"
        MANAGER = "manager", "менеджер"
        TEACHER = "teacher", "учитель"

    role = models.CharField(max_length=100, choices=RoleChoices.choices, default=RoleChoices.STUDENT)
    salary = models.IntegerField(blank=True, default=0)

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
