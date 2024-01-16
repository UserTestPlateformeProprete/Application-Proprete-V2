import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Accueil",
    page_icon="",
)
st.title("Accueil")

with st.container():
    st.subheader("Comment utiliser ce site?")
    with st.expander("Etape par étape"):
        st.write("""Vous devez renseigner les informations à chaque étape pour obtenir des résultats les plus précis possibles.""")

