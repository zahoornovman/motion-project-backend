from rest_framework import serializers
from post.models import Post
from user_profile.models import Profile

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.user.username')
    class Meta:
        model = Post
        fields = ('id', 'content', 'author', 'external_link', 'created_time', 'updated_time', 'images', 'reposted_post')
