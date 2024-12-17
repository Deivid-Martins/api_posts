from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Post
from .serializers import PostSerializer, PostUpdateSerializer

import json
    
@api_view(['DELETE', 'PUT'])
def put_delete_posts(request, id):
    if request.method == 'PUT':
        try:
            post = Post.objects.get(id=id)
            serializer = PostUpdateSerializer(post, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        try:
            post = Post.objects.get(id=id)
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET', 'POST'])
def get_post_posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)