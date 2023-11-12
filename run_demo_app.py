import streamlit as st
import json

from scripts.explanation import explain_process
from scripts.demo import run_demo
from scripts.try_it import run_try_it
from scripts.tips import show_tips

st.set_page_config(
    layout="wide",
    page_title="ZenPrompt: Automatic Prompt Engineering Demo",
    page_icon=":speech_balloon:"
)

with open("./files/demo.json", "r") as f:
    demo_data = json.load(f)


def main_selected():
    """Writes main page content."""
    st.title('	:sparkles: How to prompt?')
    st.write('---')
    st.write(demo_data['main']['intro'])
    st.write(demo_data['main']['structure'])
    st.write(demo_data['main']['features'])


def handle_feature_on_change():
    """Handles sidebar options."""
    if st.session_state.feature_selected == 'Main':
        pass
    elif st.session_state.feature_selected == ':heavy_check_mark: Tips':
        show_tips()
    elif st.session_state.feature_selected == ':pencil: Try it':
        run_try_it()
    elif st.session_state.feature_selected == ':computer: Demo':
        run_demo()
    elif st.session_state.feature_selected == ':books: Explanation':
        explain_process()


def main_view():
    """Main application function."""
    with st.sidebar:
        st.sidebar.title(demo_data['sidebar']['title'])
        st.sidebar.write(demo_data['sidebar']['content'])

        st.sidebar.radio(
            label='Select Page:',
            index=1,
            options=demo_data['sidebar']['options'],
            on_change=handle_feature_on_change,
            key='feature_selected'
        )

        st.markdown(
            "<style> div[role=radiogroup] label:first-of-type {visibility: hidden; height: 0px;}</style>",
            unsafe_allow_html=True,
        )

    if st.session_state.feature_selected == 'Main' or 'feature_selected' not in st.session_state:
        main_selected()


if __name__ == "__main__":
    main_view()
