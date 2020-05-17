from django.urls import path, include
from . import views

app_name = "reservation"

urlpatterns = [
    path('', views.index, name="index"),            # 메인 페이지
    path('board/', views.board, name="board"),      # 고구마 정보를 보여주기 위해
    path('notice/', views.notice, name="notice"),
    path('QandA/', views.QandA_list, name="QandA_list"),
    path('QandA_create/', views.QandA_create, name='QandA_create'),
    path('QandA/<int:qanda_pk>/', views.QandA_detail, name='QandA_detail'),
    path('QandA/<int:qanda_pk>/reply/',views.reply_create, name='reply_create'),
    path('QandA/<int:qanda_pk>/reply/<int:reply_pk>/delete/', views.reply_delete, name='reply_delete'),
    path('QandA/<int:qanda_pk>/update/', views.QandA_update, name='QandA_update'),
    path('QandA/<int:qanda_pk>/delete/', views.QandA_delete, name='QandA_delete'),
]