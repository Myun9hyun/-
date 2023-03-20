import streamlit as st
import pandas as pd

# 초기 데이터프레임 생성
df = pd.DataFrame({
    '이름': [],
    '나이': [],
    '성별': []
})

# 사용자 입력 받기
st.header('데이터 입력')
add_more = True
while add_more:
    name = st.text_input('이름')
    age = st.number_input('나이')
    gender = st.selectbox('성별', ['여성', '남성'])

    # 새로운 행 추가
    if st.button('Add Row'):
        new_row = {'이름': name, '나이': age, '성별': gender}
        df = df.append(new_row, ignore_index=True)
        st.success('새로운 데이터가 추가되었습니다.')

    # 사용자가 더 입력할 것인지 묻기
    add_more = st.button('Add more')

# 데이터프레임 출력
st.header('입력한 데이터프레임')
st.write(df)
