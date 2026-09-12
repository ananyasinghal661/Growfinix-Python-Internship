from fastapi import FastAPI
from tasks import process_video_task

app = FastAPI()


@app.post("/process-video")
def process_video():
    task = process_video_task.delay()

    return {
        "message": "Processing started",
        "task_id": task.id
    }