import joblib
import numpy as np
import streamlit as st

# 결정트리 모델 불러오기
model_path = "MH/DecisionTree.pkl"
model = joblib.load(model_path)

# Streamlit 앱 설정
st.title('결정트리 모델')
st.write('입력 변수')

# 입력 변수를 위한 슬라이더 추가
x1 = st.slider('X1', 0.0, 1.0, 0.5, 0.01)
x2 = st.slider('X2', 0.0, 1.0, 0.5, 0.01)

# 모델을 사용하여 예측 수행
x = np.array([x1, x2] * 77).reshape(1, -1)
y = model.predict(x)
y = y[0]

# 예측 결과 출력
st.subheader('예측 결과')
st.write('Y:', round(y, 2))
