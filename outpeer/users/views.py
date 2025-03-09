from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from .forms import UserCreationForm
from django.core.paginator import Paginator
from .models import CustomUser
from django.contrib.auth import logout

def index(request):
    return render(request, 'users/index.html')


def user_list(request):
    users = CustomUser.objects.all()  # Получаем всех пользователей
    paginator = Paginator(users, 5)  # Пагинация: 5 пользователей на страницу
    page_number = request.GET.get("page")  # Получаем номер страницы из запроса
    page_users = paginator.get_page(page_number)  # Получаем пользователей для страницы

    return render(request, "users/user_list.html", {"page_users": page_users})
    
def custom_logout(request):
    logout(request)
    return redirect("login")  
    
class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "users/registration.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматически входим после регистрации
            return redirect("login")  # Перенаправляем на страницу входа
        return render(request, "users/registration.html", {"form": form})
