class FakeVisionModel:
    def predict(self, image_bytes: bytes) -> float:
        # Mock temporário 
        return 0.72  # "probabilidade de deepfake"

class FakeNLPModel:
    def classify(self, text: str) -> float:
        return 0.34  # "probabilidade de fraude textual"
