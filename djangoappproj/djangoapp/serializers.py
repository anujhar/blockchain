from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book

class BookSerializer(serializers.HyperlinkedModelSerializer):
        name = serializers.JSONField()
        author = serializers.JSONField()
        owner = serializers.ReadOnlyField(source='owner.username')

        class Meta:
        	model = Book
        	fields = ['name', 'author','owner']


class UserSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'book']
