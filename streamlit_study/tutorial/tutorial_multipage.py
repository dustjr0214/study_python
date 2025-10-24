"""
streamlit 튜토리얼 - 멀티페이지
streamlit의 공식 문서의 tutorial을 따라서 공부합니다.
streamlit hello의 기본 페이지를 따라 구현
"""


import streamlit as st

st.set_page_config(page_title="hello", page_icon="👋")

st.write("# welcome to streamlit! :tada:")
st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)