from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def homepage(request):
    return render(request,'home.html')

def signpage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1!=pass2:
            return HttpResponse("Your password and confirm password don't match")
        else:     
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
        
    return render (request,'signup.html')
def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        passwd=request.POST.get('pass')
        
        user=authenticate(request,username=username,password=passwd)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("username and password incorrect")
    return render(request,'login.html')



def logoutpage(request):
    logout(request)
    return redirect('login')