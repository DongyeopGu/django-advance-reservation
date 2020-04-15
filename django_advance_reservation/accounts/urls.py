from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('application/', views.application, name="application"),
    path('<int:pk>/update/', views.update, name="update"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/', views.detail, name="detail"),
    path('reservation/', include('reservation.urls')),
]