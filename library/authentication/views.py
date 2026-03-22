from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser


def register_view(request):
    if request.user.is_authenticated:
        return redirect('user:index')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        role = int(request.POST.get('role', 0))

        if CustomUser.get_by_email(email):
            return render(request, 'registration/signup.html', {'error': 'User with such email already exists'})

        user = CustomUser.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            role=role
        )
        login(request, user)
        messages.success(request, f"Welcome, {first_name}!")
        return redirect('user:index')

    return render(request, 'registration/signup.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('user:index')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('user:index')
        return render(request, 'registration/login.html', {'error': 'Invalid email or password'})
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('user:login')


@login_required
def user_list_view(request):
    users = CustomUser.get_all()
    return render(request, 'user_list.html', {'users': users})


@login_required
def user_detail_view(request, user_id):
    target_user = CustomUser.get_by_id(user_id)
    if not target_user:
        messages.error(request, "User not found.")
        return redirect('user:index')
    return render(request, 'user_detail.html', {'target_user': target_user})