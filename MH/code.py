import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

# 데이터 불러오기
df = pd.read_csv('MH/cbb_preprocess.csv')

# 모델 불러오기
with open('MH/LRmodel.pkl', 'rb') as f:
    model = joblib.load(f)

# 예측값 계산
df['predicted'] = model.predict(df[['feature1', 'feature2', 'feature3']])

# 산점도 그리기
sns.set_style('darkgrid')
plt.figure(figsize=(8, 6))
plt.xlabel('feature1')
plt.ylabel('predicted')
plt.title('Linear Regression')

plt.scatter(df['feature1'], df['predicted'])
st.pyplot()
