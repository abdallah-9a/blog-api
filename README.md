# Blog API

A robust Blog REST API built with Django Rest Framework.

## Features

- **User Management**: Registration, login/logout, profile, password change/reset, JWT authentication.
- **Posts**: Create, list, retrieve, update, delete blog posts. Image upload supported.
- **Categories & Tags**: Organize posts with categories and tags. Admin-only category management.
- **Comments**: Add, list, update, and delete comments on posts. Author-only edit/delete.
- **Role-Based Permissions**: Author, admin, and read-only access for different resources.
- **Pagination**: Custom pagination for posts, categories, and comments.
- **Media Handling**: Upload and serve images for posts and user profiles.
- **Email Support**: Password reset via email.
- **Admin Panel**: Manage all models via Django admin.
- **Secure**: Password validation, JWT token blacklisting, environment-based secrets.

## API Endpoints

## Authentication

User authentication and management are handled by a separate Auth API. This project uses endpoints cloned from my [Auth API repository](https://github.com/abdallah-9a/drf-auth-api) for all user-related functionality.

## Blog API Endpoints

| Method | Endpoint                      | Description                          | Permissions   |
| ------ | ----------------------------- | ------------------------------------ | ------------- |
| GET    | /api/posts/                   | List all published posts (paginated) | Any           |
| POST   | /api/posts/                   | Create a new post                    | Authenticated |
| GET    | /api/posts/<int:pk>/          | Retrieve post details                | Any           |
| PUT    | /api/posts/<int:pk>/          | Update post                          | Author only   |
| PATCH  | /api/posts/<int:pk>/          | Partial update                       | Author only   |
| DELETE | /api/posts/<int:pk>/          | Delete post                          | Author only   |
| GET    | /api/posts/<int:pk>/comments/ | List comments for a post             | Any           |
| POST   | /api/posts/<int:pk>/comments/ | Add a comment to a post              | Authenticated |
| GET    | /api/posts/comments/<int:pk>/ | Retrieve comment details             | Any           |
| PUT    | /api/posts/comments/<int:pk>/ | Update comment                       | Author only   |
| DELETE | /api/posts/comments/<int:pk>/ | Delete comment                       | Author only   |
| GET    | /api/categories/              | List all categories                  | Any           |
| POST   | /api/categories/              | Create a new category                | Admin only    |
| GET    | /api/categories/<int:pk>/     | Retrieve category details            | Any           |
| PUT    | /api/categories/<int:pk>/     | Update category                      | Admin only    |
| DELETE | /api/categories/<int:pk>/     | Delete category                      | Admin only    |

## Contributing

Contributions are welcome. Please fork the repository and create a new branch for your feature or bug fix. Once you have made your changes, submit a pull request and your changes will be reviewed.
