from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.

class BookCategoryViewset(viewsets.ModelViewSet):
    queryset = models.BookCategory.objects.all()
    serializer_class = serializers.BookCategorySerializer
    
class BookViewset(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    
class BorrowerViewset(viewsets.ModelViewSet):
    queryset = models.Borrower.objects.all()
    serializer_class = serializers.BorrowerSerializer
    
class WishlistViewset(viewsets.ModelViewSet):
    queryset = models.Wishlist.objects.all()
    serializer_class = serializers.WishlistSerializer