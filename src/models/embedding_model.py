from sentence_transformers import SentenceTransformer

from src.helpers.config import get_settings


class EmbeddingModel:

    def __init__(self):
        settings = get_settings()
        self.model = SentenceTransformer(settings.embedding_model)

    def encode(self, texts: list[str]):
        return self.model.encode(
            texts,
            normalize_embeddings=True
        )