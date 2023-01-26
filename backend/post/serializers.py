from rest_framework import serializers

from post.models import Post
from user_profile.serializers import ProfileSerializer


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.user.username')
    reposted_post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), required=False)
    liked_by_user = ProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'content', 'author', 'external_link', 'created_time', 'updated_time', 'images', 'reposted_post',
                  'liked_by_user')
        read_only_fields = ['id', 'created_time', 'updated_time']
