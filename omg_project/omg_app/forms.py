from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
from .models import AIModel, Data

class AIModelForm(forms.ModelForm):
    class Meta:
        model = AIModel
        fields = '__all__'
        
class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = '__all__'
