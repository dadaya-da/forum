from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Q
from .models import Post, Comment
from .forms import AddNewPost, AddNewComment, Search
import time, datetime
# Create your views here.
def register(request):
    form_search = Search(request.GET)
    context = {
        'form_search':form_search
    }
    return render(request, 'forum/register.html', context)
def main_menu(request):
    posts_displayed_list = Post.objects.order_by('-post_data')[:3]
    posts_list = Post.objects.all()
    posts_popular_list = Post.objects.order_by('-post_like')[:3]
    form_search = Search(request.GET)
    context = {
        "post_list":posts_list,
        "post_displayed_list":posts_displayed_list,
        "form_search": form_search,
        "post_popular_list":posts_popular_list,
    }
    return render(request, 'forum/main-menu.html', context)
def dialog(request, post_id):
    try:
        post = Post.objects.get(pk = post_id)
    except Post.DoesNotExist as identifier:
        return HttpResponse('None comments now.')
    comments_list = Comment.objects.filter(post = post)
    form = AddNewComment(request.POST)
    form_search = Search(request.GET)
    context = {
        "comment_list":comments_list,
        "post": post,
        'form': form,
        'form_search': form_search,
    }
    return render(request, 'forum/dialog.html', context)
def creation(request):
    form = AddNewPost(request.POST)
    form_search = Search(request.GET)
    context = {
        'form': form,
        'form_search':form_search
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
    form_search = Search(request.GET)
    context = {
        'form_search':form_search
    }
    return render(request, 'create_post.html', context)
def post_like_mm(request, post_id):
    posts_displayed_list = Post.objects.order_by('-post_data')[:3]
    posts_list = Post.objects.all()
    context = {
        "post_list":posts_list,
        "post_displayed_list":posts_displayed_list,
    }
    post = get_object_or_404(Post, pk = post_id)
    current_user = request.user
    post_like_list = User.objects.filter(users_post_like = post_id)
    if current_user in post_like_list:
        try:
            post.post_like -= 1
            post.post_like_list.remove(request.user)
        except Exception as identifier:
            return redirect('main-menu')
    else:
        try:
            post.post_like += 1
            post.post_like_list.add(request.user)
        except Exception as identifier:
            return redirect('main-menu')
    post.save()
    return redirect('main-menu')
def post_like_dialog(request, post_id):
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
    post = get_object_or_404(Post, pk = post_id)
    current_user = request.user
    post_like_list = User.objects.filter(users_post_like = post_id)
    if current_user in post_like_list:
        try:
            post.post_like -= 1
            post.post_like_list.remove(request.user)
        except Exception as identifier:
            return redirect('/post/'+str(post_id))
    else:
        try:
            post.post_like += 1
            post.post_like_list.add(request.user)
        except Exception as identifier:
            return redirect('/post/'+str(post_id))
    post.save()
    return redirect('/post/'+str(post_id))
def comment_like(request, post_id, comment_id):
    try:
        post = Post.objects.get(pk = post_id)
        comment = Comment.objects.get(pk = comment_id)
    except Post.DoesNotExist as identifier:
        return HttpResponse('None comments now.')
    comments_list = Comment.objects.filter(post = post)
    form = AddNewComment(request.POST)
    context = {
        "comment_list":comments_list,
        "post": post,
        'form': form,
    }
    current_user = request.user
    comment_like_list = User.objects.filter(users_comment_like = comment_id)
    if current_user in comment_like_list:
        try:
            comment.comment_like -= 1
            comment.comment_like_list.remove(request.user)
        except Exception as identifier:
            return redirect('/post/'+str(post_id))
    else:
        try:
            comment.comment_like += 1
            comment.comment_like_list.add(request.user)
        except Exception as identifier:
            return redirect('/post/'+str(post_id))
    comment.save()
    return redirect('/post/'+str(post_id))
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
        if new_comment.comment_text:
            new_comment.save()
        return redirect('/post/'+str(post_id))
class Register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'forum/registration.html'
def post_all(request):
    form_search = Search(request.GET)
    posts_list = Post.objects.order_by('-post_data')
    context = {
        'form_search':form_search,
        "post_list":posts_list,
    }
    return render(request, 'forum/post_all.html', context)
def search(request):
    form_search = Search(request.GET)
    text = form_search.data["search_text"]
    text = '123'
    post_list = Post.objects.filter(post_name__icontains = text)
    context = {
        'form_search': form_search,
        'post_list':post_list
    }
    return render(request, 'forum/post_all.html', context)
class SearchResult(generic.ListView):
    template_name = 'forum/post_all.html'
    model = Post
    def get_queryset(self):
        query = self.request.GET.get('search')
        queryset = Post.objects.filter(Q(post_name__icontains = query) | Q(post_text__icontains = query))
        return queryset