import os
import streamlit.web.bootstrap
import streamlit.runtime.scriptrunner.magic_funcs


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    
    flag_options = {
        "server.port": 8501,
        "global.developmentMode": False,
    }

    streamlit.web.bootstrap.load_config_options(flag_options)
    streamlit.web.bootstrap.run(
        "./app/home.py",
        "streamlit run",
        [],
        flag_options,
    )
