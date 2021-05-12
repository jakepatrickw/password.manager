from django import forms
from django.db import models
from django.forms import fields
from .models import UsernamePasswordService

class PassWordForm(forms.ModelForm):

    class Meta:
        model = UsernamePasswordService
        fields = ['user', 'user_name', 'service', 'password']