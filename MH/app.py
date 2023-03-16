import streamlit as st
from streamlit.hashing import _CodeHasher
import SessionState
# SessionState class
class _SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
# function to create session state object
def get_session(key, **kwargs):
    state = _SessionState(**kwargs)
    if hasattr(st.session, key):
        old_state = getattr(st.session, key)
        if old_state:
            state.__dict__.update(old_state.__dict__)
    setattr(st.session, key, state)
    return state
# define session state key
session_state = get_session(key='session_state', button_tab=1)
# button to switch to tab 1
if st.button('Go to Tab 1'):
    session_state.button_tab = 1
# button to switch to tab 2
if st.button('Go to Tab 2'):
    session_state.button_tab = 2
# check which tab to display
if session_state.button_tab == 1:
    st.write('This is Tab 1')
else:
    st.write('This is Tab 2')