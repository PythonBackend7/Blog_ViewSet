from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    list_display_link = ('id','name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    list_display_link = ('id','name',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','name','job')
    list_display_link = ('id','name','job')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','author','category')
    list_display_link = ('id','title','content','author','category')
    list_filter = ('author','category')
    search_fields = ('title',)
    filter_horizontal = ('tags',)