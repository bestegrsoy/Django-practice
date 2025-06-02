from rest_framework import serializers
from .models import Tag, Author, Post
# from django.shortcuts import get_object_or_404

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

# class TagSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=50)
# 
#     def create(self, validated_data):
#         return Tag.objects.create(**validated_data)

# class AuthorSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100)
#     surname = serializers.CharField(max_length=100)
#     age = serializers.IntegerField()
#     email = serializers.EmailField()
# 
#     def create(self, validated_data):
#         return Author.objects.create(**validated_data)

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=50)
#     content = serializers.CharField()
#     created = serializers.DateTimeField(read_only=True)
#     updated = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField()
# 
#     author = AuthorSerializer(read_only=True)
#     tag = TagSerializer(many=True, required=False, read_only=True)
# 
#     author_id =serializers.IntegerField(write_only=True)
#     tag_ids = serializers.ListField(
#         child=serializers.IntegerField(),
#         write_only=True,
#         required=False
#     )
# 
#     def create(self, validated_data):
#         author_id = validated_data.pop('author_id')
#         tag_ids = validated_data.pop('tag_ids', [])
# 
#         author = get_object_or_404(Author, id=author_id)
#         post = Post.objects.create(author=author, **validated_data)
# 
#         if tag_ids:
#             tags = Tag.objects.filter(id__in=tag_ids)
#             post.tag.set(tags)
# 
#         return post
#     
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.is_published = validated_data.get('is_published', instance.is_published)
# 
#         author_id = validated_data.get('author_id')
#         if author_id:
#             author = get_object_or_404(Author, id=author_id)
#             instance.author = author
# 
#         tag_ids = validated_data.get('tag_ids', [])
#         if tag_ids:
#             instance.tag.clear()
#             tag = Tag.objects.filter(id__in=tag_ids)
#             instance.tag.set(tag)
# 
#         instance.save()
#         return instance
# instance güncellenmek istenen mevcut bir veri tabanındaki kaydı ifade eder. 