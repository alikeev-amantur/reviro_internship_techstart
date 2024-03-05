# reviro_internship_techstart
# Product Inventory Management System

Hey there! Welcome to the Product Inventory Management System project. This system provides CRUD (Create, Read, Update, Delete) operations for managing establishments and products.

## Getting Started

To get started with the project, follow these simple steps:

### Prerequisites

Make sure you have the following installed on your system:

- Docker
- Docker Compose

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```bash
    cd product-inventory-management
    ```

### Running the Application

Once you're in the project directory, you can start the application using Docker Compose. Run the following command:

```bash
docker-compose up -d --build
```
This command will build and start the Docker containers for the application.

After the containers are up and running, you'll need to apply migrations and create a superuser. Here's how you can do it:
```bash
docker-compose exec web python manage.py migrate
```
This command will apply any pending database migrations.
Create Superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```
### Accessing the API Documentation

Once the application is up and running, you can access the API documentation using the following URLs:

- Swagger UI: `/api/schema/swagger-ui/`
- Redoc: `/api/schema/redoc/`

### Testing

The project code has been thoroughly tested using pytest. To run the tests, make sure the Docker containers are running and execute the following command:

```bash
docker-compose exec web pytest
```
