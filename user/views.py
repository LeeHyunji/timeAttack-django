from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import get_user_model
from django.contrib import auth

# Create your views here.
def home_view(request):
    user = request.user.is_authenticated  # 사용자가 인증을 받았는지 (로그인이 되어있는지)
    if user:
        return render(request,'user/home.html')
    else:
        return redirect('/login')


def sign_up_view(request):
    if request.method == 'GET':
        return render(request,'user/signup.html')

    elif request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        phone = request.POST.get('phone',None)
        address = request.POST.get('address',None)

        if username == '' or password == '':
            return render(request, 'user/signup.html', {'error': '사용자 이름과 패스워드는 필수 값 입니다'})
        else :
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html', {'error':'사용자가 존재합니다.'})
            else:
                User.objects.create_user(username=username, 
                password=password, 
                phone=phone,
                address=address)

                return redirect('/login/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        print(username)
        print(password)

        me = auth.authenticate(request, username=username, password=password)
        print(me)
        if me is not None: 
            auth.login(request, me)
            return redirect('/home')
            
        else:
            return render(request,'user/login.html',{'error':'유저이름 혹은 패스워드를 확인 해 주세요'})

    elif request.method == 'GET':
        return render(request,'user/login.html')
