"""
retriever.py

Responsible for semantic retrieval
from the vector database.
"""

from backend.database.vector_store import VectorStore


class Retriever:

    def __init__(
        self,
        vector_store: VectorStore
    ):
        self.vector_store = vector_store
    def retrieve_with_scores(
        self,
        query: str,
        top_k: int = 5
    ):

        return (
            self.vector_store
            .similarity_search_with_score(
                query=query,
                k=top_k
            )
        )
    def retrieve(
        self,
        query: str,
        top_k: int = 5
    ) -> list:
        """
        Retrieve candidate chunks.
        """

        return self.vector_store.similarity_search(
            query=query,
            k=top_k
        )