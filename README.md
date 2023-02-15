# cc_db_library_management_system

## Library Management System API

This API provides endpoints for managing books and authors in a library. The API is built using Django REST framework (DRF).

### API Endpoints

The API has the following endpoints:

#### Books

- List all books with information: GET /books/

- Filter books: GET /books/?search=<search_term>

- Add a book: POST /books/

- Update a book: PUT /books/\<id\>/

- Remove a book: DELETE /books/\<id\>/

#### Authors

- List all authors with information: GET /authors/

- Filter authors: GET /authors/?search=<search_term>

- Add an author: POST /authors/

- Update an author: PUT /authors/\<id\>/

- Remove an author: DELETE /authors/\<id\>/

#### Requirements

- Python 3.7+

- Django 3.1+

- Django REST framework 3.11+

#### Setup

1\. Clone the repository

git clone https://github.com/VamsiM14/cc_db_library_management_system.git

2\. Change into the project directory

cd cc_db_library_management_system

3\. Install the dependencies

pip install -r requirements.txt

4\. Run the server

python manage.py runserver

#### Usage

The API can be accessed using any HTTP client like:

- Postman


#### Testing

The project includes a suite of unit tests. To run the tests:

python manage.py test

