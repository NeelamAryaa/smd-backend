from django.contrib import admin
from .models import  PostAnalytics, BasePostModel, UpcomingPost

# Register your models here.
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display= ['title']

@admin.register(PostAnalytics)
class PostAnalyticsAdmin(admin.ModelAdmin):
    list_display= ['uid','title','likes', 'dislikes', 'shares', 'comments']

# 

@admin.register(UpcomingPost)
class UpcomingPostAdmin(admin.ModelAdmin):
    list_display= ['uid', "title", "draft_or_schedule"]


