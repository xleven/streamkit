import streamlit as st


st.set_page_config(page_title="StreamKit · web toolbox")

home_page = """
# StreamKit

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamkit.streamlit.io)

Python toolbox built with Streamlit


## Toolkits

- [x] Datetime toolbox
- [x] QR code playground
- [x] Custom code runner


## License

[MIT License](https://github.com/celevn/streamkit/blob/main/LICENSE)

Copyright © 2022, [Celevn](https://github.com/celevn)
"""

st.markdown(home_page)
