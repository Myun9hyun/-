import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

# 모델 로드
model = joblib.load('MH/LRmodel.pkl')

# 데이터 로드
df = pd.read_csv('MH/cbb_preprocess.csv')

# x 값 생성
x = df['G']

# 예측값 생성
y_pred = model.predict(x.values.reshape(-1, 1))

# 그래프 그리기
sns.set_style('darkgrid')
plt.figure(figsize=(8, 6))
sns.scatterplot(x=x, y=df['P_V'])
sns.lineplot(x=x, y=y_pred)
plt.xlabel('G')
plt.ylabel('P_V')
plt.title('Linear Regression')
st.pyplot()
