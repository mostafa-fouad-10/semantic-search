from src.helpers.data_loader import DocumentLoader
from src.models.document_embedder import DocumentEmbedder
from src.models.embedding_model import EmbeddingModel
from src.search.engine import SemanticSearchEngine


class SearchService:

    def __init__(self):
        self.document_loader = DocumentLoader()
        self.document_embedder = DocumentEmbedder()
        self.embedding_model = EmbeddingModel()

        self.documents = self.document_loader.load()

        self.embeddings = self.document_embedder.embed(
            self.documents
        )

        self.search_engine = SemanticSearchEngine(
            embeddings=self.embeddings,
            documents=self.documents["text"].tolist(),
        )

    def search(self, query: str) -> list[dict]:
        query_embedding = self.embedding_model.encode([query])[0]

        return self.search_engine.search(query_embedding)
        