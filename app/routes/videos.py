from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import datetime

from app.database import SessionLocal
from app.models import Video

router = APIRouter()


# Database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Get videos with filtering
@router.get("/api/videos")
def get_videos(
    train_id: int = Query(None),
    camera_id: int = Query(None),
    from_date: str = Query(None),
    to_date: str = Query(None),
    db: Session = Depends(get_db)
):

    query = db.query(Video)

    if train_id:
        query = query.filter(Video.train_id == train_id)

    if camera_id:
        query = query.filter(Video.camera_id == camera_id)

    if from_date:
        query = query.filter(Video.stored_timestamp >= from_date)

    if to_date:
        query = query.filter(Video.stored_timestamp <= to_date)

    videos = query.all()

    return videos

@router.get("/api/videos/{video_id}")
def video_details(video_id: int, db: Session = Depends(get_db)):
    video = db.query(Video).filter(Video.id == video_id).first()

    if not video:
        return {"error": "Video not found"}

    return video