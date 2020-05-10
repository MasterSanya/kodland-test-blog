from django.db import models
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


def index(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all().order_by('-published_date')
    posts_count = 10
    if len(posts) < posts_count:
        posts_count = len(posts)
    if posts_count > 0:
        latest_post = model_to_dict(posts[0])
        previous_posts = posts[1:posts_count]

        return render(request, 'index.html', {
            'latest_post': latest_post,
            'previous_posts': previous_posts,
            'posts': posts,
        })

    else:
        return render(request, 'index.html', {})


# def new_post(request):
#     if request.method == "POST":
#         title = request.POST['title']
#         text = request.POST['text']
#
#         if len(title) == 0:
#             return render(request, 'post_edit.html', {
#                 'error': 'Не указано название публикации!'
#             })
#
#         if len(text) == 0:
#             return render(request, 'post_edit.html', {
#                 'error': 'Не указан текст публикации!'
#             })
#
#         if 'cover' in request.FILES:
#             cover = request.FILES['cover']
#             Post(
#                 author=request.user,
#                 title=title,
#                 cover=cover,
#                 text=text.replace('\n', '<br />'),
#             ).publish()
#         else:
#             Post(
#                 author=request.user,
#                 title=title,
#                 text=text.replace('\n', '<br />'),
#             ).publish()
#
#         return redirect('/')
#     else:
#         return render(request, 'post_edit.html', {})

def new_post(request):
    if request.method == "POST":
        title = request.POST['title']
        text = request.POST['text']

        if len(title) == 0:
            return render(request, 'post_edit.html', {
                'error': 'Не указано название публикации!'
            })

        if len(text) == 0:
            return render(request, 'post_edit.html', {
                'error': 'Не указан текст публикации!'
            })

        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})
