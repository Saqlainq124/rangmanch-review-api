# Rangmanch Review API

A REST API built with FastAPI and SQLModel for managing theatre play reviews.

This project demonstrates CRUD operations, request validation, SQLite database integration, filtering, pagination, and average rating calculation.

## Features

* Create theatre reviews
* Get all reviews
* Get a single review by ID
* Update reviews
* Delete reviews
* Filter reviews by play name
* Pagination using skip and limit
* Calculate average rating for a play
* Validate ratings between 1 and 5
* SQLite database integration
* Automatic API documentation with Swagger UI
* FastAPI dependency injection
* SQLModel ORM

## Tech Stack

* Python
* FastAPI
* SQLModel
* SQLite
* Pydantic
* Uvicorn

## Project Structure

```text
rangmanch-review-api/
│
├── routes/
│   ├── __init__.py
│   └── reviews.py
│
├── .gitignore
├── README.md
├── database.py
├── main.py
├── models.py
└── requirements.txt
```

## API Endpoints

| Method | Endpoint                      | Description                   |
| ------ | ----------------------------- | ----------------------------- |
| GET    | `/`                           | Welcome message               |
| POST   | `/review/`                    | Create a new review           |
| GET    | `/review/`                    | Get all reviews               |
| GET    | `/review/{review_id}`         | Get a review by ID            |
| PATCH  | `/review/{review_id}`         | Update a review               |
| DELETE | `/review/{review_id}`         | Delete a review               |
| GET    | `/review/average/{play_name}` | Get average rating for a play |

## Create Review

### Request

```json
{
    "play_name": "Hamlet",
    "reviewer_name": "Saqlain",
    "ratings": 5,
    "comment": "Excellent performance and direction."
}
```

### Example Response

```json
{
    "id": 1,
    "play_name": "Hamlet",
    "reviewer_name": "Saqlain",
    "ratings": 5,
    "comment": "Excellent performance and direction.",
    "created_at": "2026-09-28T10:30:00"
}
```

## Rating Validation

The API only accepts ratings from 1 to 5.

```text
1 → Valid
2 → Valid
3 → Valid
4 → Valid
5 → Valid
0 → Invalid
6 → Invalid
```

This validation is implemented using SQLModel fields:

```python
ratings: int = Field(ge=1, le=5)
```

## Filtering Reviews

Reviews can be filtered by play name.

Example:

```text
GET /review/?play_name=Hamlet
```

## Pagination

The API supports pagination using `skip` and `limit`.

Example:

```text
GET /review/?skip=0&limit=10
```

Parameters:

* `skip` — Number of records to skip
* `limit` — Maximum number of records to return

The maximum allowed limit is 50.

## Average Rating

The API can calculate the average rating for a specific play.

Example:

```text
GET /review/average/Hamlet
```

Example response:

```json
{
    "play_name": "Hamlet",
    "average_rating": 4.5,
    "total_reviews": 10
}
```

## Database

The project uses SQLite with SQLModel.

Database URL:

```text
sqlite:///rangmanch.db
```

The database table is automatically created when the application starts.

The SQLite database file is excluded from GitHub using `.gitignore`.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Saqlainq124/rangmanch-review-api.git
```

### 2. Open the project

```bash
cd rangmanch-review-api
```

### 3. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
```

### 4. Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```powershell
pip install -r requirements.txt
```

## Run the Application

Start the FastAPI application using:

```powershell
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## Swagger API Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can use Swagger UI to:

* Create reviews
* View reviews
* Update reviews
* Delete reviews
* Test filtering
* Test pagination
* Check average ratings

## API Testing

The API can be tested using:

* Swagger UI
* Postman
* REST API clients
* Automated API testing frameworks

## Concepts Demonstrated

This project was created to practice:

* FastAPI application structure
* APIRouter
* REST API design
* CRUD operations
* SQLModel
* SQLite
* Dependency Injection
* Database sessions
* Pydantic validation
* Query parameters
* Path parameters
* Pagination
* SQL aggregate functions
* HTTP exception handling
* Response models
* Application lifespan
* Automatic API documentation

## Author

Saqlain Quazi

QA Engineer | API Testing | API Automation | SDET
