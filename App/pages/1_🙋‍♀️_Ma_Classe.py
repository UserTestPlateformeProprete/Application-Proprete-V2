import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(
    page_title="Ma classe",
    page_icon="📖",
)
st.title("Vérifier sa classe")

# Import des données pre-requises pour les salaires
niveau_remuneration = pd.read_csv('App/data/fiche_classes_et_salaires.csv')
# st.write(classes)

# Import des données pre-requises pour classes
data_echelons = pd.read_csv('App/data/fiche_niveau_et_echelon.csv')
# st.write(data_echelons)

# Initialisation du résultat dans le session state
if 'qualification' not in st.session_state:
    st.session_state['qualification'] = None

# Conteneur intro explicative
with st.container(border=True):
    st.write("""La qualification ou  classe représente la combinaison d'un niveau de technicité, d'autonomie et de 
    responsabilité au travail. Il est constitué d'un niveau et d'un échelon marquant la progression au sein de ce 
    niveau. Il est associé à un niveau de rémunération plus ou moins élevé.    
    [Vers la convention : les grilles de classification](
    https://www.legifrance.gouv.fr/conv_coll/article/KALIARTI000047082593#KALIARTI000047082593)""",
             unsafe_allow_html=True)
    with st.expander("Voir les niveaux de rémunération"):
        st.write("""Les niveaux de rémunération suivant sont extrait directement de l'[avenant relatif aux grilles 
        tarifaires de la conventation propreté](https://www.legifrance.gouv.fr/conv_coll/article/KALIARTI000046226073#KALIARTI000046226073)
        . Les grilles présentent un taux horaire A et B. Le taux horaire B concerne les personnes 
        ayant au moins trois mois d'ancienneté, dont le contrat ne concerne pas une mission de remplacement et qui ont plusieurs rôles dans l'entreprise.
        Cela peut être par exemple, s'occuper des missions classiques demandé aux agents d'entretien, mais avoir en plus de celles-ci le gardiennage des clés, la fermeture du portail...
        Pour plus de renseignements, vous pouvez consulter la FAQ pour trouver une liste de contact utile.""")
        st.write(niveau_remuneration)

st.write("""Nous vous proposons deux outils pour vérifier votre classe :     
        - Premièrement, cela peut-etre fait avec une auto-évaluation des vos niveaux de compétences et,    
        - en cas de difficulté, le deuxième outil vous demande simplement de choisir
        le métier le plus proche du vôtre (cliquer sur 'En comparant mon métier').""")

# Séparation en deux tabs
tab1, tab2 = st.tabs(["Avec mon niveau de compétence", "En comparant mon métier"])

# Tab1 pour l'auto-évaluation de ses compétences
with (tab1):
    # Conteneur d'evaluation de son autonomie
    with (st.container()):
        st.subheader("J'évalue mon niveau d'autonomie")
        # Affichage des options
        niveau_autonomie = st.radio("Choississez le niveau d'autonomie qui vous correspond le plus : ",
                                    label_visibility="collapsed",
                                    options=data_echelons["Autonomie"].drop_duplicates(),
                                    index=None,
                                    captions=" ")
        # Affichage des niveaux de classe correspondants après selection d'une option
        if niveau_autonomie is not None:
            nca = data_echelons.loc[
                data_echelons["Autonomie"] == niveau_autonomie, ["Niveau", "Échelon"]]
            for niveau in nca.get("Niveau").drop_duplicates():
                text = "Mon niveau d'autonomie est requis au niveau :blue[" + niveau + "] pour les échelons :\n"
                for echelon in nca.loc[nca["Niveau"] == niveau, "Échelon"]:
                    text += "- :blue[" + echelon + "]\n"
                st.write(text)

    # Conteneur d'evaluation de sa technicité
    with st.container():
        st.subheader("J'évalue mon niveau de technicité")
        # Affichage des options
        niveau_technicite = st.radio("Choississez le niveau de technicité qui vous correspond le plus : ",
                                     label_visibility="collapsed",
                                     options=data_echelons["Technicité"].drop_duplicates(),
                                     index=None,
                                     captions=" ")
        # Affichage des niveaux de classe correspondants après selection d'une option
        if niveau_technicite is not None:
            nct = data_echelons.loc[
                data_echelons["Technicité"] == niveau_technicite, ["Niveau", "Échelon"]]
            for niveau in nct.get("Niveau").drop_duplicates():
                text = "Mon niveau technique est requis au niveau :blue[" + niveau + "] pour le(s) échelon(s) :\n"
                for echelon in nct.loc[nct["Niveau"] == niveau, "Échelon"]:
                    text += "- :blue[" + echelon + "]\n"
                st.write(text)

    # Conteneur d'evaluation de son niveau de responsabilité
    with st.container():
        st.subheader("J'évalue mon niveau de responsabilité")
        # Affichage des options
        niveau_responsabilite = st.radio("Choississez le niveau de responsabilité qui vous correspond le plus : ",
                                         label_visibility="collapsed",
                                         options=data_echelons["Responsabilité"].drop_duplicates(),
                                         index=None,
                                         captions=" ")
        # Affichage des niveaux de classe correspondants après selection d'une option
        if niveau_responsabilite is not None:
            ncr = data_echelons.loc[
                data_echelons["Responsabilité"] == niveau_responsabilite, ["Niveau", "Échelon"]]
            for niveau in ncr.get("Niveau").drop_duplicates():
                text = "Mon niveau de responsabilité est requis au niveau :blue[" + niveau + "] pour le(s) échelon(s) :\n"
                for echelon in ncr.loc[ncr["Niveau"] == niveau, "Échelon"]:
                    text += "- :blue[" + echelon + "]\n"
                st.write(text)

    st.divider()

    # Conteneur du bilan
    with (st.container()):
        st.header("Bilan")

        # Disclaimer
        with st.container(border=True):
            st.write("""
            Ce calculateur est fourni à titre informatif seulement, il ne remplace pas les conseils professionnels, et 
            il est donc de la responsabilité de l'utilisateur en cas de d'irrégularité détectée de rencontrer un professionnel
            pour qu'il puisse constater.
            """)

        classe_pretendu = None
        if niveau_responsabilite is not None and niveau_technicite is not None and niveau_autonomie is not None:
            index_classe_pretendu = min(ncr.index.max(), nct.index.max(), nca.index.max())
            classe_pretendu = data_echelons.loc[[index_classe_pretendu], ["Niveau", "Échelon"]]
            st.write("La combinaison de mon niveau d'autonomie, de technicité dans mon travail et de responsabilité me "
                     "permet prétendre à la qualification :blue[", classe_pretendu.iloc[0, 0], "], échelon : :blue[",
                     classe_pretendu.iloc[0, 1], "].")
            st.write("Cela me permet de prétendre à un salaire brut de :blue[",
                     str(niveau_remuneration.loc[(niveau_remuneration["Niveau"] == classe_pretendu.iloc[0, 0]) &
                                                 (niveau_remuneration["Echelon"] == classe_pretendu.iloc[0, 1]),
                     "Taux Horaire B"].iloc[0]), "€/h].")
            st.session_state['qualification'] = classe_pretendu
        else:
            st.write("Choississez un niveau pour chacun des trois critères"
                     " (Autonomie, Responsabilité, Technicité) pour avoir un résultat global qui sera affiché ici.")

# Tab2 pour la comparaison avec d'autres métiers
with (tab2):
    st.write("Sélectionnez le métier qui s'approche le plus du votre : ")
    metier = st.radio("Choississez le niveau d'autonomie qui vous correspond le plus : ",
                      options=data_echelons["Liste non exhaustive d'emplois repères"].drop_duplicates(),
                      captions=" ",
                      label_visibility="collapsed")
    # Conteneur du bilan
    st.divider()
    with (st.container()):
        st.header("Bilan")

        # Disclaimer
        with st.container(border=True):
            st.write("""
            Ce calculateur est fourni à titre informatif seulement, il ne remplace pas les conseils professionnels, et 
            il est donc de la responsabilité de l'utilisateur en cas de d'irrégularité détectée de rencontrer un professionnel
            pour qu'il puisse constater.
            """)

        if metier is None:
            st.write("Veuillez d'abord sélectionner une des options ci-dessus.")
        else:
            niveau_pretendu = data_echelons.loc[data_echelons["Liste non exhaustive d'emplois repères"] == metier,
                                                ["Niveau", "Échelon"]].drop_duplicates()
            st.session_state['qualification'] = niveau_pretendu
            st.write("Les métiers sélectionnés permettent d'accéder au niveau : :blue[", niveau_pretendu.Niveau.iloc[0],
                     "] à l'échelon : :blue[", niveau_pretendu.Échelon.iloc[0], "].")

st.write("Ma classe ne correspond pas :")
if st.button(label="Vers la FAQ"):
    st.switch_page("pages/4_❓_FAQ.py")

st.write("Je passe au calcul de mon salaire brut :")
if st.button(label="Le calculateur de salaire"):
    st.switch_page("pages/2_💰_Mon_Salaire_Brut.py")
