from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.views import View
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.core.paginator import Paginator
from .models import CustomUser, EmailVerification
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'users/index.html')


@login_required
def user_list(request):
    users = CustomUser.objects.all()  # Получаем всех пользователей
    paginator = Paginator(users, 5)  # Пагинация: 5 пользователей на страницу
    page_number = request.GET.get("page")  # Получаем номер страницы из запроса
    page_users = paginator.get_page(page_number)  # Получаем пользователей для страницы

    return render(request, "users/user_list.html", {"page_users": page_users})
    
    
class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "users/registration.html", {"form": form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Деактивируем пользователя до подтверждения email
            user.save()
            
            # Создаём код подтверждения
            verification = EmailVerification.objects.create(user=user)
            send_mail(
                "Подтверждение регистрации",
                f"Ваш код подтверждения: {verification.code}",
                "noreply@outpeer.com",
                [user.email],
                fail_silently=False,
            )
            return redirect("verify_email", user_id=user.id) 
        return render(request, "users/registration.html", {"form": form})


class VerifyEmailView(View):
    def get(self, request, user_id):
        return render(request, "users/verify_email.html", {"user_id": user_id})

    def post(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        code = request.POST.get("code")
        
        verification = get_object_or_404(EmailVerification, user=user, code=code)
        if verification:
            user.is_active = True  # Активируем пользователя
            user.save()
            verification.delete()  # Удаляем использованный код
            login(request, user)  # Логиним пользователя
            return redirect("home")

        return render(request, "users/verify_email.html", {"user_id": user_id, "error": "Неверный код"})


class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")