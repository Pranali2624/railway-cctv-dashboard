from fastapi import APIRouter

router = APIRouter()

@router.get("/api/dashboard/summary")
def dashboard_summary():
    return {
        "total_videos_today": 120,
        "total_trains_monitored": 20,
        "alerts_generated": 5,
        "storage_usage": "120GB"
    }