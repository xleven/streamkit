import streamlit as st
from streamlit_ace import st_ace


st.header("Custom code runner")

default = """# Write costom code here

# Notes:
# 1. remember to import needed modules
# 2. use st.write() instead of print() to display/debug
# 3. correct your syntax error before running

st.write("hello world")
"""
code = st_ace(value=default, language="python")

exec(code)
