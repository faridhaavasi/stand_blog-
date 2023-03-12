from rest_framework import serializers
from . models import Post
from django.contrib.auth.models import User
class listpost_serializer(serializers.Serializer):
    other = serializers.CharField(max_length=50)
    title = serializers.CharField(max_length=50)


class detailpost_serializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    other = serializers.CharField(max_length=50)
    title = serializers.CharField(max_length=50)
    category = serializers.CharField(max_length=20)
    body = serializers.CharField()
'''
    def create(self, validated_data):
        return Post.objects.create(title=validated_data['title'], other=validated_data['other'], category=validated_data['category'], body=validated_data['body'])
'''


class addedserializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['img', 'created', 'updated', 'status']


class update_serializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body', 'status']