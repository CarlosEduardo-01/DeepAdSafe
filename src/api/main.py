from fastapi import FastAPI
from .routers.detection import router as detection_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="DeepAdSafe API",
        description="API para detecção de deepfakes e anúncios fraudulentos.",
        version="0.1.0",
    )

    # Rotas
    app.include_router(detection_router, prefix="/detect", tags=["Detection"])

    return app

app = create_app()


