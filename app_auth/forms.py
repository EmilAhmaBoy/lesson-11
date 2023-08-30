from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model

User = get_user_model()


class EmptyErrorList(ErrorList):
    def __str__(self):
        return ''


class CustomUserCreationForm(UserCreationForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs['class'] = 'form-control form-control-lg'
    #     self.fields['username'].help_text = ''
    #     self.fields['username'].min_length = 5
    #     self.fields['username'].max_length = 24
    #     self.fields['last_name'].widget.attrs['class'] = 'form-control form-control-lg'
    #     self.fields['first_name'].widget.attrs['class'] = 'form-control form-control-lg'
    #     self.fields['password1'].widget.attrs['class'] = 'form-control form-control-lg'
    #     self.fields['password1'].help_text = ''
    #     self.fields['password2'].widget.attrs['class'] = 'form-control form-control-lg'
    #     self.fields['password2'].help_text = ''

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

    username = forms.CharField(label='Никнейм', min_length=3, max_length=24,
                               widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    first_name = forms.CharField(label='Имя', min_length=0, max_length=32,
                                 widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    last_name = forms.CharField(label='Фамилия', min_length=0, max_length=32,
                                widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     new = User.objects.filter(username=username)
    #     if new.count():
    #         raise ValidationError('Пользователь уже зарегистрирован!')
    #     elif len(username) < 3:
    #         raise ValidationError('Длина никнейма не должна быть меньше 3 символов в длину!')
    #     elif len(username) > 24:
    #         raise ValidationError('Длина никнейма не должна превышать 24 символов в длину!')
    #     return username
    #
    # def clean_password2(self):
    #     password1 = self.cleaned_data['password1']
    #     password2 = self.cleaned_data['password2']
    #
    #     if len(password1) < 8:
    #         raise ValidationError('Длина пароля должна быть меньше 8 символов в длину!')
    #     elif password1 != password2:
    #         raise ValidationError('Пароли не совпадают!')
    #     return password2

