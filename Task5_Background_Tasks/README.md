# Task 5 - Background Task Queues

## Objective
Implement background task processing using Celery and Redis.

## Technologies Used
- Python
- FastAPI
- Celery
- Redis (Memurai)

## How It Works
When a user requests video processing, the FastAPI API immediately returns
"Processing started".

Celery sends the video-processing task to the background worker through Redis.
The worker then performs the processing without blocking the API.

## API Endpoint

POST `/process-video`

Example response:

{
    "message": "Processing started",
    "task_id": "task-id"
}

## Result
The background task was successfully executed using Celery and Redis.