from django.shortcuts import render

from authapp.forms import AuthUserInShopLoginForm
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
        'register': 'register',
        'button_name': 'enter'
    }
    return render(request, 'authapp/login.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))
