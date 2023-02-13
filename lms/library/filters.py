import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    number_of_pages = django_filters.RangeFilter()
    release_date = django_filters.DateFilter()
    author_name = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains')
    author_surname = django_filters.CharFilter(field_name='author__surname', lookup_expr='icontains')
    author = django_filters.NumberFilter(field_name='author__pk')

    
    class Meta:
        model = Book
        fields = ['title', 'number_of_pages', 'release_date', 'author_name', 'author_surname', 'author']