from ..models import FakeVisionModel, FakeNLPModel
from ..utils.logger import log_event

vision_model = FakeVisionModel()
nlp_model = FakeNLPModel()

def analyze_text(text: str):
    prob = nlp_model.classify(text)
    explanation = "Modelo mockado retornou probabilidade estimada baseada no texto fornecido."
    log_event("text_inference", {"prob": prob})
    return prob, explanation

def analyze_image(image_bytes: bytes):
    prob = vision_model.predict(image_bytes)
    explanation = "Modelo mockado analisou a imagem e retornou um score estimado."
    log_event("image_inference", {"prob": prob})
    return prob, explanation
