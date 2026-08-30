import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from src.helpers.config import get_settings


class SemanticSearchEngine:

    def __init__(
        self,
        embeddings: np.ndarray,
        documents: list[str],
    ):
        settings = get_settings()

        self.embeddings = embeddings
        self.documents = documents
        self.top_k = settings.top_k

    def search(self, query_embedding: np.ndarray) -> list[dict]:
        similarities = cosine_similarity(
            query_embedding.reshape(1, -1),
            self.embeddings,
        )[0]

        top_indices = np.argsort(similarities)[::-1][:self.top_k]

        return [
            {
                "document": self.documents[index],
                "score": float(similarities[index]),
            }
            for index in top_indices
        ]