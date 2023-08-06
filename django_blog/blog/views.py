from django.shortcuts import redirect, render, get_object_or_404
from .models import Post # . перед models указывает на то, что мы обращаемся к файлу из текущей деректории
#деректории в которой лежит данный фал views.py

#Импортируем временные зоны 
from django.utils import timezone

#Импортируем формы
from .forms import PostForm




def post_list(request):
    #Отсортируем и отфильтруем посты по дате публикации
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render (request, 'blog/post_list.html' , {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post' : post})


def post_new(request):
     form = PostForm
     if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
     return render(request, 'blog/post_edit.html', {'form' : form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

   


