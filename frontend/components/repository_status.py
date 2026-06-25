"""
repository_status.py
"""

import streamlit as st


def render_repository_status(
    repository_name: str | None,
    current_model: str
):

    st.subheader(
        "Repository Status"
    )

    col1, col2 = st.columns(2)

    with col1:

        if repository_name:

            st.success(
                f"Loaded: {repository_name}"
            )

        else:

            st.info(
                "No repository loaded."
            )

    with col2:

        st.info(
            f"Model: {current_model}"
        )