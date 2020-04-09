from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    owner = models.ForeignKey('auth.User',null=True,related_name='book',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)


    def __str__(self):
        return self.name


