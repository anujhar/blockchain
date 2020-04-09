from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('book/', views.book_list),
    path('book/<int:pk>/', views.book_details),
]

urlpatterns = format_suffix_patterns(urlpatterns)
