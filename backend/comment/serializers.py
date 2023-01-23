from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.user.username')
    class Meta:
        model = Comment
        fields = ['id', 'content', 'post', 'author', 'created_time', 'updated_time']
        read_only_fields = ['id', 'created_time', 'updated_time']