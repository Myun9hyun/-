# 필요한 라이브러리 import
import joblib
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import seaborn as sns

##################################################################################
# st.markdown을 통해 전체 틀 고정
st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 90%;
        padding-top: 5rem;
        padding-right: 5rem;
        padding-left: 5rem;
        padding-bottom: 5rem;
    }}
    img{{
    	max-width:40%;
    	margin-bottom:40px;
    }}
</style>
""",
        unsafe_allow_html=True,
    )
##################################################################################
with st.sidebar:
    choose = option_menu("Contents", ["메인페이지", "데이터페이지", "시뮬레이션"],
                         icons=['house', 'kanban', 'person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "4!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )