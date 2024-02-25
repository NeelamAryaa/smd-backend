import datetime
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PostAnalytics, UpcomingPost

# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = '__all__'
#         # fields = ['uid', 'title', 'description', 'created_at', 'content', 'creator']


# class PostAnalyticsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PostAnalytics
#         fields = '__all__'
#         # fields = [ 'post', 'likes', 'shares', 'comments']


        
class UpcomingPostSerializer(serializers.ModelSerializer):
    creator = serializers.SerializerMethodField()
    class Meta:
        model = UpcomingPost
        fields = '__all__'
        
    def get_creator(self, obj):
        return obj.creator.username
    
    def validate(self, data):
        title = data.get('title')
        description = data.get('description')
        content = data.get('content')
        draft_or_schedule = data.get('draft_or_schedule')
        date_field = data.get('date_field')
       

        errors = {}

        # Validate title
        if not title:
            errors['title'] = 'Title cannot be empty'

        # Validate description
        if not description:
            errors['description'] = 'Description cannot be empty'

        # Validate content
        if not content:
            errors['content'] = 'Content cannot be empty'

        # Validate draft_or_schedule
        if draft_or_schedule not in [UpcomingPost.DRAFT, UpcomingPost.SCHEDULE]:
            errors['draft_or_schedule'] = 'Invalid value for draft_or_schedule'

        # Validate date_field
        # if date_field < datetime.date.today():
        #     errors['date_field'] = 'Date cannot be in the past'

        # You can add further validation for time_field if needed

        if errors:
            raise serializers.ValidationError(errors)

        return data

    def create(self, validated_data):
        # Get the user 'Neelam' or create if it doesn't exist
        neelam_user, _ = User.objects.get_or_create(username='neelam')

        # Set the creator field to Neelam
        validated_data['creator'] = neelam_user

        # Create and return the UpcomingPost instance
        return super().create(validated_data)

# ======================================================
class PostAnalyticsSerializer(serializers.ModelSerializer):
    creator = serializers.SerializerMethodField()
    class Meta:
        model = PostAnalytics
        fields = '__all__'

    def get_creator(self, obj):
        return obj.creator.username

# no need now
# class PostSerializer(serializers.ModelSerializer):
#     analytics = PostAnalyticsSerializer(read_only=True)

#     class Meta:
#         model = Post
#         fields = '__all__'
