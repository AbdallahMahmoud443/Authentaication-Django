from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
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
    return render(request,'athenticationdemoapp/login.html')