import streamlit as st

css = """
h1 {
  color: blue;
  font-size: 36px;
}

p {
  color: red;
  font-size: 18px;
}
"""

st.write(f"<style>{css}</style>", unsafe_allow_html=True)
st.write("<h1>Hello, World!</h1>", unsafe_allow_html=True)
st.write("<p>This is a paragraph.</p>", unsafe_allow_html=True)
