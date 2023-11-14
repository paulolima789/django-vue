from django.shortcuts import render,get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


# Create your views here.

class BlogListView(APIView):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()[0:4] #[0:4] isso e a paginação
        serializers = PostSerializer(posts, many=True)
        return Response(serializers.data)

class PostDetailView(APIView):
        def get(self, request, *args, **kwargs):
            post = get_list_or_404(Post, slug=post_slug)
            serializers = PostSerializer(post)
            return Response(serializers.data)
        

