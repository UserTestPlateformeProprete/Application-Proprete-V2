import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Accueil",
    page_icon="🏠",
    initial_sidebar_state="expanded"
)

# Introduction au site
st.markdown("""# Bienvenue sur la Plateforme d’Aide aux Agents d’Entretien !

Nous sommes ici pour vous accompagner et vous donner les outils nécessaires pour comprendre et défendre vos droits dans 
le secteur de la propreté.

## Notre Mission :

Le projet a pour objectif de résoudre les problèmes liés à la méconnaissance et aux abus entourant la convention 
collective du secteur de la propreté. Nous avons observé que les employés à temps partiel dans ce domaine sont 
fréquemment confrontés à des erreurs de paie, au non-respect de leur droit à la requalification, etc.

## Pourquoi nous existons :

Suite à ce constat, un projet est né au sein de l'IMT Nord Europe pour apporter l'information de façon claire et facile
à comprendre directement aux employés concernés par ces soucis. Ce projet est porté par une équipe 
d'enseignants-chercheurs de l'IMT NE et de l'université de Lille : Julie Lazès, Ilona Delouette et François-Xavier 
Devetter et développé par des étudiants de l'IMT NE : Alexandre Pontida et Paul Jourdain

## Ce que ce site offre :

Notre plateforme met à votre disposition des informations claires, des outils pratiques et des liens vers les ressources
juridiques pouvant vous aider à comprendre et à défendre vos droits. Vous retrouverez ainsi trois calculteurs vous
permettant de retrouver votre qualification, d'estimer votre salaire brut et d'estimer l'impact de l'abattement sur 
votre salaire et votre retraite. De plus, une FAQ essaiera de répondre aux questions les plus importantes et fréquemment
posée.  
Pour utiliser optimalement les outils, **nous vous conseillons de vous munir d'une fiche de paie et si possible de votre 
contrat de travail**. Nous vous recommandons aussi de parcourir les pages dans l'ordre indiqué par le menu (flèche en 
haut à gauche), les informations récupérés par un calculateur pouvant servir dans le suivant.""")

# ajout des boutons vers les pages du site en parallèle (si assez d'espace disponible)
col1, col2, col3, col4 = st.columns(4)

if col1.button(label="Vers le calculateur de classe"):
    st.switch_page("pages/1_🙋‍♀️_Ma_Classe.py")

if col2.button(label="Vers l'estimateur de salaire brut"):
    st.switch_page("pages/2_💰_Mon_Salaire_Brut.py")

if col3.button(label="Vers l'estimateur d'abattement"):
    st.switch_page("pages/3_⚖️_L'abattement_ou_DFS.py")

if col4.button(label="Vers les réponses de la FAQ"):
    st.switch_page("pages/4_❓_FAQ.py")


# fonction d'affichage pour les profils
def afg_logo_et_lien(logo, lien):
    col1, col2 = st.columns(spec=[0.05, 0.95], gap='small')
    try:
        col1.image(logo, width=22)
    except:
        st.write("Image perdue")
    col2.write(lien)
    return col1, col2


with (st.expander(label="Qui sommes nous ?")):
    st.markdown("### Ce site a été développé par :")
    auteurs1, auteurs2 = st.columns(2, gap="large")
    with auteurs1:
        # Paul
        with st.container():
            try:
                st.image(image='App/img/Paul.png', caption="Paul Jourdain")
            except:
                st.write("Image perdue")
            st.write("Etudiant en dernière année à l'IMT NE, je m'intéresse à rendre l'informatique plus durable. J'ai"
                     " rejoint ce projet car je voulais mettre mes compétences au service d'un projet humain.")
            lin_logo_paul, lin_lien_paul = afg_logo_et_lien('App/img/logo-linkedin-icon-1536.png',
                                                            "[@jourdain-paul](www.linkedin.com/in/jourdain-paul)")
            github_logo_paul, github_lien_paul = afg_logo_et_lien('App/img/logo-github.png',
                                                                  '[Github](https://github.com/ElPaulJ)')
    with auteurs2:
        # Alexandre
        with st.container():
            try:
                st.image(image='App/img/Alexandre.png', caption="Alexandre Pontida")
            except:
                st.write("Image perdue")
            st.write("Je suis aussi étudiant en dernière année à IMT NE,  dans la partie Matériaux de l’école. Étant de"
                     " nature curieuse, ce projet m’a permis de développer mes connaissances en informatique et "
                     "d’apprendre de très nombreuses connaissances sur les droits des travailleurs.")
            lin_logo_alex, lin_lien_alex = afg_logo_et_lien('App/img/logo-linkedin-icon-1536.png',
                                                            '[@alexandre-pontida](www.linkedin.com/in/alexandre-'
                                                            'pontida)')
