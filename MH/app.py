import streamlit as st
import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 30, 35, 40]}
df = pd.DataFrame(data)

# 웹페이지에 데이터프레임 출력
st.write(df)

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
