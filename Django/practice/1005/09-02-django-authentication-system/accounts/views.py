from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm




# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인(세션 데이터 처리)
            auth_login(request, form.get_user())
            # next_url 처리
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    # 장고의 기본 User모델 기반으로 동작
    # -> 버그발생
    # form = UserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            # 1. DB에 user 저장
            # 2. 내가 현재 저장하고자 하는 객체를 반환
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

def delete(request):
    request.user.delete()
    return redirect('articles:index')


def update(request):
    if request.method == 'POST':
        # pass
        form = CustomUserChangeForm(request.POST, instance= request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)