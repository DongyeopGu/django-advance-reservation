from django import forms
from .models import Reply, QandA

class QandAForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-control'
            }
        )
    )
    class Meta:
        model = QandA
        fields =['title', 'content']

class ReplyForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    class Meta:
        model = Reply
        fields = ['content']
        