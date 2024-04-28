from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter() 

router.register('bookcategory', views.BookCategoryViewset)
router.register('book', views.BookViewset)
router.register('borrower', views.BorrowerViewset)
router.register('wishlist', views.WishlistViewset)


urlpatterns = [
    path('', include(router.urls)),
]