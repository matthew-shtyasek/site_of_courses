from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render

from authapp.forms import LoginForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    context = {
        'page_title': 'Авторизация',
        'login_form': form,
    }
    return render(request, template_name='authapp/login_page.html', context=context)
