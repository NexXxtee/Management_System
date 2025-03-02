from django.contrib import admin
from users.models import CustomUser
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "role", "is_active", "is_staff", "date_created")
    search_fields = ("username", "email")
    list_filter = ("role", "is_active", "is_staff")
    
    admin.site.site_header = "Администрирование пользователей"
    admin.site.site_title = "Управление пользователями"