from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('application/', views.application, name="application"),    # 신청 페이지
    path('<int:pk>/update/', views.update, name="update"),          # 신청 정보 수정
    path('delete/', views.delete, name="delete"),          # 신청 정보 삭제
    path('<int:pk>/', views.detail, name="detail"),                 # 신청 정보 확인
    # path('reservation/', include('reservation.urls')),              # 
]