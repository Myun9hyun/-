import streamlit as st
import numpy as np
import joblib

# 모델 로드
model_path = "MH/LRmodel"
model = joblib.load(model_path)

# 승리수, 경기수 입력 받기
st.write("승리수와 경기수를 입력하세요.")
wins = st.slider("승리수", 0, 82, 41)
games = st.slider("경기수", 0, 82, 41)

# 입력값 확인
st.write("입력값:", {"승리수": wins, "경기수": games})

# 모델 예측
inputs = np.array([wins, games])
pred = model.predict(inputs.reshape(1, -1))[0]

# 예측 결과 출력
st.write(f"예측 승률: {pred:.2%}")
