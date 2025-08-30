# Books Storage API

A simple FastAPI application for storing and managing a personal reading list. Track books you've read with basic information and reading years.

---

## Features

- **RESTful API** with FastAPI  
- **SQLite database** with SQLAlchemy ORM  
- **Async/await** support for better performance  
- **Pydantic validation** for request/response models  
- **Automatic documentation** with Swagger UI

---

## API Endpoints

### Books Management

- `GET /` — Welcome message  
- `GET /books` — Get all books  
- `POST /books` — Add a new book

### Book Schema

```json
{
  "id": 1,
  "name": "Book Title",
  "author": "Author Name",
  "read_year": 2024
}
```

---

## Installation

```bash
git clone https://github.com/Nihaochingiz/BooksStorage.git
cd BooksStorage
```

### Create and activate virtual environment:

- Linux/Mac:
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```
- Windows:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

### Install dependencies:

```bash
pip install -r requirements.txt
```

### Run the application:

```bash
uvicorn main:app --reload
```

---

## Example Requests

### Add a new book

```bash
curl -X POST "http://localhost:8000/books" \
  -H "Content-Type: application/json" \
  -d '{"name": "The Great Gatsby", "author": "F. Scott Fitzgerald", "read_year": 2024}'
```

### Get all books

```bash
curl "http://localhost:8000/books"
```
