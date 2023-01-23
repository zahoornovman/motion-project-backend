from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.user.username')
    reposted_post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), required=False)

    class Meta:
        model = Post
        fields = ('id', 'content', 'author', 'external_link', 'created_time', 'updated_time', 'images', 'reposted_post')
        read_only_fields = ['id', 'created_time', 'updated_time']
