from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        exclude = ('updated_at', 'created_at')


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput) or \
                    isinstance(field.widget, forms.EmailField) or \
                    isinstance(field.widget, forms.PasswordInput) or \
                    isinstance(field.widget, forms.EmailInput) or \
                    isinstance(field.widget, forms.TimeInput):
                field.widget.attrs.update({'placeholder': field.label})
