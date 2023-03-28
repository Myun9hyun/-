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

# # 데이터 불러오기
# df = pd.read_csv('MH/cbb_preprocess.csv')

# # 모델 불러오기
# with open('MH/LRmodel.pkl', 'rb') as f:
#     model = joblib.load(f)

# # 모델 예측
# x = np.array(df['G'])
# y = np.array(df['P_V'])
# y_pred = model.predict(np.array([x,y]*28).T)

# # 산점도 그리기
# sns.set_style('darkgrid')
# plt.figure(figsize=(8, 6))
# plt.xlabel('G')
# plt.ylabel('P_V')
# plt.title('Linear Regression')
# plt.scatter(x, y)
# plt.plot(x, y_pred, color='red')

# # streamlit에서 그래프 출력
# st.pyplot()

####################################################################

# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import joblib
# import numpy as np

df = pd.read_csv('MH/cbb_preprocess.csv')

# 예측을 위한 56개 feature 생성
features = [f'G_{i}' for i in range(1, 29)] + [f'W_{i}' for i in range(1, 29)]
variables = pd.DataFrame(np.zeros((1, 56)), columns=features)

# 게임수와 승리수 입력 받기
r1_col1, r1_col2 = st.columns(2)
for i in range(28):
    variables[f'G_{i+1}'] = r1_col1.slider(f"G_{i+1}", 0, 40)
    variables[f'W_{i+1}'] = r1_col2.slider(f"W_{i+1}", 0, 40)

predict_button = st.button("예측")
if predict_button:
    # 모델 불러오기
    with open('MH/LRmodel.pkl', 'rb') as f:
        model = joblib.load(f)

    # 모델 예측
    pred = model.predict(variables)

    # 예측값 시각화
    sns.set_style('darkgrid')
    plt.figure(figsize=(8, 6))
    plt.xlabel('G')
    plt.ylabel('P_V')
    plt.title('Linear Regression')

    x = range(len(pred))
    y = pred

    plt.plot(x, y)
    st.pyplot()
