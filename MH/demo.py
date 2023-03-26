import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Load data
df = pd.read_csv("basketball_data.csv")

# User input for CONF and YEAR
conf = st.text_input('Enter a CONF value')
year = st.text_input('Enter a YEAR value')

# Extract rows matching CONF and YEAR
filtered_df = df[df['CONF'] == conf]
filtered_df = filtered_df[filtered_df['YEAR'] == year]

# Multiselect for stats selection
selected_stats = st.multiselect('Select stats', filtered_df.columns)

# Radar chart
if selected_stats:
    fig = go.Figure()
    for stat in selected_stats:
        fig.add_trace(go.Scatterpolar(
            r=filtered_df[stat],
            theta=filtered_df.index,
            fill='toself',
            name=stat
        ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[filtered_df[selected_stats].min().min(), filtered_df[selected_stats].max().max()]
            )
        ),
        showlegend=True
    )
    st.plotly_chart(fig, use_container_width=True)
