# User Authentication API

This is a simple user authentication API built with Django Rest Framework.

## Endpoints

### Login

- **URL:** `/login`
- **Method:** `POST`
- **Description:** Logs in a user and returns a token and user information.
- **Request Body:**

```json
{
    "username": "example",
    "password": "example_password"
}
```

- **Success Response:**
    - **Code:** `200 OK`
    - **Content:**

```json
{
    "token": "example_token",
    "user": {
        "id": 1,
        "username": "example",
        "email": "example@example.com",
        ...
    }
}
```

- **Error Response:**
    - **Code:** `401 UNAUTHORIZED`
    - **Content:**

```json
{
    "error": "Invalid password"
}
```

### Register

- **URL:** `/register`
- **Method:** `POST`
- **Description:** Register a new user.
- **Request Body:**

```json
{
    "username": "new_user",
    "password": "new_password",
    "email": "new_user@example.com"
}

```

- **Success Response:**
    - **Code:** `200 OK`
    - **Content:**

```json
{
    "token": "new_user_token",
    "user": {
        "id": 2,
        "username": "new_user",
        "email": "new_user@example.com"
        ...
    }
}

```

- **Error Response:**
    - **Code:** `400 BAD REQUEST`
    - **Content:**

```json
{
    "field": [
        "error_message"
    ]
}
```

### Verify Authentication

- **URL:** `/verify`
- **Method:** `POST`
- **Description:** View function to verify if a user is authenticated.
- **Authentication:** Token-based or Session-based authentication required.
- **Request Body:**
- **Success Response:**
    - **Code:** `200 OK`
    - **Content:**

```json
    {
    "message": "User is authenticated",
    "user": {
        "id": 1,
        "username": "example",
        "email": "example@example.com"
        ...
    }
}
```