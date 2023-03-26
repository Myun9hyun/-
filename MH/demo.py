import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("https://raw.githubusercontent.com/Myun9hyun/trash/main/MH/Basketball_processing.csv")

selected_stats = st.multiselect('Select stats', df.columns)

if selected_stats:
    fig = go.Figure()
    for stat in selected_stats:
        fig.add_trace(go.Scatterpolar(
            r=[df[stat].mean()],
            theta=[stat],
            fill='toself',
            name=stat
        ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[df[selected_stats].min().min(), df[selected_stats].max().max()]
            )
        ),
        showlegend=True
    )
    st.plotly_chart(fig, use_container_width=True)
