from fastapi import APIRouter, UploadFile, File
from ..services.inference import analyze_image, analyze_text
from ..schemas import (
    TextInput,
    TextDetectionResponse,
    ImageDetectionResponse,
)

router = APIRouter()

@router.post("/text", response_model=TextDetectionResponse)
def detect_text_fraud(payload: TextInput):
    probability, explanation = analyze_text(payload.text)
    return TextDetectionResponse(
        fraud_probability=probability,
        explanation=explanation
    )

@router.post("/image", response_model=ImageDetectionResponse)
def detect_image_fraud(file: UploadFile = File(...)):
    image_bytes = file.file.read()
    probability, explanation = analyze_image(image_bytes)
    return ImageDetectionResponse(
        deepfake_probability=probability,
        explanation=explanation
    )
