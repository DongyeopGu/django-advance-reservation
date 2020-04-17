from django.db import models

# 사진 및 정보를 업로드 하기 위한 모델 정의
class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    