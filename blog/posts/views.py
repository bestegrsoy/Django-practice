# from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tag, Author, Post
from .serializer import TagSerializer, AuthorSerializer, PostSerializer
from rest_framework import generics
from rest_framework import viewsets
# from django.shortcuts import get_object_or_404

class AuthorView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class TagView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class AuthorViewSet(viewsets.ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# Yukarıda main ve detail olarak yaptığımız
# işlemleri tek classda yapmamıza olanak tanır.

#######

# class AuthorView(APIView):
# 
#     def get(self, request):
#         
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data)
#     
#     def post(self,requst):
#         serializer = AuthorSerializer(data=requst.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
# 
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TagView(APIView):
#     
#     def get(self, request):
#         
#         tags = Tag.objects.all()
#         serializer = TagSerializer(tags, many=True)
#         return Response(serializer.data)
#     
#     def post(self, request):
#         serializer = TagSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     
# class PostView(APIView):
# 
#     def get(self, request):
# 
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#     
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PostDetailView(APIView):
# 
#     def get(self, request, id):
#         post = get_object_or_404(Post, id=id)
# 
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#     
#     def put(self, request, id):
#         post = get_object_or_404(Post, id=id)
# 
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     
#     def patch(self, request, id):
#         post = get_object_or_404(Post, id=id)
# 
#         serializer = PostSerializer(post, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 
#     def delete(self, request, id):
#         post = get_object_or_404(Post, id=id)
# 
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)