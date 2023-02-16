from django.contrib import admin
from .models import Category, Post, Comment

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    pass

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    pass

@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    pass

