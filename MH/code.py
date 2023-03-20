import streamlit as st
import pandas as pd

def input_name_score():
    name = st.text_input("이름을 입력하세요:", key="name_input_2")

    score = st.text_input("점수를 입력하세요:", key="score_input")
    return name, score

st.title("학생 점수 입력")

students = []
while True:
    name, score = input_name_score()
    if st.button("입력"):
        students.append({"name": name, "score": score})
    if st.button("멈춤"):
        break

df = pd.DataFrame(students)
st.dataframe(df)
