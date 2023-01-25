from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework import filters, permissions, status
from rest_framework.response import Response

from post.models import Post
from post.serializers import PostSerializer
from user_profile.models import Profile


class ListCreatePostView(ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_time')
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ListUserPostView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return self.queryset.filter(author__id=user_id).order_by('-created_time')


class ListFriendPostView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        friends = user.friends.all()
        return self.queryset.filter(author__in=friends)


class ListFollowedUserPostView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        following = profile.user_is_following.all()
        following_posts = Post.objects.filter(author__in=following).order_by('-created_time')
        return following_posts


class ListLikePostView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user_id = self.kwargs['user_id']

        return self.queryset.filter(author__id=user_id).order_by('-created_time')
    # Line for Posts Liked is missing



class ToggleUpdateLikePostView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):

        post_id = kwargs['post_id']
        post = Post.objects.get(id=post_id)
        user_profile = Profile.objects.get(custom_django_user=request.user)

        if user_profile in post.liked_by_user.all():
            post.liked_by_user.remove(user_profile)
        else:
            post.liked_by_user.add(user_profile)
        post.save()
        # serializer = self.get_serializer(post)
        return Response(status=status.HTTP_200_OK)


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class RetrieveUpdateDeletePostView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthor, permissions.IsAdminUser)
