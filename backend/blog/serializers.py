#converte Models em JSON para API
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'thumbnail', 'content', 'slug', 'published', 'author','status')
