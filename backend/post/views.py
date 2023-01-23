from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework import filters, permissions
from rest_framework.response import Response

from post.models import Post
from post.serializers import PostSerializer
from user_profile.models import Profile


# Create your views here.

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


class ListFollowingPostView(ListAPIView):
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
        user = self.request.user
        return Post.objects.filter(likes__user=user)


class ToggleUpdateLikePostView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user
        if user in post.liked_by.all():
            post.liked_by.remove(user)
        else:
            post.liked_by.add(user)
        post.save()
        serializer = self.get_serializer(post)
        return Response(serializer.data)


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class RetrieveUpdateDeletePostView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthor, permissions.IsAdminUser)
