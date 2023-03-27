import streamlit as st
import pandas as pd
import pickle
import numpy as np
# 모델 불러오기
model_path = "MH/model.pkl"
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Set the title of the web app
st.title('NCAA Outcome Predictor')

# Add a short description
st.write('Enter the win percentage of the two teams to predict the outcome of the NCAA game')

import numpy as np

def predict(team_1, team_2):
    team_1_stats = stats_df[stats_df['Team'] == team_1]
    team_2_stats = stats_df[stats_df['Team'] == team_2]
    data = pd.concat([team_1_stats, team_2_stats], axis=1).T.drop(['Team'], axis=1)
    data = np.array(data).reshape(1, -1) # 입력 데이터를 (1, n) 크기의 2차원 배열로 변환
    pred = model.predict(data)
    return pred[0]

# Add two input boxes for team win percentage
team1 = st.number_input('Team 1 Win Percentage', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
team2 = st.number_input('Team 2 Win Percentage', min_value=0.0, max_value=1.0, value=0.5, step=0.01)

# Add a button to make predictions
if st.button('Predict'):
    # Create a DataFrame with the input data
    data = pd.DataFrame({'Team1_WinPercentage': [team1], 'Team2_WinPercentage': [team2]})
    data = data.values.reshape(1, -1)

    # Make the prediction
    prediction = model.predict(data)[0]
    
    # Display the prediction
    if prediction == 0:
        st.write('Team 1 Wins!')
    else:
        st.write('Team 2 Wins!')
