from django.shortcuts import render
from rest_framework import viewsets
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookFilter, AuthorFilter
from rest_framework.permissions import IsAuthenticated
from .permissions import IsLibrarian
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

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
            if not author.book_authors.exists():
                author.delete()
        instance.delete()

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AuthorFilter

    def perform_destroy(self, instance):
        '''
        Removes an Author only if they don't have any books in library 
        '''
        if not instance.book_authors.exists():
            instance.delete()

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


