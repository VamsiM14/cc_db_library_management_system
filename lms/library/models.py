from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(default='no.email@given.com')
    phone = models.CharField(max_length=20, default='+91 98765 43210')
    faebook_username = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='author_profile_pictures', blank=True, null=True)   

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    pages = models.PositiveIntegerField()
    release_date = models.DateField()
    authors = models.ManyToManyField(Author, related_name='books')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
