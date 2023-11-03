from django.urls import path
from . import views

urlpatterns = [
    path('open/',views.file_open_by_pandas),
    path('open_null/',views.file_open_by_pandas_with_null),
    path('open_null/meanage/',views.file_open_by_pandas_with_null_meanage),
    path('normal_sort/', views.normal_sort),
    path('priority_queue/', views.priority_queue),
    path('bubble_sort/', views.bubble_sort),
]

