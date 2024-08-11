from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm



class SignUpForm(UserCreationForm):
    # Customize the fields
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    username = forms.CharField(max_length=20, required=True)
    email = forms.CharField(max_length=100,required=True)
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
        
class UserChangeProfileForm(UserChangeForm): # make custom form because django get all fields in profiling change
    # Customize the fields
    password =None
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    username = forms.CharField(max_length=20, required=True)
    email = forms.CharField(max_length=100,required=True)
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
