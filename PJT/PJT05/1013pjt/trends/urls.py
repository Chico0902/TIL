from django.urls import path
from . import views

app_name = 'trends'
urlpatterns = [
    path('base', views.base, name='base'),
    path('keyword', views.keyword, name='keyword'),
    path('keyword/<int:pk>', views.keyword_detail, name='keyword_detail'),
    path('crawling', views.crawling, name='crawling'),
    path('crawling/histogram/', views.crawling_histogram, name='crawling_histogram'),
    path('crawling/advanced/', views.advanced, name='advanced'),
    path('keyword/delete/', views.delete, name='delete'),
]