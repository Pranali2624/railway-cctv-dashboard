from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.routes import videos
from app.routes import dashboard

app = FastAPI(title="Railway CCTV Monitoring API")

# include API routes
app.include_router(videos.router)
app.include_router(dashboard.router)

# serve frontend folder
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# open frontend on root
@app.get("/")
def home():
    return FileResponse("frontend/index.html")