from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class user_form(UserCreationForm):

	email=forms.CharField(max_length=100)
	class Meta():
		model=User
		fields=('username','email','password')
