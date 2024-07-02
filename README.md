# Django REST Framework Learning Repository

Welcome to my Django REST Framework (DRF) learning repository! This project is a showcase of my journey in learning and experimenting with Django REST Framework to build robust and scalable APIs.


## Introduction

This repository contains code and examples that demonstrate my understanding and application of Django REST Framework. The project includes various features such as user authentication, CRUD operations, and integration with a front-end client.

## Features

- **User Authentication**: Implemented token-based authentication.
- **CRUD Operations**: Basic Create, Read, Update, and Delete operations for various models.
- **Serialization**: Custom serializers to control the output of API responses.
- **Permissions and Throttling**: Configured permissions and request rate limiting.
- **Pagination**: Implemented pagination for large datasets.
- **Filtering and Search**: Added filtering and search capabilities to the API endpoints.

## Installation

To get started with this project, follow the instructions below:

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/django-rest-framework-learning.git
    cd django-rest-framework-learning
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Start the development server:**

    ```sh
    python manage.py runserver
    ```

## Usage

Once the server is running, you can access the API at `http://127.0.0.1:8000/api/`. You can also access the Django admin interface at `http://127.0.0.1:8000/admin/`.

## API Endpoints

Here are some of the key API endpoints available in this project:

- **User Registration and Authentication:**
  - `POST /api/auth/register/` - Register a new user.
  - `POST /api/auth/login/` - Authenticate a user and get a token.

- **CRUD Operations:**
  - `GET /api/items/` - List all items.
  - `POST /api/items/` - Create a new item.
  - `GET /api/items/{id}/` - Retrieve a specific item by ID.
  - `PUT /api/items/{id}/` - Update an existing item by ID.
  - `DELETE /api/items/{id}/` - Delete an item by ID.

- **Filtering and Search:**
  - `GET /api/items/?search=keyword` - Search items by keyword.
  - `GET /api/items/?filter=value` - Filter items by a specific field.

## Testing

To run tests, use the following command:

```sh
python manage.py test
