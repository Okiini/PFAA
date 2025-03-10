from django.forms import ModelForm, TextInput, ModelChoiceField, Select, DateInput, CharField, IntegerField, EmailField, EmailInput, PasswordInput
from django import forms
from .models import *

class inputDataForm(ModelForm):
   class Meta:
        model = InputData
        fields = ['date', 'numberOfPeople', 'event', 'cheque', 'user']

        widgets = {

        }

class achievementForm(ModelForm):
   class Meta:
        model = Achievement
        fields = ['name', 'icon', 'category', 'limit', 'event', 'requiredQuantity', 'text', 'addExperience', 'addScore']

        widgets = {

        }