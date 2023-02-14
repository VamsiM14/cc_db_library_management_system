from django.test import TestCase
from rest_framework.test import APIClient
from .models import Book, Genre, Author
# Create your tests here.

class ListAllBooksTestCase(TestCase):
    def test_setup(self):
        genre1 = Genre.objects.create(name="Genre1")
        genre2 = Genre.objects.create(name="Genre2")
        
        author1 = Author.objects.create(name="John")
        author2 = Author.objects.create(name="Maria")

        book1 = Book.objects.create(
            title="Book1",
            pages=100,
            release_date="2023-01-01",
            genre=genre1
        )
        book1.authors.set([author1])
        book1.save()

        book2 = Book.objects.create(
            title="Book2",
            pages=200,
            release_date="2023-02-01",
            genre=genre2
        )
        book2.authors.set([author2])
        book2.save()

    def test_list_all_books(self):
        client = APIClient()
        response = client.get("/api/books/")
        # test if the endpoint returns a response with a status code of 200
        self.assertEqual(response.status_code, 200)
        
        # test if the endpoint returns a list of books
        # self.assertEqual(type(response.data), list)
        print(response.data)
        self.assertEqual(len(response.data), 2)

        # test if the informaiton in each book is correct and complete
        for book in response.data:
            self.assertIn("title", book)
            self.assertIn("pages", book)
            self.assertIn("release_date", book)
            self.assertIn("author", book)
            self.assertIn("genre", book)