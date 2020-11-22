"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Комментарий"}
  
class AnketaForm(forms.Form):
    name = forms.CharField(label='Имя', min_length=2, max_length=100)
    gender = forms.CharField(label='Что случилось?', widget=forms.RadioSelect(choices=[('1', 'Вопрос о товаре'), ('2', 'У меня проблема')]), initial=1)
    internet = forms.ChoiceField(label='Кем Вы являетесь?', choices=[('1', 'Физ. лицо'), ('2', 'Юр. Лицо')], initial=1)
    notice = forms.BooleanField(label='Продублировать ваш запрос на почту?', required=False)
    email = forms.EmailField(label='E-mail', min_length=7)
    message = forms.CharField(label='Суть обращения',
                                widget=forms.Textarea(attrs={'rows':12,'cols':20}))

class BlogForm (forms.ModelForm):
    class Meta:
        model = Blog        
        fields = ('title','content','description','image')
        labels = {'title': "Заголовок",'content': "Полное содержание",'description': "Краткое содержание",'image': "Изображение"}