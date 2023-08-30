from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, EmptyErrorList


# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES, error_class=EmptyErrorList)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect(reverse('profile'))
        else:
            context = {
                'error': form.error_messages.values(),
                'form': form
            }
            return render(request, 'app_auth/register.html', context)
    else:
        form = CustomUserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'app_auth/register.html', context)


def login_view(request):
    redirect_url = reverse('profile')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(redirect_url)
    return render(request, 'app_auth/login.html', {'error': 'Пользователь не найден'})


@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    return render(request, 'app_auth/profile.html')


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

