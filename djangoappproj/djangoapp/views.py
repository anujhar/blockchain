from django.shortcuts import render

# Create your views here.
from .models import Book
from .serializers import BookSerializer,UserSerializer
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions

class UserViewSet(viewsets.ReadOnlyModelViewSet):
   """
    This viewset automatically provides `list` and `detail` actions.
   """
   queryset = User.objects.all()
   serializer_class = UserSerializer

class BookListViewSet(viewsets.ViewSet):
     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

     def perform_create(self, serializer):
          serializer.save(owner=self.request.user)

     def list(self,request,format=None):
         queryset = Book.objects.all()
         serializer = BookSerializer(queryset, many=True)
         return Response(serializer.data)

     def create(self,request,format=None):
         serializer = BookSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    def retrieve(self, request, pk, format=None):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset,pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def update(self, request, pk, format=None):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset,pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk, format=None):
        queryset = Book.objects.all
        book = get_object_or_404(queryset,pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
