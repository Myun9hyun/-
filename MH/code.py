import pickle
import numpy as np
import streamlit as st

# 선형회귀 모델 불러오기
model_path = "MH/model.pkl"
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Streamlit 앱 설정
st.title('선형회귀 모델')
st.write('입력 변수')

# 입력 변수를 위한 슬라이더 추가
x = st.slider('X', 0.0, 1.0, 0.5, 0.01)
x = np.array([x]*77).reshape(1, -1)  # 입력값의 차원을 맞춰줍니다.
y = model.predict(x)
y = y * 100
y = y.round(2)
# 모델을 사용하여 예측 수행
x = np.array(x).reshape(1, -1)
y = model.predict(x)

# 예측 결과 출력
st.subheader('예측 결과')
st.write('Y:', y[0])
