import streamlit as st

st.set_page_config(
    page_title="F.A.Q.",
    page_icon="❓",
    layout="centered",
)
st.title("Foire Aux Questions")

st.empty()

with st.container():
    st.header("Section 1")

    with st.expander("Question 1"):
        st.write("I#m blue")

    with st.expander("Question 2"):
        st.write("I#m blue")

    with st.expander("Question 3"):
        st.write("I#m blue")

st.divider()

with st.container():
    st.header("Section 2")

    with st.expander("Question 1"):
        st.write("I#m blue")

    with st.expander("Question 2"):
        st.write("I#m blue")

    with st.expander("Question 3"):
        st.write("I#m blue")