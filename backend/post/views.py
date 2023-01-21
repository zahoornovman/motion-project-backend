from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from post.models import Post
from post.serializers import PostSerializer


# Create your views here.

class ListCreatePostView(ListCreateAPIView):
    queryset = Post.objects.all().order_by('created_time').reverse()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['content']

class RetrieveUpdateDeletePostView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class SearchPostView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('created_time').reverse()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['content']