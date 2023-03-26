import pandas as pd
import streamlit as st
import plotly.express as px
url = "https://raw.githubusercontent.com/Myun9hyun/trash/main/MH/Basketball_processing.csv"

df = pd.read_csv("https://raw.githubusercontent.com/Myun9hyun/trash/main/MH/Basketball_processing.csv", index_col=0)

conf_list = list(df["CONF"].unique())
conf_choice = st.sidebar.selectbox("Select a conference", conf_list)

filtered_df = df[df["CONF"] == conf_choice]

year_list = list(filtered_df["YEAR"].unique())
year_choice = st.sidebar.selectbox("Select a year", year_list)

selected_cols = st.multiselect("Select columns to display", list(filtered_df.columns))

display_df = filtered_df[filtered_df["YEAR"] == year_choice][selected_cols]

if not display_df.empty:
    st.plotly_chart(px.line_polar(display_df, theta=selected_cols, r=display_df.iloc[0].values))
else:
    st.warning("No data found for selected filters.")
