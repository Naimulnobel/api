from django.urls import path
from .views import *

urlpatterns=[
    path('<int:pk>/', DetailsTodo.as_view()),
    path('', ListTodo.as_view()),
]