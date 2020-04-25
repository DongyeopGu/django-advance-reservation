from django.urls import path, include
from . import views

app_name = "reservation"

urlpatterns = [
    path('', views.index, name="index"),            # 메인 페이지
    path('board/', views.board, name="board"),      # 고구마 정보를 보여주기 위해
    path('notice/', views.notice, name="notice"),
    path('Q&A/', views.qanda, name="qanda"),
]