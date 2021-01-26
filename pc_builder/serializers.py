from rest_framework import serializers
from .models import userinfos

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = userinfos
        fields = '__all__'
    