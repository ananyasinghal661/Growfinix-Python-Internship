from celery_app import celery_app
import time


@celery_app.task
def process_video_task():
    print("Video processing started...")
    
    # Simulate heavy video processing
    time.sleep(10)
    
    print("Video processing completed!")
    return "Video processing completed successfully"