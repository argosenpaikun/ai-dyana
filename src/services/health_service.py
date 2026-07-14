from services.bm25_service import check_health as check_bm25
from mongodb.client import check_health as check_mongodb
from milvus.client import check_health as check_milvus

def check_depedencies():
    checks = {
        "bm25": check_bm25(),
        "mongodb": check_mongodb(),
        "milvus": check_milvus()
    }

    return {
        "status": "UP" if all(checks.values()) else "DOWN",
        "checks": checks
    }