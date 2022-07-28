from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import LoginForm, RegistrationForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = LoginForm()
    context = {
        'page_title': 'Авторизация',
        'form': form,
        'main_button_value': 'Войти',
        'is_login': True,
    }
    return render(request, template_name='authapp/authentication_page.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:login_page'))
    else:
        form = RegistrationForm()
    context = {
        'page_title': 'регистрация',
        'form': form,
        'main_button_value': 'Регистрация',
        'is_login': False,
    }
    return render(request, template_name='authapp/authentication_page.html', context=context)
