import streamlit as st
import pandas as pd
import joblib

# 모델 불러오기
with open('MH/DecisionTree.pkl', 'rb') as f:
    model = joblib.load(f)

# 입력받기
st.sidebar.title('Input')
games_played = st.sidebar.slider('Number of Games Played', 0, 40, 20)
wins = st.sidebar.slider('Number of Wins', 0, 30, 10)

# 예측
df = pd.read_csv('MH/cbb_preprocess.csv')
data = {'G': df['G'], 'W': df['W']}
df2 = pd.DataFrame(data)
prediction = model.predict(df2)[0]

# 결과 출력
st.title('Winning Percentage Prediction')
st.write('The predicted winning percentage is:', prediction)
