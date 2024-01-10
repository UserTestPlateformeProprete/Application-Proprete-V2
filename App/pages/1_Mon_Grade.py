import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(
    page_title="Mon Grade",
    page_icon="📖",
)
st.title("Déterminer son grade")

grades = pd.read_csv('App/fiche_grades_et_salaires.csv')

with st.container(border=True):
    st.write("""Le grade représente un niveau de qualifification et d'autonomie
    au travail.    Il est associé à un niveau de rémunération plus ou moins élevé.""")
    with st.expander("Voir les niveaux de rémunération"):
        st.write(grades)

# debug
echelons = pd.read_csv('App/fiche_grade_et_echelon.csv')
st.write(echelons)

with st.container():
    st.subheader("J'évalue mon niveau d'autonomie")
    niveau_autonomie = st.radio("Choississez le niveau d'autonomie qui vous correspond le plus : ",
                 label_visibility="collapsed",
                 options=echelons["Autonomie"].drop_duplicates(),
                 index=None)

with st.container():
    st.subheader("J'évalue mon niveau de technicité")
    niveau_technicite = st.radio("Choississez le niveau de technicité qui vous correspond le plus : ",
                 label_visibility="collapsed",
                 options=echelons["Technicité"].drop_duplicates(),
                 index=None)

with st.container():
    st.subheader("J'évalue mon niveau de responsabilité")
    niveau_responsabilite = st.radio("Choississez le niveau de responsabilité qui vous correspond le plus : ",
                 label_visibility="collapsed",
                 options=echelons["Responsabilité"].drop_duplicates(),
                 index=None)

if niveau_responsabilite is not None & niveau_technicite is not None & niveau_autonomie is not None:
    with st.container():
        st.subheader("test")
