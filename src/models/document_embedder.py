import pandas as pd
import numpy as np

from src.models.embedding_model import EmbeddingModel


class DocumentEmbedder:

    def __init__(self):
        self.embedding_model = EmbeddingModel()

    def embed(self, documents: pd.DataFrame) -> np.ndarray:
        texts = documents["text"].tolist()

        return self.embedding_model.encode(texts)