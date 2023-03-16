import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


option = st.selectbox(
    'How would you like to be contacted?',
    ('연령대별 구매 카테고리', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)


