# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import joblib
# import numpy as np

# df = pd.read_csv('MH/cbb_preprocess.csv')
# G = df['G']
# W = df['W']
# r1_col1, r1_col2 = st.columns(2)
# G = r1_col1.slider("게임수", 0, 40)
# W = r1_col2.slider("승리수", 0, 40)
# # 전용면적별세대수1 = r1_col3.slider("전용면적별세대수", 1, 1865)

# predict_button = st.button("예측")
# if predict_button:
#         variable1 = np.array([G, W]* 28)
#         model1 = joblib.load('MH/LRmodel.pkl')
#         pred1 = model1.predict([variable1])
#         st.metric("결과: ", pred1[0])
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

# 모델 예측 및 그래프 그리기
x_min = df['G'].min()
x_max = df['G'].max()
x_new = st.slider('G', min_value=x_min, max_value=x_max)
y_new = model.predict([[x_new]])[0]

x = df['G']
y = df['P_V']

plt.plot(x, model.predict(df.drop('P_V', axis=1)), c='blue')
plt.scatter(x_new, y_new, c='red')

st.pyplot()
