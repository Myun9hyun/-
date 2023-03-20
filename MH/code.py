import streamlit as st
import pandas as pd

# 초기 데이터프레임 생성
df = pd.DataFrame({
    '이름': ['Alice', 'Bob', 'Charlie'],
    '나이': [25, 30, 35],
    '성별': ['여성', '남성', '남성']
})

# 데이터프레임 출력
st.write(df)

# 입력 폼 생성
st.header('새로운 데이터 추가')
name = st.text_input('이름')
age = st.number_input('나이', min_value=0)
gender = st.selectbox('성별', ['여성', '남성'])

# "Add Row" 버튼 클릭시 새로운 행 추가
if st.button('Add Row'):
    new_row = {'이름': name, '나이': age, '성별': gender}
    df = df.append(new_row, ignore_index=True)
    st.write('새로운 데이터가 추가되었습니다.')
    st.write(df)
