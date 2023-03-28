import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import numpy as np

# 모델 로드
model = joblib.load('MH/LRmodel.pkl')

# 데이터 로드
df = pd.read_csv('MH/cbb_preprocess.csv')

# x 값 생성
x = df.drop('P_V', axis=1).values

# 예측값 생성
x_77d = np.hstack([x, np.zeros((len(x), 77 - len(x[0])), dtype=x.dtype)])
y_pred = model.predict(x_77d)

# 그래프 그리기
sns.set_style('darkgrid')
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df['G'], y=df['P_V'])
sns.lineplot(x=df['G'], y=y_pred)
plt.xlabel('G')
plt.ylabel('P_V')
plt.title('Linear Regression')
st.pyplot()
