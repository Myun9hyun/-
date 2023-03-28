import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import numpy as np

# 데이터 불러오기
df = pd.read_csv('MH/cbb_preprocess.csv')

# 모델 불러오기
with open('MH/LRmodel.pkl', 'rb') as f:
    model = joblib.load(f)

# 산점도 그리기
sns.set_style('darkgrid')
plt.figure(figsize=(8, 6))
plt.xlabel('G')
plt.ylabel('P_V')
plt.title('Linear Regression')

# 입력값 받기
G = st.slider('G', min_value=0, max_value=40, value=20)
W = st.slider('W', min_value=0, max_value=40, value=20)

# 입력값 변환
input_values = np.zeros((1, 56))
input_values[0, 0] = G
input_values[0, 1] = W

# 모델 예측 및 그래프 그리기
pred = model.predict(input_values)[0]
st.metric('결과', pred)

x_min = 0
x_max = 40
x_new = G
y_new = pred

x = list(range(x_min, x_max+1))
input_values = np.zeros((x_max+1, 56))
input_values[:, 0] = x
input_values[:, 1] = W
y = model.predict(input_values)

plt.plot(x, y)
plt.scatter(x_new, y_new, c='red')
st.pyplot()
