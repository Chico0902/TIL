from django.urls import path
from . import views

app_name="accounts"
urlpatterns = [
    # 회원가입
    path('signup/', views.signup, name="signup"),
    # 로그인
    path('login/', views.login, name="login"),
    # 로그아웃
    path('logout/', views.logout, name="logout"),
    # 팔로우 데이터 저장 및 팔로우 데이터 삭제
    # path('<user_pk>/follow/', views.follow, name="follow")
    path('<user_pk>', views.profile, name='profile')

]
