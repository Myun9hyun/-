import streamlit as st
import pandas as pd
from math import pi
from bokeh.palettes import Category10
from bokeh.plotting import figure

url = "https://raw.githubusercontent.com/Myun9hyun/trash/main/MH/Basketball_processing.csv"

df = pd.read_csv("https://raw.githubusercontent.com/Myun9hyun/trash/main/MH/Basketball_processing.csv", index_col=0)

import streamlit as st
import pandas as pd
from math import pi
from bokeh.palettes import Category10
from bokeh.plotting import figure

# csv 파일 읽어오기
df = pd.read_csv("your_csv_file.csv")

# 선택할 수 있는 옵션 리스트
conf_list = df['CONF'].unique().tolist()
conf_selected = st.sidebar.selectbox("Select Conference", conf_list)

# 선택한 컨퍼런스에 해당하는 행들 추출
filtered_df = df[df['CONF'] == conf_selected]

# 선택할 수 있는 옵션 리스트
columns = filtered_df.columns[3:].tolist()
columns_selected = st.sidebar.multiselect("Select Columns", columns)

# 선택한 컬럼들로 radar chart 그리기
colors = Category10[10]
p = figure(title="Radar Chart", plot_width=500, plot_height=500)

for i, column in enumerate(columns_selected):
    data = filtered_df[column].tolist()
    angles = [n / float(len(columns_selected)) * 2 * pi for n in range(len(columns_selected))]
    angles += angles[:1]
    data += data[:1]
    p.annular_wedge(x=0, y=0, inner_radius=0.2, outer_radius=0.8, start_angle=angles[i], end_angle=angles[i+1], color=colors[i], alpha=0.5)
    p.line(x=data, y=data, color=colors[i], alpha=0.5)
    p.patch(x=data, y=data, color=colors[i], alpha=0.2)

st.bokeh_chart(p, use_container_width=True)
