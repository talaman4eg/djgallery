from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    title = models.CharField(max_length=1500)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_cover_photo = models.ForeignKey('Photo', on_delete=models.SET_NULL, null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s (%s)" % (self.title, self.id)


class Photo(models.Model):
    title = models.CharField(max_length=1500)
    description = models.TextField()
    photo = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_album = models.ManyToManyField(Album)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s (%s)" % (self.title, self.id)


class Comment(models.Model):
    comment = models.TextField(max_length=1500)
    user = models.ForeignKey(User, related_name="gallery_user_comment_set", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s (%s)" % (self.comment, self.id)

    class Meta:
        unique_together = [
            ['user', 'comment'],
        ]
