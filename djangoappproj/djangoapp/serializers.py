from rest_framework import serializers

from .models import Book

class BookSerializer(serializers.HyperlinkedModelSerializer):
	name = serializers.JSONField()
	author = serializers.JSONField()    
	class Meta:
        	model = Book
        	fields = ('name', 'author')
