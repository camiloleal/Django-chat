from django import forms
from models import ChatProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username','email', 'password')
		success_url = ('/login/')

class ProfileForm(forms.ModelForm):
	class Meta:
		model = ChatProfile
