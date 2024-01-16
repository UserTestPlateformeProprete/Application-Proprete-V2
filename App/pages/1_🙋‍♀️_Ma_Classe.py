import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(
    page_title="Ma classe",
    page_icon="📖",
)
st.title("Vérifier sa classe")

# Import des données pre-requises pour les salaires
niveau_remuneration = pd.read_csv('App/fiche_classes_et_salaires.csv')
# st.write(classes)

# Import des données pre-requises pour classes
data_echelons = pd.read_csv('App/fiche_niveau_et_echelon.csv')
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
    https://www.legifrance.gouv.fr/conv_coll/article/KALIARTI000047082593#KALIARTI000047082593)""")
    with st.expander("Voir les niveaux de rémunération"):
        st.write("[Vers les grilles de salaires](https://www.convention.fr/convention-proprete-entreprises-de-3173"
                 ".html#grilles-de-salaire)")
        st.write(niveau_remuneration)

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
    st.subheader("Bilan")
    classe_pretendu = None
    if niveau_responsabilite is not None and niveau_technicite is not None and niveau_autonomie is not None:
        index_classe_pretendu = min(ncr.index.max(), nct.index.max(), nca.index.max())
        classe_pretendu = data_echelons.loc[[index_classe_pretendu], ["Niveau", "Échelon"]]
        st.write("La combinaison de mon niveau d'autonomie, de technicité dans mon travail et de responsabilité me "
                 "permet prétendre à la qualification :blue[", classe_pretendu.iloc[0, 0], "], échelon : :blue[",
                 classe_pretendu.iloc[0, 1], "].")
        st.write("Cela me permet de prétendre à un salaire de :blue[",
                 str(niveau_remuneration.loc[(niveau_remuneration["Niveau"] == classe_pretendu.iloc[0, 0]) &
                                             (niveau_remuneration["Echelon"] == classe_pretendu.iloc[0, 1]),
                                             "Taux Horaire B"].iloc[0]), "€/h].")
        st.session_state['qualification'] = classe_pretendu
    else:
        st.write("Choississez un niveau pour chacun des trois critères"
                 " (Autonomie, Responsabilité, Technicité) pour avoir un résultat global")
