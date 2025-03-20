from rest_framework import serializers
from .models import Legend


class LegendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legend
        fields = ['id', 'name', 'image_url', 'class_type']
