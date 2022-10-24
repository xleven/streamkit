import streamlit as st
from datetime import datetime


st.header("Datatime toolbox")

st.subheader("Delta between 2 dates")
with st.form("datepicker"):
    da = st.date_input("Day 1")
    db = st.date_input("Day 2")
    if st.form_submit_button("Calculate"):
        st.write(da-db)

st.subheader("Timestamp Converter")
tab1, tab2 = st.tabs(["timestamp to datetime", "datetime to timestamp"])
with tab1:
    ts = st.text_input("timestamp in senconds", value=datetime.now().timestamp())
    try:
        ts = float(ts)
    except:
        st.error("Error: please check your input")
    else:
        dt = datetime.fromtimestamp(ts)
        st.write(dt)
with tab2:
    with st.form("datetiem"):
        date = st.date_input("date")
        time = st.time_input("time")
        if st.form_submit_button("Convert"):
            dt = datetime.combine(date, time)
            ts = datetime.timestamp(dt)
            st.write(ts)