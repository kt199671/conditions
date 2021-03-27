

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, get_user_model
User = get_user_model()
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .forms import SignUpForm, LoginForm
from datetime import date
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView




def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        print(signup_form.is_valid())
        if signup_form.is_valid():
            signup_form.save()
            username = signup_form.cleaned_data.get('username')
            password = signup_form.cleaned_data.get('password1')
            position = signup_form.cleaned_data.get('position')
            user = authenticate(request, username=username, password=password, position=position)
            messages.add_message(request, messages.SUCCESS, 'ユーザー登録が完了しました！')
            login(request, user)
            return redirect('condition:post')
    else:
        signup_form = SignUpForm()
    context = {
        'signup_form': signup_form,
    }
    return render(request, 'accounts/create.html', context)

@require_http_methods(['GET', 'POST'])
def login_function(request):
    """ログインページ"""
    if request.method != 'POST':
        login_form = LoginForm()
    else:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.clean_username()
            password = login_form.clean_password()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # return redirect('condition:index')
                return redirect('condition:post')
        else:
            pass
    context = {
        'login_form': login_form
    }
    return render(request, 'accounts/login.html', context)

def index(request):
    return render(request, 'accounts/index.html')
