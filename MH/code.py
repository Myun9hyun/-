import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the data
df = pd.read_csv('MH/cbb_preprocess.csv')

# Train the linear regression model
# X = df['P_V'].values.reshape(-1, 1)
# y = df['P_V'].values
X = df.drop('P_V', axis=1).values.reshape(-1, 1) # 독립변수 (관측값, 피쳐)
y = df['P_V'].values # 종속변수 (예측값, 라벨)
lr = LinearRegression()
lr.fit(X, y)

# Draw the scatter plot
sns.set_style('darkgrid')
plt.figure(figsize=(8, 6))
plt.xlabel('G')
plt.ylabel('P_V')
plt.title('Linear Regression')
plt.scatter(X, y)

# Draw the regression line
x_range = range(df['G'].min(), df['G'].max() + 1)
y_range = lr.predict([[x] for x in x_range])
plt.plot(x_range, y_range, c='red')

# Display the plot using Streamlit
st.pyplot()
