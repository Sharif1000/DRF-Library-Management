from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter() 

router.register('user', views.UserAccountViewset)


urlpatterns = [
    path('', include(router.urls)),
]