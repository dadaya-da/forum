from django.urls import path
from . import views
urlpatterns = [
    # path("", views.register, name = 'register'),
    path("", views.main_menu, name = 'main-menu'),
    path("post/<int:post_id>/", views.dialog, name = 'dialog'),
    path("creation/", views.creation, name = 'creation'),
    path("like/<int:post_id>", views.like, name = 'like'),
]