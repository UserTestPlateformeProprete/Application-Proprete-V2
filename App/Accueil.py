import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Accueil",
    page_icon="🏠",
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
à comprendre directement aux employés concernés par ces soucis. Porté par Julie Lazès, appuyée de Ilona Delouette et 
François-Xavier Devetter, ce projet va passer par les mains deux 2 groupes d'étudiant pour prendre sa forme actuelle.

## Ce que ce site offre :

Notre plateforme met à votre disposition des informations claires, des outils pratiques et des liens vers les ressources
juridiques pouvant vous aider à comprendre et à défendre vos droits. Vous retrouverez ainsi trois calculteurs vous
permettant de retrouver votre qualification, d'estimer votre salaire brut et d'estimer l'impact de l'abattement sur 
votre salaire et votre retraite. De plus, une FAQ essaiera de répondre aux questions les plus importantes et fréquemment
posée.  
Pour utiliser optimalement les outils, nous vous conseillons de vous munir d'une fiche de paie et si possible de votre 
contrat de travail. Nous vous recommandons aussi de parcourir les pages dans l'ordre indiqué par le menu (flèche en haut 
à gauche), les informations récupérés par un calculateur pouvant servir dans le suivant. """)

# ajout des boutons vers les pages du site en parallèle
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
    col1, col2 = st.columns(spec=[0.05, 0.8], gap='small')
    col1.image(logo, width=22)
    col2.write(lien)
    return col1, col2


with (st.expander(label="Qui sommes nous ?")):
    st.markdown("### Ce site a été développé par :")
    paul, alexandre = st.columns(2, gap="large")
    with paul:
        st.image(image='App\img\paul.png', caption="Paul Jourdain")
        st.write("Etudiant en dernière année à l'IMT NE, je m'intéresse à rendre l'informatique plsus durable. J'ai "
                 "rejoint ce projet car je voulais mettre mes compétences au service d'un projet humain.")
        lin_logo_paul, lin_lien_paul = afg_logo_et_lien('App/img/logo-linkedin-icon-1536.png',
                                                        "[@jourdain-paul](www.linkedin.com/in/jourdain-paul)")
        github_logo_paul, github_lien_paul = afg_logo_et_lien('App/img/logo-github.png',
                                                              '[Github](https://github.com/ElPaulJ)')
    with alexandre:
        st.image(image='App/img/Alexandre.png', caption="Alexandre")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore "
                 "et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut.")
        lin_logo_alex, lin_lien_alex = afg_logo_et_lien('App/img/logo-linkedin-icon-1536.png',
                                                        '[@alexandre-pontida](www.linkedin.com/in/alexandre-pontida)')
