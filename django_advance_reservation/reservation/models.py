from django.db import models
from django.conf import settings

class QandA(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

class Reply(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    QandA = models.ForeignKey(QandA, on_delete=models.CASCADE)
    content = models.TextField()

    