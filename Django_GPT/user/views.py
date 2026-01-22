from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout, get_user_model
from django.contrib import messages

User = get_user_model()

# Create your views here.

def login(request,pk):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            if pk == 2:
                return redirect('AI:AI_two_page')
            elif pk == 3:
                return redirect('AI:AI_three_page')
            else:
                return redirect('AI:main')
        else:
            print('Login Fail')
    if not request.user.is_authenticated and (pk == 2 or pk == 3):
        messages.error(request, "로그인 후 사용가능합니다!")

    return render(request,'user/login.html')

def logout_fun(request):
    logout(request)
    return redirect('user:login' ,pk=0)

def signup(request):
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        
        new_user = User.objects.create_user(username=u, password=p)
        
        auth_login(request, new_user)
        return redirect('AI:main') 
        
    return render(request, 'user/signup.html')