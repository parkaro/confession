from rest_framework import serializers
from .models import Confession, Comment


class ConfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Confession
        fields = ['id', 'author', 'description', 'date']
