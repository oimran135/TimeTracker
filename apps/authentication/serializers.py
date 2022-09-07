from rest_framework import serializers
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from .models import (
    User,
)


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 68, min_length= 8, write_only = True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'name',]

    def create(self, validated_data):
         return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(
        max_length=68, min_length=8, write_only=True)
    username = serializers.CharField(
        max_length=150, read_only=True)

    tokens = serializers.SerializerMethodField()
    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])
        return user.tokens()['access']

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'username', "tokens"]

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('The email or password is incorrect')

        return{
            'id':user.id,
            'email':user.email,
            'username':user.username,
            'tokens':user.tokens
        }


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('email', 'username', 'name',)


class PasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 68, min_length= 8, write_only = False)
    new_password = serializers.CharField(max_length = 68, min_length= 8, write_only = True)
    
    class Meta:
        model = User
        fields = ('password', 'new_password',)