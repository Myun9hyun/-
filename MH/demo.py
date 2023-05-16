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


answer1 = "안녕"

st.write("만나서 반가울때 하는 인사는?")
quiz = st.text_input("만나서 반가울때 하는 인사는?")
if quiz == answer1:
    st.success("정답입니다! 2번 문제 오픈을 위한 비밀번호는 1234입니다")