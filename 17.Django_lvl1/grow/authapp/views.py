from django.shortcuts import render

from authapp.forms import AuthUserInShopLoginForm,GrowUserCreationForm,GrowUserChangeForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        login_form = AuthUserInShopLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        login_form = AuthUserInShopLoginForm()
    context = {
        'form': login_form,
        'title_page': 'аутентификация',
        'register': 'зарегестрироваться',
        'button_name': 'войти'
    }
    return render(request, 'authapp/login.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))


def register_user(request):
    if request.method == 'POST':
        login_form = GrowUserCreationForm(request.POST,request.FILES)
        if login_form.is_valid():
            login_form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        login_form = GrowUserCreationForm()
    context = {
        'form': login_form,
        'title_page': 'регистрация',
        'button_name': 'зарегестрироваться',
        'button_index':'на главную'
    }
    return render(request, 'authapp/register.html', context=context)


def profile_edit(request):
    if request.method == 'POST':
        login_form = GrowUserChangeForm(request.POST,request.FILES, instance=request.user)
        if login_form.is_valid():
            login_form.save()
            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        login_form = GrowUserChangeForm(instance=request.user)

    context = {
        'form': login_form,
        'title_page': 'редактирование профиля',
        'button_name': 'сохранить',
        'button_index':'на главную'
    }
    return render(request, 'authapp/update.html', context=context)