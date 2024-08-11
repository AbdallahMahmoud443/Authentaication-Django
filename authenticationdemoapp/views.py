from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,UserChangeForm
from django.contrib.auth import login,authenticate,update_session_auth_hash,logout
from authenticationdemoapp.forms import SignUpForm, UserChangeProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def SignIn(request):
    #form = UserCreationForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user) # make User Login After SignUp
            return redirect('HomePage')
    else:
       form = SignUpForm() 
    return render(request,'athenticationdemoapp/signin.html',{'form':form})


@login_required #  must user login to access this page 
def Home(request):
    return render(request,'athenticationdemoapp/home.html')

def Login(request):
    if request.method =='POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            # get data from form 
           userName =  form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           # check user in database
           user = authenticate(request,username=userName,password=password) 
           if user is not None:
                login(request,user)
           return redirect('HomePage') 
    else:
        form = AuthenticationForm()
    return render(request,'athenticationdemoapp/login.html',{'form':form})


@login_required
def ChangePassword(request):
    if request.method == 'POST':
       form = PasswordChangeForm(request.user,request.POST)
       if form.is_valid():
          user = form.save()
          update_session_auth_hash(request,user) #! Important to Maintain the session
          return redirect('HomePage')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'athenticationdemoapp/changePassword.html',{'form':form})


@login_required
def ChangeProfile(request):
    if request.method == 'POST':
       form = UserChangeProfileForm(instance=request.user,data=request.POST)
       if form.is_valid():
          form.save()
          return redirect('HomePage')
    else:
        form = UserChangeProfileForm(instance=request.user)
    return render(request,'athenticationdemoapp/changeProfile.html',{'form':form})


@login_required
def DeleteAcount(request):
    if request.method == 'POST':
       request.user.delete()
       return redirect('LoginPage')
    return render(request,'athenticationdemoapp/deleteAccount.html') # for get request


def LogOut(request):
    logout(request)
    return redirect('LoginPage')
    
   
   