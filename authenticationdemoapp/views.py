from django.shortcuts import render

# Create your views here.


def SignIn(request):
    return render(request,'athenticationdemoapp/signin.html')