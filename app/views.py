"""
Definition of views.
"""
from .forms import AnketaForm
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import Blog
from .models import Comment
from .forms import CommentForm
from .forms import BlogForm


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Связаться с нами',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'message':'Информация о магазине',
            'year':datetime.now().year,
        }
    )

def pool(request):
    """Опросник"""
    assert isinstance(request, HttpRequest)
    data = None
    gender = {'1':'Вопрос о товаре', '2':'У меня проблема'}
    internet = {'1':'Физ. лицо','2':'Юр. лицо'}
    if request.method == 'POST':
        form = AnketaForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['gender'] = gender[form.cleaned_data['gender'] ]
            data['internet'] = internet[form.cleaned_data['internet'] ]
            if(form.cleaned_data['notice'] == True):
                data['notice'] = 'Да'
            else:
                data['notice'] = 'Нет'
            data['email'] = form.cleaned_data['email']
            data['message'] = form.cleaned_data['message']
            form = None
    else:
        form = AnketaForm()
    return render(
        request,
        'app/pool.html',
        {
            'title':'Обратная связь',
            'form':form,
            'data':data,
            'year':datetime.now().year
        }
    )
def links(request):
    """Renders the links page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            'title':'Полезные ресурсы',
            'message':'Вам может пригодиться',
            'year':datetime.now().year,
        }
    )
def blog(request):
    """Renders the contact page."""
    posts = Blog.objects.all()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        {
            'title':'Блог',
            'posts' : posts,
            'year':datetime.now().year,
        }
    )

def registration(request):
    assert isinstance(request, HttpRequest)
    if request.method == "POST": # после отправки формы
       regform = UserCreationForm (request.POST)
       if regform.is_valid(): #валидация полей 
         reg_f = regform.save(commit=False) # не сохраняем автоматически данные 
         reg_f.is_staff = False # запрещен вход в административный 
         reg_f.is_active = True # активный 
         reg_f.is_superuser = False # не является 
         reg_f.date_joined = datetime.now() # дата 
         reg_f.last_login = datetime.now() # дата последней 
         reg_f.save() # сохраняем изменения после добавления 
         return redirect('home') # переадресация на главную страницу после 
    else:
       regform = UserCreationForm() # создание объекта формы для ввода данных нового 
    return render(
       request,
       'app/registration.html',
       {
         'title':'Регистрация',
         'regform': regform, # передача формы в шаблон веб-страницы
         'year':datetime.now().year,
       }
    )
def blogpost(request, parametr):
    """Renders the about page."""
    post_1 = Blog.objects.get(id=parametr)
    comments = Comment.objects.filter(post=parametr)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = Blog.objects.get(id=parametr)
            comment_f.save()

            return redirect('blogpost', parametr=post_1.id)
    else:
        form = CommentForm()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blogpost.html',
        {   'form': form,
            'comments': comments,
            'post_1': post_1,
            'year':datetime.now().year
        }
    )

def newpost(request):
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.author = request.user
            blog_f.save()

            return redirect('blog')
    else:
        blogform = BlogForm()
    
    return render(
        request,
        'app/newpost.html',
        {
            'blogform': blogform,
            'title': 'Добавить статью блога',
            'year':datetime.now().year,
        }
    )

def videopost(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title':'Видео',
            'year':datetime.now().year,
        }
    )