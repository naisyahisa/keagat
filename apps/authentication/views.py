from django import template
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required
from .forms import HelpForm

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
        form = HelpForm(request.POST)
        if form.is_valid():
            form.save()
            #submitting true to the redirect to GET, pass down
            return HttpResponseRedirect('/helpdesk?submitted=True')
    #did not fill out the form
    else:
        form = HelpForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "home/helpdesk.html", {'form': form, 'submitted': submitted})