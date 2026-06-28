# <div align="center">🤖 GitGuru</div>

<h3 align="center">
AI-Powered Repository Intelligence Platform
</h3>

<p align="center">

Semantic Repository Search • Agentic RAG • Multi-LLM • LangChain • LLD Architecture

</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue)
![LangChain](https://img.shields.io/badge/LangChain-Agent-success)
![ChromaDB](https://img.shields.io/badge/VectorDB-Chroma-orange)
![Groq](https://img.shields.io/badge/Groq-Supported-red)
![Ollama](https://img.shields.io/badge/Ollama-Supported-lightgrey)
![Architecture](https://img.shields.io/badge/Architecture-Layered-blueviolet)
![Design Patterns](https://img.shields.io/badge/Design-LLD-important)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

# 🚀 Overview

GitGuru is an **AI-powered Repository Intelligence Platform** capable of understanding an entire GitHub repository through **Retrieval-Augmented Generation (RAG)**, **semantic search**, **agentic tool usage**, and **multiple Large Language Models**.

Unlike conventional GitHub chatbots that rely solely on the uploaded repository context, GitGuru is designed using **Low-Level Design (LLD)** principles and **SOLID architecture**, making it modular, extensible and production-ready.

It combines:

* 🧠 LangChain Agents
* 📚 Semantic Retrieval
* ⚡ Runtime LLM Switching
* 🔍 Agentic Tool Calling
* 📈 Live Retrieval Metrics
* 🕸 Interactive Dependency Graphs
* 💬 Multi-session Chat
* 🏗 Clean Layered Architecture

---

# ✨ Features

## 📂 Repository Intelligence

* Clone any public GitHub repository
* Parse complete project structure
* Intelligent repository indexing
* Automatic chunk generation
* Semantic vector database creation

---

## 🤖 AI Assistant

* Context-aware conversations
* Repository-specific answers
* Multi-turn chat history
* Runtime model switching
* Agentic reasoning using LangChain

---

## 🔍 Agentic Tools

* Semantic Code Search
* File Reader
* Dependency Analyzer
* GitHub Issue Search
* Interactive Dependency Graph

---

## 📈 Performance Monitoring

* Live Retrieval Similarity Score
* Average Session Retrieval Score
* Runtime Model Tracking
* Repository Status
* Session Statistics

---

## 🧠 Multiple LLM Providers

Current Support

* Groq
* Ollama

Designed to support

* OpenRouter
* Gemini
* OpenAI
* Claude

without changing the application logic.

---

# ⚙️ System Workflow

```text
            GitHub Repository

                    │

                    ▼

          Repository Cloning

                    │

                    ▼

            Source Code Parser

                    │

                    ▼

          Intelligent Chunking

                    │

                    ▼

        Embedding Generation

                    │

                    ▼

              ChromaDB

                    │

                    ▼

         Semantic Retriever

                    │

                    ▼

          LangChain Agent

          ┌───────────────┐
          │               │
          ▼               ▼

      Tool Calling     LLM Manager

                            │

                  Adapter Design Pattern

              ┌──────────┴──────────┐

              ▼                     ▼

        Ollama Adapter        Groq Adapter

              │                     │

              ▼                     ▼

        ChatOllama            ChatGroq

                    │

                    ▼

             Final Response
```

---

# 🏛 Layered Architecture

```text
Frontend
│
├── Components
├── Pages
└── Styles

            │

            ▼

Backend Facade

            │

────────────────────────────────────

Services Layer

• RepositoryService

• ChatService

• AgentService

• DatabaseService

• LLMService

────────────────────────────────────

Pipeline Layer

RepoParser

↓

ChunkTask

↓

EmbeddingTask

↓

StoreTask

────────────────────────────────────

Retrieval Layer

Retriever

↓

Reranker

↓

Context Builder

────────────────────────────────────

LLM Layer

LLM Manager

↓

Factory

↓

Adapter

↓

Clients

────────────────────────────────────

Database Layer

ChromaDB

↓

Vector Store
```

---

# 📐 UML Architecture

```text
                           +----------------------+
                           |    BackendFacade     |
                           +----------+-----------+
                                      |
      +-------------------------------+-------------------------------+
      |                               |                               |
      ▼                               ▼                               ▼

RepositoryService              DatabaseService                 ChatService

      |                               |

      ▼                               ▼

ProcessingPipeline              ChromaDB

      |                               |

      ▼                               ▼

 Retriever ----------------------> SearchCodebaseTool

      |

      ▼

 AgentService

      |

      ▼

 AgentFactory

      |

      ▼

 LangChain Agent

      |

      ▼

 LLM Manager

      |

      ▼

 <<Adapter>>

 LLMAdapter

     ▲

 ┌───┴───────────────┐

 │                   │

 ▼                   ▼

GroqAdapter     OllamaAdapter

 │                   │

 ▼                   ▼

GroqClient     OllamaClient
```

---

# 🏗 Design Patterns Used

| Pattern              | Usage                                              |
| -------------------- | -------------------------------------------------- |
| Facade               | BackendFacade exposes a single backend entry point |
| Adapter              | Supports multiple LLM providers                    |
| Factory              | Dynamically creates LLM adapters                   |
| Strategy             | Swappable retrieval pipeline components            |
| Pipeline             | Repository indexing workflow                       |
| Repository           | Database abstraction                               |
| Dependency Injection | Loose coupling between services                    |
| Singleton            | Session-level backend lifecycle                    |

---

# 🧠 LLM Architecture

```text
                    LLMService

                        │

                        ▼

                   LLMManager

                        │

             Active LLM Adapter

                        │

          ┌─────────────┴─────────────┐

          ▼                           ▼

   OllamaAdapter               GroqAdapter

          │                           │

          ▼                           ▼

    OllamaClient                GroqClient

          │                           │

          ▼                           ▼

     ChatOllama                 ChatGroq
```

---

# 🤖 Agentic Workflow

```text
User Question

      │

      ▼

LangChain Agent

      │

      ▼

Need Repository Information?

      │

 ┌────┴─────┐

 │          │

Yes         No

 │

 ▼

Tool Selection

 │

 ├── Semantic Search

 ├── Read File

 ├── Dependency Analysis

 └── GitHub Issue Search

 │

 ▼

Retrieved Context

 │

 ▼

LLM

 │

 ▼

Final Response
```

---

# 🛠 Technology Stack

| Layer            | Technology            |
| ---------------- | --------------------- |
| Frontend         | Streamlit             |
| Backend          | Python                |
| AI Framework     | LangChain             |
| Agent Framework  | LangGraph             |
| Vector Database  | ChromaDB              |
| Embeddings       | Sentence Transformers |
| Local LLM        | Ollama                |
| Cloud LLM        | Groq                  |
| Dependency Graph | NetworkX + PyVis      |

---

# 📊 Live Metrics

GitGuru continuously monitors retrieval quality during conversations.

Current metrics include

* Average Retrieval Similarity
* Session Retrieval Score
* Active LLM
* Repository Status
* Chat Statistics

Additional metrics can easily be integrated due to the modular architecture.

---

# 📁 Project Structure

```text
backend/

├── database/

├── llm/
│   ├── adapters/
│   ├── clients/
│   ├── factories/
│   ├── registry/
│   └── prompts/

├── managers/

├── pipeline/
│   ├── base/
│   └── tasks/

├── retrieval/

├── services/

├── tools/

└── utils/

frontend/

├── components/

├── pages/

├── styles/

└── utils/
```

---

# 🚀 Installation

```bash
git clone https://github.com/<your-username>/GitGuru.git

cd GitGuru

python -m venv venv

source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
GROQ_API_KEY=your_api_key
```

Run the application

```bash
streamlit run app.py
```

---

# 🎯 Why GitGuru?

| Traditional GitHub Chat        | GitGuru |
| ------------------------------ | ------- |
| Basic LLM Chat                 | ✅       |
| Semantic Repository Search     | ✅       |
| Agentic Tool Calling           | ✅       |
| Runtime LLM Switching          | ✅       |
| Interactive Dependency Graph   | ✅       |
| Live Retrieval Metrics         | ✅       |
| Multiple Chat Sessions         | ✅       |
| LLD-based Modular Architecture | ✅       |
| Easily Extendable              | ✅       |

---

# 🔮 Roadmap

* [x] Agentic RAG
* [x] Multi-LLM Support
* [x] Runtime Model Switching
* [x] Dependency Visualization
* [x] Live Retrieval Metrics
* [x] Multi-session Chat

Future Enhancements

* [ ] AI Code Review
* [ ] Pull Request Reviewer
* [ ] Knowledge Graph Generation
* [ ] Repository Health Dashboard
* [ ] Persistent Chat Sessions
* [ ] Repository Architecture Scoring
* [ ] Multi-Agent Collaboration

---

# 🤝 Contributing

Contributions, feature requests and suggestions are always welcome.

If you'd like to improve GitGuru, feel free to fork the repository and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a Star!

**Built with ❤️ using Python, LangChain, ChromaDB, Groq and Streamlit**

</div>
