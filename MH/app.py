pip install plotly
import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.DataFrame({
    'Option': ['Option 1', 'Option 2', 'Option 3'],
    'Value': [50, 30, 20]
})

option = st.selectbox(
    'Which option do you like best?',
    df['Option'])

st.write('You selected:', option)

fig = px.pie(df, values='Value', names='Option')

if option == 'Option 1':
    st.write('You selected Option 1')
    st.plotly_chart(fig)
elif option == 'Option 2':
    st.write('You selected Option 2')
    st.plotly_chart(fig)
else:
    st.write('You selected Option 3')
    st.plotly_chart(fig)
