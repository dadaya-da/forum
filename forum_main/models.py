from django.db import models

# Create your models here.
class Post(models.Model):
    post_name = models.CharField(max_length=20)
    post_text = models.CharField(max_length=200)
    post_data = models.DateTimeField('date posted')
    post_like = models.IntegerField(default=0)
    def __str__(self):
        return self.post_text

class Comment(models.Model):
    comment_text = models.CharField(max_length=200)
    comment_data = models.DateTimeField('date posted')
    comment_like = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment_text