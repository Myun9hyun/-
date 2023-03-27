import streamlit as st
import pandas as pd
import numpy as np
import pickle

# 저장된 모델 파일을 로드합니다.
model_path = "MH/model.pkl"
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# 사용자가 입력한 경기수와 승리경기수를 기반으로 승률을 예측합니다.
def predict_win_rate(wins, games):
    x = np.array([[wins, games]])  # 입력값의 차원을 맞춰줍니다.
    win_rate = model.predict(x)
    return win_rate[0]



# Streamlit 앱을 구성합니다.
def main():
    st.title("NCAA 농구 승률 예측기")
    st.write("이 앱은 NCAA 농구 팀의 승률을 예측합니다.")
    st.write("사용자는 팀의 경기수와 승리경기수를 입력해야 합니다.")
    
    # 사용자 입력 폼을 구성합니다.
    games = st.slider("경기수", 0, 40, 20)
    wins = st.slider("승리경기수", 0, 40, 10)

    # 예측 결과를 표시합니다.
    if st.button("예측하기"):
        # x = np.array([wins, games]*38).reshape(38,2)
        # win_rate = model.predict(x)
        x = np.array([wins, games]).reshape(1, -1)  # 입력값의 차원을 맞춰줍니다.
        win_rate = predict_win_rate(wins, games)
        st.write(f"예상 승률: {win_rate:.2%}")

if __name__ == "__main__":
    main()
