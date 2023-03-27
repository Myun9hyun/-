import streamlit as st
import pickle
import numpy as np

# 모델 불러오기
model_path = "MH/model.pkl"

with open(model_path, 'rb') as f:
    model = pickle.load(f)

st.title('Linear Regression Model')

# create sidebar with input parameters
# st.sidebar.header('Input Parameters')
st.write('Input Parameters')
# x = st.sidebar.slider('X', 0.0, 10.0, 5.0, 0.1)
x = st.slider('X', 0.0, 1.0, 0.5, 0.01)

# use model to make prediction
x = np.array([x]*77).reshape(1, -1)  # 입력값의 차원을 맞춰줍니다.
y = model.predict(x)

# show prediction result
st.subheader('Prediction Result')
st.write('Y:', y[0])
