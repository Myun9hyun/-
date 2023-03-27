import streamlit as st
import pandas as pd
import joblib
import pickle
# 모델 불러오기
model_path = "MH/model.pkl"
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# function to predict the outcome
def predict_outcome(team1, team2):
    # create a DataFrame with the data for prediction
    X_test = pd.DataFrame({
        'team1': [team1],
        'team2': [team2]
    })
    
    # predict the outcome using the loaded model
    y_pred = model.predict(X_test)[0]
    
    return y_pred

# set the app title
st.title('NCAA 승률 예측기')

# create input fields for team 1 and team 2
team1 = st.text_input('팀 1')
team2 = st.text_input('팀 2')

# create a button to predict the outcome
if st.button('예측하기'):
    # check if both teams have been entered
    if team1 and team2:
        # call the predict_outcome function
        outcome = predict_outcome(team1, team2)
        st.write(f"{team1} vs {team2} 예측 승률: {outcome:.2f}")
    else:
        st.warning('팀 이름을 입력하세요.')
