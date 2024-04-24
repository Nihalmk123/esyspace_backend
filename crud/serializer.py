from django.db.models import fields
from rest_framework import serializers
from crud.models import DetailsModel
from crud.models import CreateTaxModel
from django.contrib.auth.models import User

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=DetailsModel
        fields="__all__"

class CreateTaxModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateTaxModel
        fields = ('id', 'tax_name', 'tax_amount')


class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()