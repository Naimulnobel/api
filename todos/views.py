from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Todo
from .serializers import *

class ListTodo(generics.ListAPIView):
    queryset= Todo.objects.all()
    serializer_class= TodoSerializer

class DetailsTodo(generics.RetrieveAPIView):
    queryset= Todo.objects.all()
    serializer_class= TodoSerializer
    