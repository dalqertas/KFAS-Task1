from rest_framework import serializers
django.contrib.auth.models import User
from .models import Authors, Books


class AuthorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model= Authors
        fields = '__all__'

class BooksListSerializer(serializers.ModelSerializer):
    class Meta:
        model= Books
        fields = '__all__'

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Books
        fields= ["title","color","author"]

class AuthorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Authors
        fields = ["first_name","last_name"]

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields =['username','password']

    def create(self,validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user = User(username=username,password=password)
        user.set_password(password)
        user.save()
        return validated_data
