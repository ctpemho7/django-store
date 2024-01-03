from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from users.forms import UserLoginForm, UserRegisterForm


def login(request):
    if request.method == 'POST':
        data = request.POST
        form = UserLoginForm(data=data)
        if form.is_valid():
            username = data['username']
            password = data['password']
            account = auth.authenticate(username=username, password=password)
            if account:
                auth.login(request, account)
                return HttpResponseRedirect(reverse('index'))

    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        data = request.POST
        form = UserRegisterForm(data=data)
        if form.is_valid():
            # Сохраняем форму. Под капотом сам сохранит нужную модель
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)
