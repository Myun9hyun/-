import streamlit as st
from PIL import Image
import requests
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import joblib
import xgboost as xgb
import seaborn as sns
from streamlit_option_menu import option_menu
import base64

bg_image = Image.open("MH/image/back.jpg")


# CSS 스타일을 사용하여 배경 이미지를 설정합니다.
st.markdown(
    f"""
    <style>
    body {{
        background-image: url(data:image/jpeg;base64,{base64.b64encode(open(bg_image, "rb").read()).decode()});
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# 이후 Streamlit 앱의 나머지 부분을 정의합니다.




with st.sidebar:
    choice = option_menu("Menu", ["페이지1", "페이지2", "페이지3"],
                         icons=['house', 'kanban', 'bi bi-robot'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "4!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
        "nav-link-selected": {"background-color": "#08c7b4"},
    }
    )
    st.write("💾Team repo")
    st.markdown('<a href="https://github.com/Myun9hyun"><img src="https://badgen.net/badge/icon/github?icon=github&label"></a>', unsafe_allow_html=True)
    st.write("💪Team Notion")
    st.markdown('<a href="https://www.notion.so/DL_PROJECT-82b3fdfbde2e4937b0f9463fce66d056"><img src="https://img.shields.io/badge/Notion-Deep%20Learning-lightgrey"></a>', unsafe_allow_html=True)

if choice == "페이지1":

    tab0, tab1, tab2, tab3 = st.tabs(["🏠 Main", "tab1", "tab2", "tab3"])
    image_path = "MH/image/molu.gif"

        # Streamlit에서 GIF 보여주기
    
   

    with tab0:
        tab0.subheader("팀 이름")
        
        st.write()
        '''
        **⬆️위의 탭에 있는 메뉴를 클릭해 선택하신 항목을 볼 수 있습니다!⬆️**
        '''
        # st.image("https://cdn.pixabay.com/photo/2020/09/02/04/06/man-5537262_960_720.png", width=700)
        st.image(image_path, caption='GIF', width=500)
        '''
        ---

        ### Team 💪

        | 이름 | 역할 분담 | 그 외 역할 | 딥러닝모델링 | GitHub |
        | :---: | :---: | :---: | :---: | :---: |
        | 서상원 |  |  |  |[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/tkd8973)|
        | 조성훈 |  |  |  |[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/)|
        | 김명현 |  |  |  |[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/Myun9hyun)|
        | 강성욱 |  |  |  |[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/JoySoon)|
        ---
        
        '''
    with tab1:
        tab1.subheader("탭1")
        tab1.write()
        '''
        ### 자료 설명
        '''
    with tab2:
        tab2.subheader("탭2")
        st.write()
        '''
        ### 탭2
        '''

    with tab3:
        tab3.subheader("탭3")
        st.write()
        '''
        ### 탭3
        '''
elif choice == "페이지2":
    st.subheader("페이지2")
    
        

elif choice == "페이지3":
    st.subheader("페이지3")
    
    