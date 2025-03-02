from django.contrib import admin
from users.models import User, Position


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "date_created"]
    list_display_links = ["name"]
    
    
@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ["name", "salary"]