"""
collection_manager.py

Responsible for collection lifecycle.

Creates and manages
repository-specific collections.
"""

import uuid


class CollectionManager:

    def create_collection_name(
        self,
        repo_name: str
    ) -> str:

        unique_id = str(
            uuid.uuid4()
        )[:8]

        return (
            f"{repo_name}_{unique_id}"
        )