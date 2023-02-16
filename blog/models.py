from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Category(models.Model):
    title = models.TextField(max_length=200, unique=True)
    priority = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s (%s)" % (self.title, self.id)

    class Meta:
        verbose_name_plural = "categories"


class Post(models.Model):
    title = models.CharField(max_length=1500)
    post = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    avg_rating = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s (%s)" % (self.title, self.id)

    def is_recent(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)


class PostRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together  = [
            ['user', 'post'],
        ]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    user = models.ForeignKey(User, related_name="blog_user_comment_set", on_delete=models.CASCADE)
    avg_rating = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s (%s)" % (self.comment, self.id)

class CommentRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [
            ['user', 'comment'],
        ]

