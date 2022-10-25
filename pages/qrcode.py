from ast import Bytes
from io import BytesIO
import streamlit as st

from qrcode import QRCode
from qrcode import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H


st.set_page_config(page_title="StreamKit · web toolbox")

st.header("QR code playgroud")
st.caption("Powered by [python-qrcode](https://github.com/lincolnloop/python-qrcode)")

with st.form("qrconfig"):
    data = st.text_input(label="Data to encode", placeholder="Hello world!")
    version = st.number_input(label="Version", min_value=0, max_value=40,
                              help="size of the QR Code (the smallest, version 1, is a 21x21 matrix), 0 for autofit")
    box_size = st.number_input(label="Box size", min_value=1, max_value=50, value=10, help="how many pixels each “box” of the QR code is")
    border = st.number_input(label="Border width", min_value=4, max_value=10, help="how many boxes thick the border should be")
    err = st.selectbox(label="Error correction level",
                       options=["ERROR_CORRECT_L", "ERROR_CORRECT_M", "ERROR_CORRECT_Q", "ERROR_CORRECT_H"],
                       index=1,
                       help="""
                            ERROR_CORRECT_L ~ About 7% or less errors can be corrected\n
                            ERROR_CORRECT_M ~ About 15% or less errors can be corrected (default)\n
                            ERROR_CORRECT_Q ~ About 25% or less errors can be corrected\n
                            ERROR_CORRECT_H ~ About 30% or less errors can be corrected\n
                        """)
    fcolor = st.color_picker(label="Color to fill", value="#000000")
    bcolor = st.color_picker(label="Color of backgroud", value="#ffffff")
    button = st.form_submit_button("Generate")

if button:
    version = None if version < 1 else version
    qr = QRCode(version=version, error_correction=eval(err), box_size=box_size, border=border)
    bytes = BytesIO()
    qr.add_data(data)
    qr.make(fit=True)
    qr.make_image(
        fill_color=fcolor,
        back_color=bcolor,
    ).save(bytes)
    st.image(bytes)