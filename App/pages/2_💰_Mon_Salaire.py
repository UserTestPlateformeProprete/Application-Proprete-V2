import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Mon salaire",
    page_icon="📖",
)
st.title("Tout savoir sur mon salaire")

# Importation de la fiche des salaires
grades = pd.read_csv('App/fiche_grades_et_salaires.csv')

#Inscription en dur des niveaux de prime  d'ancienneté
primes = [[4, 2], [6, 3], [8, 4], [10, 5], [15, 5.5], [20, 6]]

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
    st.subheader("Je renseigne mon nombre d'heures travaillées mensuelles")
    heures_contractuelles = st.number_input("Entrer le nombre d'heures mensuelles du contrat", step=1, format="%i")
    with st.expander("Ou retrouver son nombre d'heures ?"):
        st.write("""Lorem Ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
                 ut labore et dolore magna aliqua. Ut enim ad minim veniam ut aliquip ex ea commodo consequat""")
    heures_travaillées = st.number_input("Entrer le nombre d'heures travaillées ce mois", step=1, format="%i")
    est_taux_horaire_B = st.checkbox("J'ai travaillé trois mois en continu et je ne suis pas en remplacement")

st.divider()

# Container pour afficher le salaire
with (st.container()):
    st.subheader("Bilan")

    if est_taux_horaire_B:
        base = float(grades.loc[(grades["Niveau"] == niveau) & (grades["Echelon"] == echelon), 'Taux Horaire B'])
    else: base = float(grades.loc[(grades["Niveau"] == niveau) & (grades["Echelon"] == echelon), 'Taux Horaire A'])
    st.write("Mon taux horaire est", base, "€/heure")

    salaire_contractuel = base * min(heures_travaillées, heures_contractuelles)
    st.write("Mon salaire minimal brut sur mes heures contractuelles est : ", round(salaire_contractuel,2), "€")

    heures_complementaires_maj_11 = min(max(heures_travaillées - heures_contractuelles, 0), 0.1 * heures_contractuelles)
    prime_heures_complémentaires_maj_11 = base * 1.11 * heures_complementaires_maj_11
    st.write("J'ai ", heures_complementaires_maj_11, "heures complémentaire majorées à 11%, soit un revenu de : ", round(prime_heures_complémentaires_maj_11,2), "€")

    heures_complementaire_maj_25 = min(max(heures_travaillées - (heures_contractuelles + heures_contractuelles * 0.1),0), 1/3 * heures_contractuelles - 0.1 * heures_contractuelles)
    prime_heures_complementaire_maj_25 = base * 1.25 * heures_complementaire_maj_25
    st.write("J'ai ", heures_complementaire_maj_25, "heures complémentaire majorées à 25%, soit un revenu de : ", round(prime_heures_complementaire_maj_25,2), "€")

    # Determine le niveau d'ancienneté
    niveau_prime_ancienneté = 0
    if ancienneté > 3:
        for prime in reversed(primes) :
            if ancienneté >= prime[0]:
                niveau_prime_ancienneté = prime[1]
                break
    prime_ancienneté = niveau_prime_ancienneté/100*salaire_contractuel
    st.write("Ma prime d'ancienneté me rapporte ", round(prime_ancienneté,2),"€")

    salaire_total = salaire_contractuel + prime_heures_complémentaires_maj_11 + prime_heures_complementaire_maj_25 + prime_ancienneté
    st.write("Mon salaire minimum brut est donc de :", round(salaire_total,2), "€")


