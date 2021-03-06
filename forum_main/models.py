from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    post_user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_name = models.CharField(max_length=20)
    post_text = models.CharField(max_length=200)
    post_data = models.DateTimeField('date posted')
    post_like = models.IntegerField(default=0)
    post_like_list = models.ManyToManyField(User, related_name='users_post_like')
    def __str__(self):
        return self.post_text

class Comment(models.Model):
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    comment_data = models.DateTimeField('date posted')
    comment_like = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_like_list = models.ManyToManyField(User, related_name='users_comment_like')
    def __str__(self):
        return self.comment_text