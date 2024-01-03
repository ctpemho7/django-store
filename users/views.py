from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm


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
            messages.success(request, 'Вы успешно зарегистрировались!')
            # Сохраняем форму. Под капотом сам сохранит нужную модель
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)


def profile(request):
    if request.method == 'POST':
        # получаем конкретного пользователя через instance
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    context = {'form': form}
    return render(request, 'users/profile.html', context)