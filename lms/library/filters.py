import django_filters
from .models import Book, Author

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    pages = django_filters.RangeFilter(field_name='pages')
    release_date = django_filters.DateFromToRangeFilter()
    author_name = django_filters.CharFilter(field_name='authors__name', lookup_expr='icontains')
    author_surname = django_filters.CharFilter(field_name='authors__surname', lookup_expr='icontains')
    author = django_filters.NumberFilter(field_name='authors__pk')

    
    class Meta:
        model = Book
        fields = ['title', 'pages', 'release_date', 'authors']


class AuthorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    surname = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = Author
        fields = ['name', 'surname', 'email']