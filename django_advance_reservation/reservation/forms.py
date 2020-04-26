from django import forms
from .models import Reply, QandA

class QandAForm(forms.ModelForm):
    class Meta:
        model = QandA
        fields =['title', 'content']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']