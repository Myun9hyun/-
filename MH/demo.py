# import pandas as pd
# import streamlit as st

# # 데이터프레임을 불러옵니다.
# df = pd.read_csv("https://raw.githubusercontent.com/Myun9hyun/trash/main/MH/Basketball_processing.csv")

# # 체크박스로 선택한 columns 받기
# selected_columns = st.multiselect('Select columns', df.columns)

# # 선택한 columns에 해당하는 index 추출하기
# selected_index = df[df[selected_columns].notna().all(axis=1)].index

# # 선택한 index들을 출력할 데이터프레임 만들기
# selected_df = df.loc[selected_index, selected_columns]

# # 선택한 index들을 출력
# st.write(selected_df)
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
# 데이터 불러오기
df = pd.read_csv("https://raw.githubusercontent.com/Myun9hyun/trash/main/MH/Basketball_processing.csv")

# 체크박스로 선택한 columns 받기
selected_columns = st.multiselect('Select columns', df.columns)

# 선택한 columns에 해당하는 index 추출하기
selected_index = df[df[selected_columns].notna().all(axis=1)].index

# 선택한 index들을 출력할 데이터프레임 만들기
selected_df = df.loc[selected_index, selected_columns]


# 해당 컬럼에 결측값이 있을 경우 0으로 대체
selected_df[col] = selected_df[col].fillna(0)

# 선택한 스탯들을 비교하는 radar chart 그리기
fig = go.Figure()
for col in selected_stats:
    fig.add_trace(go.Scatterpolar(
        r=[selected_df[col].mean()],
        theta=[col],
        fill='toself',
        name=col
    ))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[selected_df[selected_stats].min().min(), selected_df[selected_stats].max().max()]
        )
    ),
    showlegend=True
)
st.plotly_chart(fig, use_container_width=True)

# # radar chart 그리기
# if not selected_df.empty:
#     fig = go.Figure()
#     for col in selected_columns:
#         fig.add_trace(go.Scatterpolar(
#             r=[selected_df[col].mean()],
#             theta=[col],
#             fill='toself',
#             name=col
#         ))
#     fig.update_layout(
#         polar=dict(
#             radialaxis=dict(
#                 visible=True,
#                 range=[selected_df[selected_columns].min().min(), selected_df[selected_columns].max().max()]
#             )
#         ),
#         showlegend=True
#     )
#     st.plotly_chart(fig, use_container_width=True)
# else:
#     st.write("No data selected.")
