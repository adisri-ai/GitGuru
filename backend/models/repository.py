"""
repository.py

Domain model representing a GitHub repository
throughout the application.

All repository-related modules should pass around
this object instead of passing multiple parameters.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Repository:
    """
    Represents a repository loaded into the system.
    """

    repo_name: str
    owner: str
    repo_url: str

    local_path: Optional[str] = None

    default_branch: Optional[str] = None
    primary_language: Optional[str] = None

    indexed: bool = False

    metadata: dict = field(default_factory=dict)