import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

# # 모델 불러오기
# with open('MH/LRmodel.pkl', 'rb') as f:
#     model = joblib.load(f)

# # 산점도 그리기
# sns.set_style('darkgrid')
# plt.figure(figsize=(8, 6))
# plt.xlabel('G')
# plt.ylabel('W')
# plt.title('Linear Regression')

# # 모델 예측 및 그래프 그리기
# x_min = 0
# x_max = 40
# x_new = st.slider('G', min_value=x_min, max_value=x_max)
# x_new_56dim = [0]*56  # 56차원 벡터 생성
# x_new_56dim[0] = x_new  # 입력값 할당
# y_new = model.predict([x_new_56dim])[0]

# x = list(range(x_min, x_max+1))
# x_56dim = [[i] + [0]*55 for i in x]  # 56차원 벡터 생성
# y = model.predict(x_56dim)

# plt.plot(x, y)
# plt.scatter(x_new, y_new, c='red')
# st.pyplot()

# 첫번째 행
df = pd.read_csv('MH/cbb_preprocess.csv')
G = df['G']
W = df['W']
r1_col1, r1_col2 = st.columns(2)
G = r1_col1.slider("게임수", 0, 40)
W = r1_col2.slider("승리수", 0, 40)
# 전용면적별세대수1 = r1_col3.slider("전용면적별세대수", 1, 1865)

predict_button = st.button("예측")
if predict_button:
        variable1 = np.array([G, W])
        model1 = joblib.load('MH/LR_model.pkl')
        pred1 = model1.predict([variable1])
        st.metric("결과: ", pred1[0])
