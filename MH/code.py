import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

# 데이터 불러오기
df = pd.read_csv('MH/cbb_preprocess.csv')
X = df.drop('P_V', axis=1) # 독립변수 (관측값, 피쳐)
st.write(X.isna().sum())
st.write(len(X.columns))
# y = df['P_V'] # 종속변수 (예측값, 라벨)

# 모델 불러오기
with open('MH/LRmodel.pkl', 'rb') as f:
    model = joblib.load(f)

# 예측값 계산
df['predicted'] = model.predict(X)

# 산점도 그리기
sns.set_style('darkgrid')
plt.figure(figsize=(8, 6))
# plt.xlabel('P_V')
# plt.ylabel('predicted')
# plt.title('Linear Regression')

# sns.scatterplot(df['P_V'], df['predicted'])
sns.scatterplot(x = 'P_V', y='predicted', data=df)
st.pyplot()
