import joblib
import numpy as np
import pandas as pd
import streamlit as st

# 랜덤 포레스트 모델 불러오기
model_path = "MH/LRmodel.pkl"
model = joblib.load(model_path)

st.write("LinearRegressor")
# 첫번째 행
r1_col1, r1_col2 = st.columns(2)
경기수 = r1_col1.slider("경기수", 0, 40)
승리수 = r1_col2.slider("승리수", 0, 40)

predict_button = st.button("예측")

if predict_button:
        variable1 = np.array([경기수, 승리수]*28)
        model1 = joblib.load('MH/LRmodel.pkl')
        pred1 = model1.predict([variable1])
        st.metric("결과: ", pred1[0])