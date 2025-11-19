from pydantic import BaseModel

class TextInput(BaseModel):
    text: str

class TextDetectionResponse(BaseModel):
    fraud_probability: float
    explanation: str

class ImageDetectionResponse(BaseModel):
    deepfake_probability: float
    explanation: str
