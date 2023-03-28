import streamlit as st
import pandas as pd
import joblib

# 모델 불러오기
with open('MH/DecisionTree.pkl', 'rb') as f:
    model = joblib.load(f)

# 입력받기
st.sidebar.title('Input')
df = pd.read_csv('MH/cbb_preprocess.csv')
G = st.sidebar.slider('Number of Games Played', 0, 40, 20)
W = st.sidebar.slider('Number of Wins', 0, 40, 10)
X_DT = df.drop('P_V', axis=1) # 독립변수 (관측값, 피쳐)
X_new = pd.DataFrame({'GP': [G], 'W': [W]})
X_DT = X_DT.append(X_new, ignore_index=True).reset_index(drop=True)
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)
# 예측
prediction = model.predict(X_DT.iloc[-1].values.reshape(1, -1))[0]

# 결과 출력
st.title('Winning Percentage Prediction')
st.write('The predicted winning percentage is:', prediction)
