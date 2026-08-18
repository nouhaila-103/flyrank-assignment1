import sqlite3
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Task API",
    version="1.0",
    description="A simple CRUD API using SQLite for managing tasks.",
)

DATABASE = "tasks.db"


def get_db():
    return sqlite3.connect(DATABASE)


conn = get_db()

conn.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    done BOOLEAN NOT NULL
)
""")

conn.commit()

count = conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]

if count == 0:
    conn.executemany(
        "INSERT INTO tasks (id, title, done) VALUES (?, ?, ?)",
        [
            (1, "Learn FastAPI", False),
            (2, "Build CRUD API", False),
            (3, "Learn Git", True),
        ],
    )
    conn.commit()

conn.close()


# Stage 1: Root endpoint
@app.get("/", summary="Get API information")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"],
    }


# Stage 1: Health endpoint
@app.get("/health", summary="Check API health")
def health():
    return {"status": "ok"}


# Stage 2: Get all tasks
@app.get(
    "/tasks",
    summary="List all tasks",
    description="Returns all tasks currently stored in memory.",
)
def get_tasks():
    return tasks


# Stage 2: Get one task
@app.get(
    "/tasks/{task_id}",
    summary="Get one task",
    description="Returns a single task by its ID.",
)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    return JSONResponse(
        status_code=404,
        content={"error": f"Task {task_id} not found"},
    )


# Stage 3: Create a task
@app.post(
    "/tasks",
    status_code=201,
    summary="Create a task",
    description="Creates a new task with a title and sets done to false.",
)
def create_task(body: dict):
    title = body.get("title")

    if not isinstance(title, str) or not title.strip():
        return JSONResponse(
            status_code=400,
            content={"error": "Title is required and cannot be empty"},
        )

    new_id = max([task["id"] for task in tasks], default=0) + 1

    new_task = {
        "id": new_id,
        "title": title.strip(),
        "done": False,
    }

    tasks.append(new_task)

    return new_task


# Stage 4: Update a task
@app.put("/tasks/{task_id}", summary="Update a task")
def update_task(task_id: int, body: dict):
    task = next(
        (task for task in tasks if task["id"] == task_id),
        None,
    )

    if task is None:
        return JSONResponse(
            status_code=404,
            content={"error": f"Task {task_id} not found"},
        )

    if not body:
        return JSONResponse(
            status_code=400,
            content={"error": "Request body cannot be empty"},
        )

    if "title" in body:
        if not isinstance(body["title"], str) or not body["title"].strip():
            return JSONResponse(
                status_code=400,
                content={"error": "Title cannot be empty"},
            )

        task["title"] = body["title"].strip()

    if "done" in body:
        if not isinstance(body["done"], bool):
            return JSONResponse(
                status_code=400,
                content={"error": "Done must be true or false"},
            )

        task["done"] = body["done"]

    return task


# Stage 4: Delete a task
@app.delete("/tasks/{task_id}", status_code=204, summary="Delete a task")
def delete_task(task_id: int):
    task = next(
        (task for task in tasks if task["id"] == task_id),
        None,
    )

    if task is None:
        return JSONResponse(
            status_code=404,
            content={"error": f"Task {task_id} not found"},
        )

    tasks.remove(task)