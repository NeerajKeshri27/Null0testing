from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import foodSerializer
from .models import FoodPlaza
# Create your views here.

class FoodCrudCBV(ModelViewSet):
    queryset = FoodPlaza.objects.all()
    serializer_class = foodSerializer
    