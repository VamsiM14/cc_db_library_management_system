from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.urls import reverse
from ..models import Book, Genre, Author
from . import TestLoaderUser, TestLoaderLibrarian


authentication_classes = (TokenAuthentication,)


class ListAllBooksTestCase(TestLoaderUser):
    
    def test_list_all_books(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        # book list endpoint
        response = self.client.get(reverse('book-list'))
        
        # test if the endpoint returns a response with a status code of 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # test if the endpoint returns a correct number of books
        self.assertEqual(len(response.data), 2)


class ListAllAuthorTestCase(TestLoaderUser):

    def test_list_all_authors(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        # author list endpoint
        response = self.client.get(reverse('author-list'))

        # test if the endpoint returns a response with a status code of 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # test if the endpoint returns a correct number of books
        self.assertEqual(len(response.data), 2)


class FilterBooksTestCase(TestLoaderUser):

    def test_filter_books(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        # filter books endpoint
        response = self.client.get(reverse('book-list') + "?title=Nucleus")

        # test if the endpoint returns a response with a status code of 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # test the count of objects given by response
        self.assertEqual(len(response.data), 1)

        # test if filter works as expected(case-insensitive, exact/partial match)
        response = self.client.get(reverse('book-list') + "?title=nucleus")
        self.assertEqual(len(response.data), 1)

        response = self.client.get(reverse('book-list') + "?title=nucl")
        self.assertEqual(len(response.data), 1)

        # test filters on release_date is working as expected (exact match, earlier/later than and range)
        response = self.client.get(reverse('book-list') + "?release_date_after=2019-09-18&release_date_before=2020-02-28")
        self.assertEqual(len(response.data), 1)

        response = self.client.get(reverse('book-list') + "?release_date_after=2019-01-01")
        self.assertEqual(len(response.data), 2)

        # test if the number of pages filters work as expected (range)
        response = self.client.get(reverse('book-list') + "?pages_min=200")
        self.assertEqual(len(response.data), 1)

        response = self.client.get(reverse('book-list') + "?pages_max=200")
        self.assertEqual(len(response.data), 1)

        response = self.client.get(reverse('book-list') + "?pages_min=10&pages_max=200")
        self.assertEqual(len(response.data), 1)

        # test filters on book with author_id (exact), by name, surname or both
        response = self.client.get(reverse('book-list') + "?author=1")
        self.assertEqual(len(response.data), 1)

        response = self.client.get(reverse('book-list') + "?author_name=Gavin")
        self.assertEqual(len(response.data), 1)

        response = self.client.get(reverse('book-list') + "?author_surname=Gregory")
        self.assertEqual(len(response.data), 1)

        response = self.client.get(reverse('book-list') + "?author_name=Gavin&author_surname=Belson")
        self.assertEqual(len(response.data), 1)


class FilterAuthorsTestCase(TestLoaderUser):
    def test_filter_authors(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        # test filters on author (case-insensitive, exact & partial match)
        response = self.client.get(reverse('author-list') + "?name=gavin")
        self.assertEqual(len(response.data), 1)


class LibrarianCRUDTestCase(TestLoaderLibrarian):
    def test_crud_ops_librarian(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        
        # add book
        book = {
            'title': 'The Hooli',
            'pages': 578,
            'release_date': '2018-01-02',
            'author_id': 1
        }
        response = self.client.post(reverse('book-list'), data=book)
        self.assertEqual(response.status_code, status.HTTP_200_OK)