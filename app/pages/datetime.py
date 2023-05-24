import streamlit as st
from datetime import datetime


st.set_page_config(page_title="StreamKit · web toolbox")

st.header("Datatime toolbox")

st.subheader("Delta between 2 dates")
with st.form("datepicker"):
    da = st.date_input("Day 1")
    db = st.date_input("Day 2")
    if st.form_submit_button("Calculate"):
        st.write(da-db)

st.subheader("Timestamp Converter")
with st.form("timestamp"):
    st.write("timestamp to datetime")
    ts1 = st.text_input("timestamp in senconds", value=1666666666)
    if st.form_submit_button("Convert"):
        try:
            ts1 = int(float(ts1))
        except:
            st.error("Error: please check your input")
        else:
            dt1 = datetime.fromtimestamp(ts1)
            st.write(dt1)
with st.form("datetiem"):
    st.write("datetime to timestamp")
    date = st.date_input("date")
    time = st.time_input("time")
    if st.form_submit_button("Convert"):
        dt2 = datetime.combine(date, time)
        ts2 = datetime.timestamp(dt2)
        st.write(ts2)