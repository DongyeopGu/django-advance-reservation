from django.urls import path, include
from . import views

app_name = "reservation"

urlpatterns = [
    path('', views.index, name="index"),
    path('accounts/', include('accounts.urls'))
]