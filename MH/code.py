import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 데이터 로드
df = pd.read_csv('MH/cbb_preprocess.csv')

# x, y 변수 선택
x = df[['G']] # 독립변수 (관측값, 피쳐)
y = df['P_V']

# 모델 훈련
model = LinearRegression()
model.fit(x.values.reshape(-1, 1), y)

# 산점도 그리기
sns.set_style('darkgrid')
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(x=x, y=y, ax=ax)
sns.lineplot(x=x, y=model.predict(x.values.reshape(-1, 1)), ax=ax)
plt.xlabel('G')
plt.ylabel('W')
plt.title('Linear Regression')
st.pyplot(fig)

# 모델 예측
x_new = st.slider('W', min_value=0, max_value=40)
y_new = model.predict([[x_new]])[0]
st.write(f'예측 결과: {y_new:.2f}')
