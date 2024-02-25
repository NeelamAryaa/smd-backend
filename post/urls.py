from django.urls import path
from . import views

urlpatterns = [
    # path('posts/', views.PostListCreateAPIView.as_view(), name='post-list'),
    # path('posts/<uuid:pk>/', views.PostDetailAPIView.as_view(), name='post-detail'),
    path('post-analytics/', views.PostAnalyticsListAPIView.as_view(), name='post-analytics-list'),
    # path('post-analytics/<uuid:pk>/', views.PostAnalyticsDetailAPIView.as_view(), name='post-analytics-detail'),
    # path('upcoming-posts/', views.UpcomingPostListCreateAPIView.as_view(), name='upcoming-post-list'),
    path('posts/<str:status>', views.DraftScheduledPostListView.as_view(), name='draft-scheduled-post-list'),
    path('upcoming-posts/', views.CreateUpcomingPostView.as_view(), name='create-upcoming-post'),
    # path('upcoming_post/<uuid:pk>/', views.UpcomingPostDetailAPIView.as_view(), name='upcoming-post-detail'),
]