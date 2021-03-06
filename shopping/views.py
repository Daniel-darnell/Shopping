from django.shortcuts import render
from rest_framework import Viewsets
from .models import ShoppingItem
from .serializers import ShoppingItemSerializer

# Create your views here.
class ShoppingItemViewSet(viewsets.ModelViewSet):
    serializer_class = ShoppingItemSerializer
    queryset = ShoppingItem.objects.all()
    