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
password3 = "초초"
answer3 = "릎샴"
quiz1_password = st.text_input("1번 문제 오픈을 위한 비밀번호를 입력해주세요!",  key="quiz1_password")
if quiz1_password == password1:
    quiz1 = st.text_input("우리 길드의 이름은 뭘까?")
    if st.button("정답 확인", key="check_answer_button1"):
        if quiz1 == answer1:
            st.balloons()
            st.success("정답입니다!")
            st.write("우리 길드와 함께해줘서 고마워 ╰(*°▽°*)╯")
            st.write("2번 문제 오픈을 위한 비밀번호는 5678입니다")
            
            
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
            st.balloons()
            st.success("정답입니다!")
            st.write("[둥둥향]은 조잡한 페이지 만드는 역할을 맡고 있어!")
            st.write("3번 문제의 비밀번호는 '초초'야!")
        else :
            st.error("다시 한번 생각해봐!")
    if st.button("힌트 보기", key = "check_hint_button2"):
        st.write("만든 사람의 직업은 캐논마스터야!")
quiz3_password = st.text_input("3번 문제 오픈을 위한 비밀번호를 입력해주세요!", key = "quiz3_password3")
if quiz3_password == password3:
    quiz3 = st.text_input("이번 메이플 팬페스트 금손 부스에 참석한 간부는 누구일까요?")
    if st.button("정답 확인"):
        if quiz3 == answer3:
            st.ballons()
            st.success("정답입니다!")
            st.write("[릎샴]은 이번 팬페스트에 '볼빵빵하우스'라는 부스 담당자로 참석했어!")
            st.write("[릎샴]은 길드에서 포스터, 길드규정문 등을 만드는 디자인 역할을 하고 있어!")
        else : 
            st.warning("다시 생각해봐!")
    if st.button("힌트 보기"):
        st.write("캡틴 김수호를 생각해봐!")
else :
    st.error("비밀번호가 틀렸어!")