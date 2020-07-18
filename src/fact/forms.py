from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class Contact_us_form(forms.ModelForm):
    class Meta:
        model = Contact_us
        fields = [
            'name',
            'email',
            'mobile',
            'comment'
        ]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Blog_form(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'heading',
            'text',
            'pic'
        ]


class Client_form(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class Staff_form(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'


class Visitor_form(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = '__all__'


class Trainer_form(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'


class Equipment_form(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'


class Achivement_form(forms.ModelForm):
    class Meta:
        model = Achivement
        fields = '__all__'
