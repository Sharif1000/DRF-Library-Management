from rest_framework import serializers
from . import models

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserAccount
        fields = '__all__'
        