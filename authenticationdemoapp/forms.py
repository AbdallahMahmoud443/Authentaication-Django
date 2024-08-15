
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import UserChangeForm
from sqlalchemy import false

# from authenticationdemoapp.models import CustomUser



class SignUpForm(UserCreationForm):
    # Customize the fields
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    username = forms.CharField(max_length=20, required=True)
    email = forms.CharField(max_length=100,required=True)
    # country = forms.ChoiceField(choices=CustomUser.COUNTRY_CHOICES,required=True)
    # address = forms.CharField(max_length=30,required=True)
    
    class Meta:
        #model = CustomUser
        #fields = ['first_name','last_name','username','email','country','address']
        model = User
        fields = ['first_name','last_name','username','email']
        
class UserChangeProfileForm(UserChangeForm): # make custom form because django get all fields in profiling change    
    # Customize the fields
    password =None
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    username = forms.CharField(max_length=20, required=True)
    email = forms.CharField(max_length=100,required=True)
    # country = forms.ChoiceField(choices=CustomUser.COUNTRY_CHOICES,required=True)
    # address = forms.CharField(max_length=30,required=True)
    
    class Meta:
        # model = CustomUser
        # fields = ['first_name','last_name','username','email','country','address']
        model = User
        fields = ['first_name','last_name','username','email']
        
class RoleForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']
        
class CreateStaffEmployeeForm(UserCreationForm):
    role = forms.ModelChoiceField(queryset=Group.objects.all(),required=false) #! Trick
    class Meta:
        model=User
        fields = ['first_name','last_name','username','email','role']
        
class UpdateStaffEmployeeForm(UserChangeForm):
    role = forms.ModelChoiceField(queryset=Group.objects.all(),required=false) #! Trick
    password =None
    class Meta:
        model=User
        fields = ['first_name','last_name','username','email','role']

