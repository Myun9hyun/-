import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

# 모델 불러오기
with open('MH/LRmodel.pkl', 'rb') as f:
    model = pickle.load(f)

# 산점도 그리기
sns.set_style('darkgrid')
plt.figure(figsize=(8, 6))
plt.xlabel('G')
plt.ylabel('P_V')
plt.title('Linear Regression')

# 모델 예측 및 그래프 그리기
x_min = 0
x_max = 40
x_new = st.slider('G', min_value=x_min, max_value=x_max)
y_new = model.predict([[x_new]])[0]

x = list(range(x_min, x_max+1))
y = model.predict([[i] for i in x])

plt.plot(x, y)
plt.scatter(x_new, y_new, c='red')
st.pyplot()
