from rest_framework import serializers
from .models import Poyabzallar, Comments

class PoyabzalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poyabzallar
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'user', 'post', 'text', 'created_at', 'updated_at']
