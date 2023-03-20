import streamlit as st
import pandas as pd

# 빈 리스트 생성
name_list = []
score_list = []

# 이름과 점수를 입력받는 함수
def input_name_score():
    name = st.text_input("이름을 입력하세요:")
    score = st.number_input("점수를 입력하세요:", min_value=0, max_value=100, step=1)
    return name, score

# Streamlit 앱 생성
st.title("이름과 점수 입력하기")

# 이름과 점수 입력 받기
while True:
    name, score = input_name_score()
    if not name or not score:
        break
    name_list.append(name)
    score_list.append(score)

# '표 만들기' 버튼을 누르면 데이터프레임으로 표시
if st.button("표 만들기"):
    df = pd.DataFrame({"이름": name_list, "점수": score_list})
    st.write(df)
