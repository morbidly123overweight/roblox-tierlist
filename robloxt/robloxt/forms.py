from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Hra_v_Robloxe

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=63)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class HraForm(forms.ModelForm):
    class Meta:
        model = Hra_v_Robloxe
        fields = ['meno_hry', 'obrazok', 'popis_hry']
        labels = {
            'meno_hry': 'Názov hry',
            'obrazok': 'Obrázok hry',
            'popis_hry': 'Popis hry'
        }
        widgets = {
            'popis_hry': forms.Textarea(attrs={'rows': 4}),
        }
