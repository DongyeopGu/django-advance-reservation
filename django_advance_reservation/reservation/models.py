from django.db import models
from django.conf import settings

# 사진 및 정보를 업로드 하기 위한 모델 정의
class QandA(models.Model):
    title = models.CharField(max_length=100)
    user =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()

class Reply(models.Model):
    content = models.TextField()
    QandA = models.ForeignKey(QandA, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    