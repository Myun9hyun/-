import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

model = joblib.load("MH/DecisionTree_drop.pkl")

X = pd.read_csv("MH/cbb_drop.csv")
y = X.pop("target")

feature_importances = pd.Series(model.feature_importances_, index=X.columns)

plt.figure(figsize=(12, 10))
# sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
sns.heatmap(X.iloc[:, sorted_idx].corr(), cmap='coolwarm', annot=True)

st.pyplot()
