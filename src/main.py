import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI
from telemetry.opentelemetry import instrument
from api.collections import router as collection_router
from api.documents import router as document_router
from api.rag import router as rag_router
from api.health import router as health_router
from api.people import router as people_router
from services.bm25_service import rebuild_index

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup.
    """
    rebuild_index()

    yield

    """
    Application shutdown.
    """
    pass

def create_app() -> FastAPI:
    """
    Application factory.
    Creates and configures FastAPI application.
    """
    app = FastAPI(
        title="AI-Dyana",
        version="1.0.0",
        description="AI-Dyana RAG Service using FastAPI and Milvus",
        lifespan=lifespan,
    )

    instrument(app)

    # Register API routers
    app.include_router(health_router)
    app.include_router(collection_router)
    app.include_router(document_router)
    app.include_router(rag_router)
    app.include_router(people_router)

    @app.get("/")
    def health():
        return {
            "application": "AI-Dyana",
            "status": "running"
        }

    return app

def main():
    """
    Application entrypoint.
    """
    uvicorn.run(
        "main:create_app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        factory=True
    )

app = create_app()

if __name__ == "__main__":
    main()