from pyexpat import model
from xml.dom.minidom import Attr
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from matplotlib import widgets
from .models import Helpdesk

GROUP_CHOICES =(
    ("staff","Staf"),
    ("helpdesk_staff","Staf Helpdesk"),
    ("admin_staff","Admin"),
)

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
    group_staff = forms.ChoiceField(widget=forms.Select, choices = GROUP_CHOICES)
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
        fields = ('username', 'email', 'group_staff', 'password1', 'password2')

class HelpForm(ModelForm):
    help_status =  forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),initial='Baru')
   
    help_subject = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Subjek",
                "class": "form-control"
                
            }
        ))
    help_content = forms.CharField(
    widget=forms.Textarea(
        attrs={
            "placeholder": "Komen",
            "class": "form-control",
            "rows":3 
        }
    ))
    
    class Meta:
        model = Helpdesk
        # exclude = ('help_author')
        fields = ('help_status','help_subject', 'help_content')
        
class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password', 'placeholder':'Kata laluan lama'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password','placeholder':'Kata laluan baru'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password', 'placeholder':'Pengesahan kata laluan baru'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
        labels = {
                'old_password':"",
                'new_password1':"",
                'new_password2':""
            }        
