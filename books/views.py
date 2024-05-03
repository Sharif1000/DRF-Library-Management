from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from . import models
from . import serializers

# Create your views here.

class BookCategoryViewset(viewsets.ModelViewSet):
    queryset = models.BookCategory.objects.all()
    serializer_class = serializers.BookCategorySerializer
    
class BookViewset(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['genre__name']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(genre_id=category_id)
        return queryset
    
class BorrowerViewset(viewsets.ModelViewSet):
    queryset = models.Borrower.objects.all()
    serializer_class = serializers.BorrowerSerializer

    
class WishlistViewset(viewsets.ModelViewSet):
    queryset = models.Wishlist.objects.all()
    serializer_class = serializers.WishlistSerializer