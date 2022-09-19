import streamlit as st


st.header("Datatime toolbox")

st.subheader("Delta between 2 dates")
with st.form("datepicker"):
    da = st.date_input("Day 1")
    db = st.date_input("Day 2")
    if st.form_submit_button("Calculate"):
        st.write(da-db)
