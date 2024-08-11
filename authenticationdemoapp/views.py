from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from authenticationdemoapp.forms import SignUpForm
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
           print(user)
           if user is not None:
                login(request,user)
           return redirect('HomePage') 
    else:
        form = AuthenticationForm()
    return render(request,'athenticationdemoapp/login.html',{'form':form})