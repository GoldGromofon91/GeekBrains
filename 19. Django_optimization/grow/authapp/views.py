from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_init
from django.dispatch import receiver
from django.shortcuts import render

from authapp.forms import AuthUserInShopLoginForm, GrowUserCreationForm, GrowUserChangeForm, GrowUserProfileChangeForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

from authapp.models import GrowUser, GrowUserProfile
from grow.settings import DOMAIN_NAME


def login(request):
    redirect_param = request.GET.get('next', '')
    email = None

    if request.method == 'POST':
        login_form = AuthUserInShopLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            redirect_to = request.POST.get('redirect-param')
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(redirect_to or reverse('mainapp:index'))

    else:
        login_form = AuthUserInShopLoginForm()

    context = {
        'form': login_form,
        'title_page': 'аутентификация',
        'register': 'зарегистрироваться',
        'button_name': 'войти',
        'redirect_to': redirect_param,
        'domain_name': f'{DOMAIN_NAME}/auth/user/verify/',

    }
    return render(request, 'authapp/login.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))


def register_user(request):
    email = None
    activ_key = None
    if request.method == 'POST':
        login_user_form = GrowUserCreationForm(request.POST, request.FILES)
        if login_user_form.is_valid():
            user = login_user_form.save(commit=False)
            user.is_active = False
            user.generate_activation_key()
            email = user.email
            activ_key = user.activation_key
            user.save()
            if not user.send_user_confirm_email():
                return HttpResponseRedirect(reverse('authapp:register'))

            context = {
                'form': login_user_form,
                'title_page': 'регистрация',
                'button_name': 'зарегистрироваться',
                'button_index': 'на главную',
                'domain': f'{DOMAIN_NAME}/auth/user/verify/{email}/{activ_key}'

            }
            return render(request, 'authapp/register.html', context=context)
    else:
        login_user_form = GrowUserCreationForm()
    context = {
        'form': login_user_form,
        'title_page': 'регистрация',
        'button_name': 'зарегистрироваться',
        'button_index': 'на главную',
    }
    return render(request, 'authapp/register.html', context=context)


def profile_edit(request):
    if request.method == 'POST':
        login_form = GrowUserChangeForm(request.POST, request.FILES, instance=request.user)
        profile_form = GrowUserProfileChangeForm(request.POST, request.FILES, instance=request.user.growuserprofile)
        if login_form.is_valid() and profile_form.is_valid():
            login_form.save()
            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        login_form = GrowUserChangeForm(instance=request.user)
        profile_form = GrowUserProfileChangeForm(instance=request.user.growuserprofile)

    context = {
        'form': login_form,
        'profile_form': profile_form,
        'title_page': 'редактирование профиля',
        'button_name': 'сохранить',
        'button_index': 'на главную',
    }
    return render(request, 'authapp/update.html', context=context)


@receiver(post_save, sender=GrowUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        GrowUserProfile.objects.create(user=instance)


@receiver(post_save, sender=GrowUser)
def save_profile(sender, instance, **kwargs):
    instance.growuserprofile.save()


def verify_user(request, email, activation_key):
    user = get_user_model().objects.get(email=email)
    if user.activation_key == activation_key and not user.is_activation_key_ttl_expired:
        user.is_active = True
        user.save()
        auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')

        return render(request, 'authapp/confirm_verification.html')
