from celery import Celery

celery_app = Celery(
    "task5",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=["tasks"]
)