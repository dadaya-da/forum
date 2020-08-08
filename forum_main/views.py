from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Post, Comment
from .forms import AddNewPost
import time, datetime
# Create your views here.
def register(request):
    context = {
        11: 'asd'
    }
    return render(request, 'forum/register.html', context)
def main_menu(request):
    posts_displayed_list = Post.objects.order_by('-post_data')[:3]
    posts_list = Post.objects.all()
    context = {
        "post_list":posts_list,
        "post_displayed_list":posts_displayed_list,
    }
    return render(request, 'forum/main-menu.html', context)
def dialog(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    comments_list = get_list_or_404(Comment, post = post)
    context = {
        "comment_list":comments_list,
        "post": post,
    }
    return render(request, 'forum/dialog.html', context)
def creation(request):
    form = AddNewPost(request.POST)
    context = {
        'form': form,
        }
    if request.method == 'POST':
        new_post = Post()
        new_post.post_name = form.data["post_name"]
        new_post.post_text = form.data["post_text"]
        new_post.post_data = datetime.datetime.now()
        new_post.post_like = 0
        new_post.save()
        return render(request, 'forum/post_create_complete.html', context)
    return render(request, 'forum/create_post.html', context)
def post_create_complete(request):
    context = {
        1:1
    }
    return render(request, 'create_post.html', context)
def like(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post.post_like += 1
    post.save()
    posts_displayed_list = Post.objects.order_by('-post_data')[:3]
    posts_list = Post.objects.all()
    context = {
        "post_list":posts_list,
        "post_displayed_list":posts_displayed_list,
    }
    return render(request, 'forum/main-menu.html', context)