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
answer1 = "안녕"

quiz1_password = st.text_input("1번 문제 오픈을 위한 비밀번호를 입력해주세요!",  key="quiz1_password")
if quiz1_password == password1:
    quiz1 = st.text_input("만나서 반가울때 하는 인사는?")
    if quiz1 == answer1:
        st.success("정답입니다!")
        st.success("2번 문제 오픈을 위한 비밀번호는 1234입니다")
    