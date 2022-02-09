from xml.dom.minidom import Attr
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from matplotlib import widgets
from .models import Helpdesk

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Kata laluan",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "E-mel",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Kata laluan",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Pengesahan kata laluan",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class HelpForm(ModelForm):
    class Meta:
        model = Helpdesk
        fields = ('user_email', 'help_status', 'email_subject', 'email_content')
        # if User.is_active:
        #     user = User.email
        # choice_value1 = [('1',user),()]
        # choice_value2 = [('1','Baru'),()]
        # widgets = {
        #     'user_email': forms.ChoiceField(choice= choice_value1 , attrs={'class':'form-control', 'placeholder': 'E-mel'}),
        #     'help_status': forms.ChoiceField(choice= choice_value2 , attrs={'class':'form-control', 'placeholder': 'Baru'}),
        #     'email_subject': forms.CharField(attrs={'class': 'form-control', 'placeholder': 'Subjek'}),
        #     'email_content': forms.CharField(attrs={'class': 'form-control', 'placeholder': 'Kandungan'}, widget=forms.Textarea(attrs={'rows':3})),
            # 'date_created': forms.DateField(auto_now = True)
        # }
