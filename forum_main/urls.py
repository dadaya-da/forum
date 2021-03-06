from django.urls import path
from . import views
from .views import Register, SearchResult
urlpatterns = [
    path("", views.main_menu, name = 'main-menu'),
    path("post/<int:post_id>/", views.dialog, name = 'dialog'),
    path("creation/", views.creation, name = 'creation'),
    path("like/<int:post_id>", views.post_like_mm, name = 'like'),
    path("comment/<int:post_id>", views.comment, name = 'comment'),
    path("like_post/<int:post_id>/", views.post_like_dialog, name = 'post_like_dialog'),
    path("like_comment/<int:post_id>/<int:comment_id>", views.comment_like, name = 'like_comment'),
    path("registration/", Register.as_view(), name = 'registration'),
    path("search/", SearchResult.as_view(), name = 'search'),
    path("post_all/", views.post_all, name = 'post_all'),
]