import streamlit as st

def render_sidebar(
    backend
):

    with st.sidebar:

        st.title(
            "RepoGuru"
        )

        st.caption(
            "AI Repository Assistant"
        )

        st.divider()

        #
        # Model Selection
        #

        available_models = (
            backend.get_available_models()
        )

        current_model = (
            backend.get_current_model()
        )

        selected_model = st.selectbox(
            "LLM Model",
            available_models,
            index=available_models.index(
                current_model
            )
        )

        if (
            selected_model
            != current_model
        ):

            backend.switch_model(
                selected_model
            )

            st.rerun()
        st.divider()
        sessions = (
            backend
            .get_chat_sessions()
        )
        selected_session = (
            st.selectbox(
                "Chat Session",
                sessions
            )
        )
        backend.switch_chat_session(
            selected_session
        )
        new_session = st.text_input(
            "New Session"
        )

        if st.button(
            "Create Session"
        ):

            backend.create_chat_session(
                new_session
            )

            st.rerun()
        st.divider()

        repo_name = (
            backend.get_repository_name()
        )

        if repo_name:

            st.success(
                "Repository Indexed"
            )

            st.markdown(
                f"**{repo_name}**"
            )

            st.divider()

            history = (
                backend.get_chat_history()
            )
            st.metric(
                "Avg Retrieval Score",
                f"{backend.get_average_retrieval_score():.2%}"
            )

            st.metric(
                "Messages",
                len(history)
            )

            st.metric(
                "Status",
                "Ready"
            )

            st.metric(
                "Model",
                current_model
            )

        else:

            st.warning(
                "No Repository Loaded"
            )

        st.divider()

        if st.button(
            "🧹 Clear Chat",
            width="stretch"
        ):

            backend.clear_chat()

            st.rerun()

        if st.button(
            "🗑 Remove Repository",
            width="strech"
        ):

            backend.clear_repository()

            st.rerun()