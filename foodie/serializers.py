"""serializers - changes complexed querysets or model instances into json or xml"""

from rest_framework import serializers
from .models import FoodPlaza
from rest_framework.serializers import ModelSerializer

class foodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodPlaza
        fields = '__all__'

