from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

@require_http_methods(['GET','POST'])
def signup(request):
    # 로그인한 사용자가 들어오면???
    if request.user.is_authenticated:
        return redirect("boards:index")
    

    # METHOD 가 GET 일 때와  POST 일 때
    # POST:  실제로 회원 가입 진행
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # 저장 및 자동로그인
            user = form.save()
            auth_login(request,user)
            return redirect("boards:index")
        
    # GET : 회원가입 페이지 보여줘야함
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET','POST'])
def login(request):
    # 로그인한 사용자가 들어오면???
    if request.user.is_authenticated:
        return redirect("boards:index")
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("boards:index")
        
    # GET : 회원가입 페이지 보여줘야함
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)


# 세션 데이터를 삭제하네? -> POST
@login_required
@require_POST
def logout(request):
    # 로그인 된 사용자만 로그아웃
    
    auth_logout(request)
    return redirect("boards:index")
    
    

@require_POST
def follow(request,user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person != request.user:
        if request.user in person.followers.all():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect('accounts:profile', person.pk)

def profile(request,user_pk):
    person = get_user_model().objects.get(pk=user_pk)
    context={
        'person' : person
    }
    return render(request, 'accounts/profile.html',context)