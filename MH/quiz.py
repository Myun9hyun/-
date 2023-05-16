import streamlit as st
import pandas as pd
import os
from PIL import Image
import requests
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import joblib
import xgboost as xgb
import seaborn as sns
from streamlit_option_menu import option_menu

password1 = "1234"
answer1 = "아기자기"
password2 = "5678"
answer2 = "둥둥향"
quiz1_password = st.text_input("1번 문제 오픈을 위한 비밀번호를 입력해주세요!",  key="quiz1_password")
if quiz1_password == password1:
    quiz1 = st.text_input("우리 길드의 이름은 뭘까?")
    if st.button("정답 확인", key="check_answer_button1"):
        if quiz1 == answer1:
            st.balloon(
            st.success("정답입니다!")
            st.success("2번 문제 오픈을 위한 비밀번호는 5678입니다")
            )
        else:
            st.warning("다시 한번 생각해봐!")
    if st.button("힌트 보기", key="check_hint_button1"):
            st.write("이건 힌트 줄수가 없어! 잘 생각해봐")
else : 
    st.warning("비밀번호가 틀렸어!")
quiz2_password = st.text_input("2번 문제 오픈을 위한 비밀번호를 입력해주세요!", key = "quiz2_password")
if quiz2_password == password2:
    quiz2 = st.text_input("이 페이지 누가 만들었을까요?")
    if st.button("정답 확인", key="check_answer_button2"):
        if quiz2 == answer2:
            st.success("정답입니다!")
        else :
            st.error("다시 한번 생각해봐!")
    if st.button("힌트 보기", key = "check_hint_button2"):
        st.write("만든 사람의 직업은 캐논마스터야!")

else :
    st.error("비밀번호가 틀렸어!")