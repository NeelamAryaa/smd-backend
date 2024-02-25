

# Create your views here.
# views.py
from rest_framework import generics, status
from rest_framework.response import Response
from .models import  PostAnalytics, UpcomingPost
from .serializers import  PostAnalyticsSerializer, UpcomingPostSerializer
from rest_framework.pagination import PageNumberPagination

# class PostListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer



# class PostAnalyticsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = PostAnalytics.objects.all()
#     serializer_class = PostAnalyticsSerializer


# class UpcomingPostListCreateAPIView(generics.ListCreateAPIView):
#     queryset = UpcomingPost.objects.all()
#     serializer_class = UpcomingPostSerializer

# class UpcomingPostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UpcomingPost.objects.all()
#     serializer_class = UpcomingPostSerializer




class PostAnalyticsListAPIView(generics.ListAPIView):
    queryset = PostAnalytics.objects.all().order_by('-likes')
    serializer_class = PostAnalyticsSerializer 
    # pagination_class = PageNumberPagination



class DraftScheduledPostListView(generics.ListAPIView):
    
    serializer_class = UpcomingPostSerializer

    def get_queryset(self):
        draft_or_schedule = self.kwargs['status']  # assuming you pass 'draft' or 'schedule' in the URL
        return UpcomingPost.objects.filter(draft_or_schedule=draft_or_schedule).order_by('-created_at')
    


class CreateUpcomingPostView(generics.CreateAPIView):
    serializer_class = UpcomingPostSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)