from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView

from comment.serializers import CommentSerializer
from comment.models import Comment
from post.models import Post


class ListCreateCommentView(ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        queryset = Comment.objects.filter(post=post_id).order_by('-created_time')
        return queryset

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)
