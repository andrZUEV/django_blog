from django.shortcuts import render
from .models import Post # . перед models указывает на то, что мы обращаемся к файлу из текущей деректории
#деректории в которой лежит данный фал views.py

#Импортируем временные зоны 
from django.utils import timezone


def post_list(request):
    #Отсортируем и отфильтруем посты по дате публикации
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render (request, 'blog/post_list.html' , {'posts' : posts})