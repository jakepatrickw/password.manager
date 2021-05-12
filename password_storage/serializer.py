from rest_framework import serializers
from . models import UsernamePasswordService


class PassWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsernamePasswordService
        fields = ['id', 'service', 'user_name', 'password']


class UpdatePassWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsernamePasswordService
        fields = ['id', 'service', 'user_name', 'password']
    service = serializers.CharField(required=False)
    user_name = serializers.CharField(required=False)
    password = serializers.CharField(required=False)