from rest_framework.test import APITestCase
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group
from ..models import Book, Genre, Author


class TestLoaderUser(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user1',
            password='testpassword'
        )
        Token.objects.create(user=self.user)

        # create test genres
        self.genre1 = Genre.objects.create(name="genre1")
        self.genre2 = Genre.objects.create(name="genre2")

        # create test authors
        self.author1 = Author.objects.create(
            name="Gavin",
            surname="Belson"
        )
        self.author2 = Author.objects.create(
            name="Peter",
            surname="Gregory"
        )

        # create some books
        self.book1 = Book.objects.create(
            title="Nucleus: The core of Hooli",
            pages=123,
            release_date='2020-04-03',
            genre=self.genre1
        )
        self.book1.authors.set([self.author1])
        self.book2 = Book.objects.create(
            title="Raviga: Venture Capital with an edge",
            pages=434,
            release_date='2020-02-02',
            genre=self.genre2
        )
        self.book2.authors.set([self.author2])
        super().setUp()


class TestLoaderLibrarian(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user_librarian',
            password='testpassword'
        )
        
        Token.objects.create(user=self.user)

        librarian_group, created = Group.objects.get_or_create(name='librarian')
        librarian_group.user_set.add(self.user)

         # create test genres
        self.genre3 = Genre.objects.create(name="genre3")
        self.genre4 = Genre.objects.create(name="genre4")

        # create test authors
        self.author5 = Author.objects.create(
            name="Ben",
            surname="Thomson"
        )
        self.author6 = Author.objects.create(
            name="Nathan",
            surname="Siguey"
        )
        self.author7 = Author.objects.create(
            name="Peter",
            surname="Theil"
        )

        # create a book object
        self.book7 = Book.objects.create(
            title="Zero to One by Peter Theil",
            pages=111,
            release_date='2015-01-01',
            genre=self.genre3
        )
        self.book7.authors.set([self.author7])

        super().setUp()
