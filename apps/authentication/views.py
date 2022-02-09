from django import template
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from matplotlib.style import context
from .forms import LoginForm, PasswordChangingForm, SignUpForm, HelpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Butiran tidak sah. Sila cuba lagi.'
        else:
            msg = 'Ralat mengesahkan maklumat. Sila cuba lagi.'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'Pengguna baru telah dicipta - sila <a href="/login">log masuk</a>.'
            success = True

            return redirect("/login/")

        else:
            msg = 'Butiran tidak dapat disahkan. Sila cuba lagi.'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

@login_required(login_url="/login/")
def help_form(request):
    submitted = False
    if request.method == "POST":
        print("masuk method post")
        form = HelpForm(request.POST)
        print('form', form)
        if form.is_valid():
            print("masuk save data")
            print(form)
            form.save()
            #submitting true to the redirect to GET, pass down
            return HttpResponseRedirect('home/helpdesk?submitted=True')
        else:
            print('Maklumat tidak sah')
    #did not fill out the form
    else:
        form = HelpForm
        if 'submitted' in request.GET:
            print("masuk submitted == True")
            submitted = True

    return render(request, "home/helpdesk.html", {'form': form, 'submitted': submitted})

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'accounts/password_success.html', {})