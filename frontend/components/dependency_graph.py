"""
dependency_graph.py
"""

import streamlit as st
import networkx as nx
import plotly.graph_objects as go


def render_dependency_graph(
    graph: nx.DiGraph
):

    if graph is None:

        st.info(
            "No dependency graph available."
        )

        return

    pos = nx.spring_layout(
        graph,
        seed=42
    )

    edge_x = []
    edge_y = []

    for edge in graph.edges():

        x0, y0 = pos[
            edge[0]
        ]

        x1, y1 = pos[
            edge[1]
        ]

        edge_x.extend(
            [
                x0,
                x1,
                None
            ]
        )

        edge_y.extend(
            [
                y0,
                y1,
                None
            ]
        )

    edge_trace = (
        go.Scatter(
            x=edge_x,
            y=edge_y,
            mode="lines",
            hoverinfo="none"
        )
    )

    node_x = []
    node_y = []
    labels = []

    for node in graph.nodes():

        x, y = pos[node]

        node_x.append(x)
        node_y.append(y)

        labels.append(node)

    node_trace = (
        go.Scatter(
            x=node_x,
            y=node_y,
            mode="markers+text",
            text=labels,
            textposition="top center",
            hoverinfo="text",
            marker=dict(
                size=15
            )
        )
    )

    fig = go.Figure(
        data=[
            edge_trace,
            node_trace
        ]
    )

    fig.update_layout(
        height=700,
        showlegend=False
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )