from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Post, Comment
from .forms import AddNewPost, AddNewComment
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
    try:
        post = Post.objects.get(pk = post_id)
    except Post.DoesNotExist as identifier:
        return HttpResponse('None comments now.')
    comments_list = Comment.objects.filter(post = post)
    form = AddNewComment(request.POST)
    context = {
        "comment_list":comments_list,
        "post": post,
        'form': form,
    }
    return render(request, 'forum/dialog.html', context)
def creation(request):
    form = AddNewPost(request.POST)
    context = {
        'form': form,
        }
    if request.method == 'POST':
        new_post = Post()
        new_post.post_user = request.user
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
def post_like_mm(request, post_id):
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
def post_like_dialog(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post.post_like += 1
    post.save()
    try:
        post = Post.objects.get(pk = post_id)
    except Post.DoesNotExist as identifier:
        return HttpResponse('None comments now.')
    comments_list = Comment.objects.filter(post = post)
    form = AddNewComment(request.POST)
    context = {
        "comment_list":comments_list,
        "post": post,
        'form': form,
    }
    return render(request, 'forum/dialog.html', context)
def comment_like(request, post_id, comment_id):
    post = get_object_or_404(Post, pk = post_id)
    comment = get_object_or_404(Comment, pk = comment_id)
    comment.comment_like += 1
    comment.save()
    try:
        post = Post.objects.get(pk = post_id)
    except Post.DoesNotExist as identifier:
        return HttpResponse('None comments now.')
    comments_list = Comment.objects.filter(post = post)
    form = AddNewComment(request.POST)
    context = {
        "comment_list":comments_list,
        "post": post,
        'form': form,
    }
    return render(request, 'forum/dialog.html', context)
def comment(request, post_id):
    try:
        post = Post.objects.get(pk = post_id)
    except Post.DoesNotExist as identifier:
        return HttpResponse('None comments now.')
    comments_list = Comment.objects.filter(post = post)
    form = AddNewComment(request.POST)
    context = {
        "comment_list":comments_list,
        "post": post,
        'form': form,
    }
    if request.method == 'POST':
        new_comment = Comment()
        new_comment.comment_user = request.user
        new_comment.comment_text = form.data["comment_text"]
        new_comment.comment_data = datetime.datetime.now()
        new_comment.comment_like = 0
        new_comment.post = get_object_or_404(Post, pk = post_id)
        new_comment.save()
    return render(request, "forum/dialog.html", context)