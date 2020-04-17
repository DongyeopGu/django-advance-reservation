from django.db import models
from django.contrib.auth.models import AbstractUser # AbstractUser를 가져옴

class User(AbstractUser): # User 모델에 추가할 필드를 넣기 위해 AbstractUser 상속받음
    
    email_address = models.EmailField(blank=True)
    sweetpotato_size = models.CharField(max_length=30,blank=True)
    sweetpotato_num = models.IntegerField(blank=True)
    address = models.CharField(max_length=500, blank=True)
