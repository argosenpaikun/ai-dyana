import time
from datetime import datetime, timezone

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from services.health_service import check_depedencies


router = APIRouter(
    prefix="/health",
    tags=["Health"]
)

START_TIME = time.time()

@router.get("/live")
def liveness():
    """
    Liveness probe

    Indicates whether the application process is running
    """
    return {
        "status": "UP",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

@router.get("/ready")
def readiness():
    """
    Readiness probe

    Indicates whether all dependencies are ready
    """
    health = check_depedencies()

    response = {
        "application": "AI-Dyana",
        "status": health["status"],
        "uptime_seconds": round(time.time() - START_TIME),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "check": {
            name: "UP" if ok else "DOWN"
            for name, ok in health["checks"].items()
        }
    }

    if health["status"] == "DOWN":
            return JSONResponse(status_code=503, content=response)
    return response