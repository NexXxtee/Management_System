from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Имя")
    email = models.EmailField(max_length=200, unique=True, verbose_name="Email")
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата регистрации"
    )
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    position = models.ForeignKey(
        "Position",
        verbose_name="Должность",
        on_delete=models.CASCADE,
        related_name="users",
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.name


class Position(models.Model):
    class RoleChoices(models.TextChoices):
        STUDENT = "student", "студент"
        MANAGER = "manager", "менеджер"
        TEACHER = "teacher", "учитель"

    name = models.CharField(
        max_length=20, choices=RoleChoices.choices, default=RoleChoices.STUDENT
    )
    salary = models.PositiveIntegerField(blank=True, null=True, default=0)

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return self.name
