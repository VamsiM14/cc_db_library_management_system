from django.shortcuts import render
from rest_framework import viewsets
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookFilter, AuthorFilter
from rest_framework.permissions import IsAuthenticated
from .permisssions import IsLibrarian
from rest_framework import generics

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
    permission_class = [IsAuthenticated, IsLibrarian]

    def perform_destroy(self, instance):
        '''
        Removes Authors who do not have books in the library
        '''
        for author in instance.authors.all():
            if not author.book_set.exists():
                author.delete()
        instance.delete()

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AuthorFilter
    

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer