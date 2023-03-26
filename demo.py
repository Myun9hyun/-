import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('https://raw.githubusercontent.com/Myun9hyun/trash/main/MH/Basketball_processing.csv', index_col=0)

# Get user input
conf_options = df['CONF'].unique()
selected_conf = st.selectbox('Select CONF:', conf_options)

year_options = df['YEAR'].unique()
selected_year = st.selectbox('Select YEAR:', year_options)

# Filter the dataframe based on user input
filtered_df = df[(df['CONF'] == selected_conf) & (df['YEAR'] == selected_year)]

# Get column options from user
column_options = list(filtered_df.columns[3:])  # Exclude the first three columns
selected_columns = st.multiselect('Select columns:', column_options)

# Create the radar chart
fig = px.line_polar(filtered_df, theta=selected_columns, r=filtered_df[selected_columns].iloc[0], line_close=True)
st.plotly_chart(fig)
