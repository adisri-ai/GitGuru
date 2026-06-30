"""
vector_store.py

Abstract vector store contract.

Allows swapping:

- ChromaDB
- FAISS
- Pinecone

without changing services.
"""

from abc import ABC
from abc import abstractmethod


class VectorStore(ABC):

    @abstractmethod
    def add_documents(
        self,
        documents: list
    ) -> None:
        pass

    @abstractmethod
    def similarity_search(
        self,
        query: str,
        k: int = 5
    ) -> list:
        pass
    @abstractmethod
    def similarity_search_with_score(
        self,
        query: str,
        k: int = 5
    ):
        pass
    @abstractmethod
    def delete_collection(
        self
    ) -> None:
        pass