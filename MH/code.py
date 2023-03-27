import joblib
import numpy as np
import pandas as pd
import streamlit as st

# 랜덤 포레스트 모델 불러오기
model_path = "MH/LRmodel.pkl"
model = joblib.load(model_path)

st.write("LinearRegressor")
# 첫번째 행
r1_col1, r1_col2, r1_col3 = st.columns(3)
경기수 = r1_col1.slider("경기수", 0, 40)
승리수 = r1_col2.slider("승리수", 0, 40)
# 전용면적별세대수1 = r1_col3.slider("전용면적별세대수", 1, 1865)
# 두번째 행
# r2_col1, r2_col2, r2_col3 = st.columns(3)
# 공가수1 = r2_col1.slider("공가수",0,55)
# 지하철_option1 = (0, 1, 2, 3)
# 지하철1 = r2_col2.selectbox("지하철", 지하철_option1)
# 버스1 = r2_col3.slider("버스", 0,20)
# # 세번째 행
# r3_col1, r3_col2, r3_col3 = st.columns(3)
# 단지내주차면수1 = r3_col1.slider("단지내주차면수",13,1798)
# 공급유형_비율1 = r3_col2.slider("공급유형_비율",0,60)
# 지역_비율1 = r3_col3.slider("지역_비율",0,21)
predict_button = st.button("예측")

if predict_button:
        variable1 = np.array([경기수, 승리수]*28)
        # , 전용면적별세대수1, 공가수1, 지하철1, 버스1, 단지내주차면수1, 공급유형_비율1, 지역_비율1
       
        model1 = joblib.load('MH/LRmodel.pkl')
        pred1 = model1.predict([variable1])
        st.metric("결과: ", pred1[0])