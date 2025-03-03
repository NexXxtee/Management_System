from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import UserRegistrationForm, RegistrationForm
from .models import CustomUser
import random
from django.core.mail import send_mail
from django.conf import settings
from .models import EmailConfirmationCode
from django.contrib import messages
from django.core.paginator import Paginator

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False 
            user.save()

            # Генерируем код подтверждения
            confirmation_code = random.randint(100000, 999999)
            EmailConfirmationCode.objects.create(user=user, code=confirmation_code)

            # Отправляем код на email
            send_mail(
                "Подтверждение регистрации",
                f"Ваш код подтверждения: {confirmation_code}",
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )

            return redirect("confirm_email")  
    else:
        form = UserRegistrationForm()

    return render(request, "users/register.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Делаем пользователя неактивным
            verification_code = user.generate_verification_code()  # Генерируем код
            user.save()

            # Отправляем email
            send_mail(
                subject="Подтверждение регистрации",
                message=f"Ваш код подтверждения: {verification_code}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )

            return redirect("verify_email", user_id=user.id)
    else:
        form = RegistrationForm()
    return render(request, "users/register.html", {"form": form})


def verify_email(request, user_id):
    user = CustomUser.objects.get(id=user_id)

    if request.method == "POST":
        code = request.POST.get("code")
        if code == user.verification_code:
            user.is_active = True  # Делаем аккаунт активным
            user.verification_code = None  # Очищаем код
            user.save()
            return redirect("login")  # После подтверждения — на страницу входа
        else:
            return render(request, "users/verify_email.html", {"error": "Неверный код!"})

    return render(request, "users/verify_email.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  # После входа перенаправляем на главную
        else:
            messages.error(request, "Неверный логин или пароль")

    return render(request, "users/login.html")


def user_logout(request):
    logout(request)
    return redirect("login")  # После выхода перенаправляем на страницу входа


User = get_user_model()  # Получаем кастомную модель пользователя

def users_list(request):
    users = User.objects.all()
    paginator = Paginator(users, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "users/users_list.html", {"page_obj": page_obj})