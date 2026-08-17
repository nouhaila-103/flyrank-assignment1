from fastapi import FastAPI

app = FastAPI(
    title="Task API",
    version="1.0",
)


@app.get("/", summary="Get API information")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"],
    }


@app.get("/health", summary="Check API health")
def health():
    return {"status": "ok"}