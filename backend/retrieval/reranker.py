"""
reranker.py

Responsible for improving
retrieval ordering.

Current implementation:
No-op reranker.

Can later be replaced with
CrossEncoder based ranking.
"""


class Reranker:

    def rerank(
        self,
        query: str,
        documents: list
    ) -> list:
        """
        MVP implementation.

        Return documents unchanged.
        """

        return documents