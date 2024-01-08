import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Mon salaire",
    page_icon="📖",
)
st.title("Tout savoir sur mon salaire")

# Importation de la fiche des salaires
grades = pd.read_csv('App/fiche_grades_et_salaires.csv')
st.write(grades)

# Container pour le renseignement de son grade
with st.container():
    st.subheader("Je renseigne mon grade")
    with st.expander("En savoir plus"):
        st.write("""Lorem Ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
                 ut labore et dolore magna aliqua. Ut enim ad minim veniam ut aliquip ex ea commodo consequat""")
    niveau = st.selectbox('Selectionner votre niveau', grades["Niveau"].drop_duplicates().drop_duplicates())
    echelon = st.selectbox('Selectionner votre échelon', grades.loc[grades['Niveau'] == niveau, 'Echelon'].drop_duplicates().drop_duplicates())

st.divider()

# Container pour renseigner son ancienneté
with st.container():
    st.subheader("Je renseigne mon ancienneté")
    with st.expander("Comment connaitre son ancienneté"):
        st.write("""Lorem Ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
                 ut labore et dolore magna aliqua. Ut enim ad minim veniam ut aliquip ex ea commodo consequat""")
    ancienneté = st.number_input("Entrer un nombre d'année", step=1, format="%i")

st.divider()

# Container pour renseigner son nombre d'heures
with st.container():
    st.subheader("Je renseigne mon nombre d'heures travaillées")
    heures_contractuelles = st.number_input("Entrer le nombre d'heures du contrat", step=1, format="%i")
    with st.expander("Ou retrouver son nombre d'heures ?"):
        st.write("""Lorem Ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
                 ut labore et dolore magna aliqua. Ut enim ad minim veniam ut aliquip ex ea commodo consequat""")
    heures_travaillées = st.number_input("Entrer le nombre d'heures travaillées ce mois", step=1, format="%i")
    taux_horaire = st.checkbox("J'ai travaillé trois mois en continu et je ne suis pas en remplacement")