from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from ..models import Book, Genre, Author
from . import TestLoader
# Create your tests here.

class ListAllBooksTestCase(TestLoader):
    authentication_classes = (TokenAuthentication,)
    # create a test user
    # user = User.objects.create_user(
    #     username='test_user6',
    #     password='testpassword'
    # )
    # token = Token.objects.create(user=user)
    # print('******'*10)
    # print(f'token: {token}')
    # print('******'*10)

    # def setUp(self):
    #     # create a test user
    #     # self.user = User.objects.create_user(
    #     #     username='test_user1',
    #     #     password='testpassword'
    #     # )
    #     # Token.objects.create(user=self.user)
    #     # create test genres
    #     self.genre1 = Genre.objects.create(name="genre1")
    #     self.genre2 = Genre.objects.create(name="genre2")

    #     # create test authors
    #     self.author1 = Author.objects.create(
    #         name="Gavin",
    #         surname="Belson"
    #     )
    #     self.author2 = Author.objects.create(
    #         name="Peter",
    #         surname="Gregory"
    #     )

    #     # create some books
    #     self.book1 = Book.objects.create(
    #         title="Nucleus: The core of Hooli",
    #         pages=123,
    #         release_date='2020-04-03',
    #         genre=self.genre1
    #     )
    #     self.book1.authors.set([self.author1])
    #     self.book2 = Book.objects.create(
    #         title="Raviga: Venture Capital with an edge",
    #         pages=434,
    #         release_date='2020-02-02',
    #         genre=self.genre2
    #     )
    #     self.book2.authors.set([self.author2])


    def test_list_all_books(self):
        # book list endpoint
        # token = '89de43fe7c73294f41b20cd3e7a580819be1201c'
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        response = self.client.get("/api/books/")
        # print('******'*10)
        # print(f'response.data: {response.data}')
        # print('******'*10)

        # test if the endpoint returns a response with a status code of 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # test if the endpoint returns a list of books
        # self.assertEqual(type(response.data), list)
        # print(response.data)
        self.assertEqual(len(response.data), 2)