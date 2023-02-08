from django.contrib import admin
from .models import Author, Genre, Book

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
