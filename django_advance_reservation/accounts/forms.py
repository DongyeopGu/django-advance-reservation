from django.contrib.auth.forms import UserCreationForm # 기본 제공하는 modelForm을 사용하기 위해
from django import forms
from .models import User		# 커스터마이징한 User 모델을 불러옴
from django.contrib.auth.forms import UserChangeForm  # User 정보를 수정하기 위해
from django.contrib.auth import get_user_model		# User 정보를 수정할 때 정보를 가져오기 위해

class ApplicationForm(UserCreationForm):		# 상속받아 사용할 클래스 선언
    def __init__(self, *args, **kwargs):	# init을 통해 존재하던 필드의 정보를 수정
        super().__init__(*args, **kwargs)
        class_update_fields = ['password1', 'password2']
        for field_name in class_update_fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:					 # Meta 클래스를 통해 새로 추가한 필드의 attrs에서 form-control 추가
        model = User			 # Bootstrap을 사용하기 위해서 추가했음
        fields = (
            'username',
            'email_address',
            'sweetpotato_size',
            'sweetpotato_num',
            'address',
            'phone_number',
        )
        SIZE_CHOICES = (
            ('대','대'),
            ('중','중'),
            ('중','소'),
        )
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'email_address': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'sweetpotato_size': forms.Select(
                choices=SIZE_CHOICES,
                attrs={
                    'class': 'form-control',
                }
            ),
            'sweetpotato_num': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'phone_number': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

        
class ApplicationChangeForm(UserChangeForm):		# User 정보를 update하기 위하여 
    class Meta:
        model = get_user_model()
        fields = ['username', 'email_address','address', 'sweetpotato_num', 'sweetpotato_size', 'phone_number']