import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(
    page_title="La déduction forfaitaire spécifique",
    page_icon="📖",
)
st.title("La déduction forfaitaire spécifique, suis-je gagnant ?")

with st.container(border=True):
    st.subheader("C'est quoi la déduction forfaitaire spécifique ?")
    st.write("""La déduction forfaitaire spécifique (DFS) ou abattement permet d'augmenter son salaire en diminuant le 
    montant prélevé pour les charges sociales. Mais attention car cela implique donc aussi de diminuer le 
    montant pris en compte pour la retraite. Ainsi il est important de peser l'importance de cette diminution de 
    retraite lorsque l'on vous propose d'utiliser la DFS.    
    Il ne sera plus possible de faire de la déduction forfaitaire spécifique après 2029.
    Cet outil est là pour aider à visualiser les gains sur son salaire mais aussi les pertes sur sa future retraite.
    """)

smic = pd.read_csv("App/data/fiche_coefficient_inflation_revalorisation_smic.csv", sep=";")

a_abattement = st.checkbox("Je profite de l'abattement")

#Container départ à la retraite
a_retraite = st.checkbox("Je partirai à la retraite avant 2029")

if a_abattement:
    with st.container():
        st.subheader("Je renseigne l'année depuis laquelle je profite de l'abattement ")
        with st.expander("Qu'est-ce que le nombre d'année cotisé?"):
            st.write("""C'est le nombre d'année où vous avez cotisé pour votre retraite, vous aurez donc une retraite plus élevée.""")
        annees_cotisees = st.number_input("Entrer l'année", step=1, format="%i")

with st.container():
    smic['Année'] = pd.to_datetime(smic['Année'], format='%Y')
    ecart = st.slider("Quel écart aviez vous avec le SMIC en pourcentage ?", value=100)
    temps_de_travail = st.number_input("temps de travail moyen mensuel", value=100)
    smic['Smic'] = smic['Smic'] * temps_de_travail
    smic["salaire"] = smic['Smic'] * (1 + ecart/100)
    st.write("le smic valait :", smic.head(5))