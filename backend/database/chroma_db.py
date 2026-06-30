"""
chroma_db.py

Concrete implementation of VectorStore.

Uses ChromaDB.
"""

from chromadb import EphemeralClient

from langchain_chroma import Chroma

from backend.database.vector_store import (
    VectorStore
)


class ChromaDB(VectorStore):

    def __init__(
        self,
        collection_name: str,
        embedding_function,
        persist_directory: str
    ):

        self.client = EphemeralClient()

        self.vector_db = Chroma(
            client=self.client,
            collection_name=collection_name,
            embedding_function=embedding_function
        )

    def add_documents(
        self,
        documents: list
    ) -> None:

        self.vector_db.add_documents(
            documents
        )

    def similarity_search(
        self,
        query: str,
        k: int = 5
    ) -> list:

        return (
            self.vector_db
            .similarity_search(
                query=query,
                k=k
            )
        )

    def delete_collection(
        self
    ) -> None:

        self.client.delete_collection(
            self.vector_db
            ._collection
            .name
        )
    def similarity_search_with_score(
    self,
    query: str,
    k: int = 5
    ):

        return (
            self.vector_db
            .similarity_search_with_score(
                query=query,
                k=k
            )
        )