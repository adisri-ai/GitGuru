"""
main.py

Backend Facade.

Single entry point for all backend
operations.

Frontend communicates ONLY with this
class.
"""

from backend.pipeline.base.pipeline_context import (
    PipelineContext
)
from backend.managers.retreival_metrics_manager import RetrievalMetricsManager
from backend.pipeline.processing_pipeline import (
    ProcessingPipeline
)
from backend.services.dependency_graph_service import (
    DependencyGraphService
)
from backend.managers.llm_manager import (
    LLMManager
)

from backend.services.llm_service import (
    LLMService
)

from backend.pipeline.tasks.repo_parser_task import (
    RepoParserTask
)

from backend.pipeline.tasks.chunk_task import (
    ChunkTask
)

from backend.pipeline.tasks.embedding_task import (
    EmbeddingTask
)

from backend.pipeline.tasks.store_task import (
    StoreTask
)

from backend.llm.embeedings import (
    EmbeddingProvider
)
from backend.managers.llm_manager import (
    LLMManager
)

from backend.services.llm_service import (
    LLMService
)

from backend.managers.database_manager import (
    DatabaseManager
)

from backend.tools.tools_factory import (
    ToolsFactory
)

from backend.retrieval.retriever import (
    Retriever
)

from backend.services.agent_service import (
    AgentService
)

from backend.services.database_service import (
    DatabaseService
)

from backend.services.repository_service import (
    RepositoryService
)

from backend.services.chat_service import (
    ChatService
)

from backend.config.constants import (
    MAX_CHAT_HISTORY
)
from dotenv import load_dotenv
from backend.llm.registry.model_registry import DEFAULT_MODEL
class BackendFacade:

    """
    Main entry point of backend.
    """

    def __init__(self):

        self.repository_service = (
            RepositoryService()
        )

        self.chat_service = (
            ChatService()
        )

        self.embedding_provider = (
            EmbeddingProvider()
        )

        self.database_manager = (
            DatabaseManager(
                embedding_function=
                self.embedding_provider.embeddings,
                persist_directory=
                "./storage/chroma_db"
            )
        )

        self.database_service = (
            DatabaseService(
                self.database_manager
            )
        )
        self.dependency_graph_service = (
            DependencyGraphService()
        )

        self.dependency_graph = None
        self.llm_manager = (
            LLMManager(
                default_model=
                DEFAULT_MODEL
            )
        )

        self.llm_service = (
            LLMService(
                self.llm_manager
            )
        )
        self.retrieval_metrics_manager = RetrievalMetricsManager()
        self.agent_service = None

        self.current_repository = None
        load_dotenv()
    def get_dependency_graph(
        self
    ):

        return (
            self.dependency_graph
        )
    def ingest_repository(
        self,
        github_url: str
    ) -> str:

        """
        Clone repository and
        build vector database.
        """

        repository = (
            self.repository_service
            .load_repository(
                github_url
            )
        )

        self.current_repository = (
            repository
        )
        self.dependency_graph = (
            self.dependency_graph_service
            .build_graph(
                repository.local_path
            )
        )

        source_files = (
            self.repository_service
            .scan_repository(
                repository
            )
        )

        vector_db = (
            self.database_service
            .create_repository_database(
                repository.repo_name
            )
        )

        pipeline = (
            ProcessingPipeline(
                [
                    RepoParserTask(),
                    ChunkTask(),
                    EmbeddingTask(
                        self.embedding_provider.embeddings
                    ),
                    StoreTask(
                        self.database_service
                    )
                ]
            )
        )

        context = PipelineContext(
            repository=repository,
            source_files=source_files
        )

        pipeline.execute(
            context
        )

        self.retriever = Retriever(
            vector_db
        )

        tools = (
            ToolsFactory
            .create_tools(
                self.retriever,
                self.retrieval_metrics_manager
            )
        )

        self.agent_service = (
            AgentService(
                llm=
                self.llm_service.get_llm(),
                tools=tools
            )
        )

        return (
            f"Repository "
            f"{repository.repo_name} "
            f"indexed successfully."
        )

    def chat(
        self,
        query: str
    ) -> str:

        """
        Ask questions about repo.
        """

        if self.agent_service is None:

            raise RuntimeError(
                "No repository indexed."
            )

        self.chat_service.add_user_message(
            query
        )

        history = (
            self.chat_service
            .get_recent_history(
                MAX_CHAT_HISTORY
            )
        )

        response = (
            self.agent_service
            .process_query(
                query=query,
                chat_history=history
            )
        )

        self.chat_service.add_ai_message(
            response
        )

        return response

    def get_chat_history(
        self
    ):

        return (
            self.chat_service
            .get_history()
        )

    def clear_chat(
        self
    ):

        self.chat_service.clear()

    def clear_repository(
        self
    ):

        if self.current_repository:

            self.repository_service.cleanup_repository(
                self.current_repository
            )

        self.database_service.delete_database()

        self.current_repository = None

        self.agent_service = None
        self.dependency_graph = None
    def switch_model(
    self,
    model_name: str
    ):

        self.llm_service.switch_model(
            model_name
        )
        self.retrieval_metrics_manager.reset()
        if self.agent_service:

            self.retriever = Retriever(
                self.database_service
                .get_database()
            )
            tools = (
                ToolsFactory
                .create_tools(
                    self.retriever,
                    self.retrieval_metrics_manager
                )
            )

            self.agent_service = (
                AgentService(
                    llm=
                    self.llm_service.get_llm(),
                    tools=tools
                )
            )

    def create_chat_session(
        self,
        session_name: str
    ):

        self.chat_service.create_session(
            session_name
        )
    def switch_chat_session(
        self,
        session_name: str
    ):

        self.chat_service.switch_session(
            session_name
        )
    def get_chat_sessions(
        self
    ):

        return (
            self.chat_service
            .get_sessions()
        )
    def get_available_models(
        self
    ):

        return (
            self.llm_service
            .get_available_models()
        )
    def get_average_retrieval_score(
            self
        ):
            return (
                self.retrieval_metrics_manager
                .get_average_score()
            )

    def get_current_model(
        self
    ):

        return (
            self.llm_service
            .get_current_model()
        )

    def get_repository_name(
        self
    ) -> str | None:

        if not self.current_repository:
            return None

        return (
            self.current_repository
            .repo_name
        )