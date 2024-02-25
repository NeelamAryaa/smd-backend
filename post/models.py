import datetime
from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class BasePostModel(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500) 
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class PostAnalytics(BasePostModel):
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    shares = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"Analytics for {self.likes}"
    

# class Post(BaseModel):
#     title = models.CharField(max_length=255)
#     description = models.TextField(max_length=500) 
#     content = models.TextField()
#     creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
#     analytics = models.ForeignKey(PostAnalytics, on_delete=models.CASCADE, related_name="analytics")
    
#     def __str__(self):
#         return self.title
    



class UpcomingPost(BasePostModel):
    DRAFT = 'draft'
    SCHEDULE = 'schedule'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (SCHEDULE, 'Schedule'),
    ]
   
    draft_or_schedule = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
    )

    date_field = models.DateField(default=datetime.date.today)
    time_field = models.TimeField(default=datetime.time)
    
    # set_time = models.DateField(default=timezone.now)


# class Comment(BaseModel):
#     user = models.ForeignKey(User, on_delete=models.CASCADE) 
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#     comment = models.TextField()

#     def __str__(self):
#         return f"Comment '{self.comment}' by {self.user.username} on '{self.post.title}'"
    

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

#         # Update the average rating and number of ratings for the associated course
#         post = self.post
#         comments = Comment.objects.filter(post=post).count()
#         post.comment_count = comments
#         post.save()



