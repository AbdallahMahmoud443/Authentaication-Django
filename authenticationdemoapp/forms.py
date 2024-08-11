from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from authenticationdemoapp.models import CustomUser



class SignUpForm(UserCreationForm):
    # Customize the fields
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    username = forms.CharField(max_length=20, required=True)
    email = forms.CharField(max_length=100,required=True)
    country = forms.ChoiceField(choices=CustomUser.COUNTRY_CHOICES,required=True)
    address = forms.CharField(max_length=30,required=True)
    
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','email','country','address']
        
class UserChangeProfileForm(UserChangeForm): # make custom form because django get all fields in profiling change
    # Customize the fields
    password =None
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    username = forms.CharField(max_length=20, required=True)
    email = forms.CharField(max_length=100,required=True)
    country = forms.ChoiceField(choices=CustomUser.COUNTRY_CHOICES,required=True)
    address = forms.CharField(max_length=30,required=True)
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','email','country','address']
