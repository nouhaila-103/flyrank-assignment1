# Task API

A simple CRUD API for managing a to-do list, built with Python and FastAPI.

The API uses an **in-memory list** to store tasks. No database is used, so tasks are reset whenever the server restarts.

## Features

* Create tasks
* Read all tasks
* Read a single task
* Update tasks
* Delete tasks
* Input validation
* HTTP status codes
* Interactive Swagger UI documentation

## Requirements

* Python 3.10+
* FastAPI

## Installation

Clone the repository and enter the project directory:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd task-api
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
python -m fastapi dev main.py
```

The API will be available at:

```text
http://localhost:8000
```

Swagger UI is available at:

```text
http://localhost:8000/docs
```

## API Endpoints

| Method | Endpoint      | Description                      |
| ------ | ------------- | -------------------------------- |
| GET    | `/`           | Get API information              |
| GET    | `/health`     | Check whether the API is running |
| GET    | `/tasks`      | Get all tasks                    |
| GET    | `/tasks/{id}` | Get one task                     |
| POST   | `/tasks`      | Create a new task                |
| PUT    | `/tasks/{id}` | Update a task                    |
| DELETE | `/tasks/{id}` | Delete a task                    |
| GET    | `/docs`       | Interactive Swagger UI           |

## Example Task

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "done": false
}
```

## Create a Task

Request:

```bash
curl -i -X POST http://localhost:8000/tasks \
-H "Content-Type: application/json" \
-d '{"title":"Buy milk"}'
```

The API returns status `201 Created` when the task is successfully created.

## Error Handling

The API uses the following status codes:

* `200 OK` — successful read or update
* `201 Created` — task successfully created
* `204 No Content` — task successfully deleted
* `400 Bad Request` — invalid or empty input
* `404 Not Found` — task does not exist

## In-Memory Storage

Tasks are stored only in memory. If the server is stopped and started again, newly created tasks disappear and the three example tasks are restored.

This is intentional for this assignment. A database will be introduced in a later stage of the backend learning process.

## Swagger UI

The API includes automatically generated Swagger UI through FastAPI.

Open:

```text
http://localhost:8000/docs
```

Use the **Try it out** buttons to test the complete CRUD cycle without using curl.

<!-- Add your Swagger screenshot below before submitting -->

## Project Structure

```text
task-api/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Author

Nouhaila RABII
