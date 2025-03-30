This module provides endpoints for managing users in the system, including creating, reading, updating, and deleting users. Below are the details of each available endpoint.

### Endpoints

### 1. List Users

**GET** `/users/`

Returns a list of users with pagination support.

- **Query Parameters**:
- `limit` (int, optional): The maximum number of users to return. Default value: `10`.
- `offset` (int, optional): The number of users to ignore before returning results. Default value: `0`.

- **Response**:
- `200 OK`: A list of users in the format `{ "users": [...] }`.


### 2. Create User

**POST** `/users/`

Creates a new user in the system.

- **Request Body**:
- `UserSchema`: Schema containing `email`, `username` and `password` of the new user.

- **Response**:
- `201 Created`: The newly created user in `UserPublic` format.

- **Errors**:
- `400 Bad Request`: If the `username` or `email` already exists.

### 3. Get User by ID

**GET** `/users/{user_id}`

Returns information for a specific user based on their ID.

- **Path Parameters**:
- `user_id` (int): The user ID to retrieve.

- **Response**:
- `200 OK`: The user details in `UserPublic` format.

- **Errors**:
- `404 Not Found`: If the user with the given `user_id` is not found.

### 4. Update User

**PUT** `/users/{user_id}`

Updates the information of an existing user.

- **Path Parameters**:
- `user_id` (int): The ID of the user to be updated.

- **Request Body**:
- `UserSchema`: Schema containing the new values ​​for `email`, `username`, and `password`.

- **Response**:
- `200 OK`: The updated user details in `UserPublic` format.

- **Errors**:
- `404 Not Found`: If the user with the given `user_id` is not found.
- `401 Unauthorized`: If the authenticated user does not have permission to update the user.

### 5. Delete User

**DELETE** `/users/{user_id}`

Deletes a specific user from the system.

- **Path Parameters**:
- `user_id` (int): The ID of the user to be deleted.

- **Response**:
- `200 OK`: Confirmation message of the deletion in the format `{ "message": "User deleted" }`.

- **Errors**:
- `404 Not Found`: If the user with the given `user_id` is not found.
- `401 Unauthorized`: If the authenticated user does not have permission to delete the user.

**WARNING ⚠️**

> The token expiration time must be 30 minutes, the algorithm used |must be HS256 and the subject must be the email

<br><br>
