# import streamlit as st
# import pickle
# import pickle

# # with open('model.pkl', 'rb') as f:
# #     model = pickle.load(f)

# # 모델 불러오기
# model_path = "MH/model.pkl"

# with open(model_path, 'rb') as f:
#     model = pickle.load(f)

# st.title('Linear Regression Model')

# # create sidebar with input parameters
# st.sidebar.header('Input Parameters')
# x = st.sidebar.slider('X', 0.0, 10.0, 5.0, 0.1)

# # use model to make prediction
# prediction = model.predict(x)

# y = model.prediction([[x]])

# # prediction = model.predict(x)
# # show prediction result
# st.subheader('Prediction Result')
# st.write('Y:', y[0])

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
x = st.slider('X', 0.0, 10.0, 5.0, 0.1)

# use model to make prediction
x = np.array([x]*77).reshape(1, -1)  # 입력값의 차원을 맞춰줍니다.
y = model.predict(x)

# show prediction result
st.subheader('Prediction Result')
st.write('Y:', y[0])
