from django.db import models

from posts.models import Post


class Comment(models.Model):
    text = models.TextField(blank=False) #нельзя отправлять пустой комментарий
    date_of_create = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=32)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date_of_create', )