from django.urls import path, include
from . import views

app_name = "reservation"

urlpatterns = [
    path('', views.index, name="index"),            # 메인 페이지
    path('board/', views.board, name="board"),      # 고구마 정보를 보여주기 위해
    path('notice/', views.notice, name="notice"),
    path('QandA/', views.qanda, name="qanda"),
    path('QandA_create/', views.QandA_create, name='qandacreate'),
    path('QandA/<int:qanda_pk>', views.QandA_detail, name='qandadetail'),
    path('QandA/<int:qanda_pk>/reply',views.reply_create, name='reply_create')
]