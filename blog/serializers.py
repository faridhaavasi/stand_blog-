from rest_framework import serializers

class listpost_serializer(serializers.Serializer):
    other = serializers.CharField(max_length=50)
    title = serializers.CharField(max_length=50)


