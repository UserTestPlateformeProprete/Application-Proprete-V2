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
    En 2024 le montant maximal abattu est de 8% est diminue d'1% chaque année. Ainsi, il ne sera plus possible de faire 
    de la déduction forfaitaire spécifique après 2029.    
    Cet outil est là pour aider à visualiser les gains sur son salaire mais aussi les pertes sur sa future retraite.
    """)

# Import des données
df = pd.read_csv("demo/data/fiche_coefficient_inflation_revalorisation_smic.csv", sep=",")
# st.write(df)

# Selection de la période
with st.container():
    debut, fin = st.select_slider("Choississez sur quelle période vous comptez utiliser la DFS",
                                  df["année"], value=(2000, 2020),
                                  help="Glissez à gauche pour sélectionner une année de départ et à droite pour"
                                       " l'année de fin")

# Selection de la moyenne d'heure travaillée
with st.container():
    nbr_heures_mensuel = st.number_input("J'estime mon nombre d'heures mensuelles moyen travaillé", value=100)

# Selection de son écart au SMIC
with st.container():
    ecart_smic = st.slider("Choississez votre écart moyen avec le smic sur cette période en pourcentage", 0, 100,
                           value=0, help="Vous pouvez vérifier ci-dessous que l'écart choisit correspond bien à votre "
                                         "salaire sur la période")

    # Conversion des taux horaires en salaire mensuel
    salaires = df.loc[(df['année'] >= debut) & (df['année'] <= fin), ["année", "smic", "abattement"]]
    salaires["salaires"] = salaires["smic"] * (1 + ecart_smic / 100) * nbr_heures_mensuel
    # st.write(salaires)

    # Affichage des salaires estimés
    st.write("En ", int(salaires.iloc[0]["année"]), "le SMIC était de ", int(salaires.iloc[0]["smic"] * nbr_heures_mensuel),
             "€ donc mon salaire brut mensuel était d'environ ", int(salaires.iloc[0]["salaires"]), "€")
    if fin - debut > 2:
        st.write("En ", int(salaires.iloc[int(len(salaires) / 2)]["année"]), "le SMIC était de ",
                 int(salaires.iloc[int(len(salaires)/2)]["smic"] * nbr_heures_mensuel),
                 "€ donc mon salaire brut mensuel était d'environ ",
                 int(salaires.iloc[int(len(salaires)/2)]["salaires"]), "€")
    if fin - debut > 0:
        st.write("En ", int(salaires.iloc[-1]["année"]), "le SMIC était de ",
                 int(salaires.iloc[-1]["smic"] * nbr_heures_mensuel), "€ donc mon salaire brut mensuel était d'environ ",
                 int(salaires.iloc[-1]["salaires"]), "€")

# Nombre de trimestres effectués
with st.container():
    a_trimestres_retraite = st.checkbox("Je n'aurais pas tous mes trimestres lorsque je partirai en retraite")
    if a_trimestres_retraite:
        st.subheader("Je renseigne mon nombre de trimestres effectués lorsque je partirai en retraite")
        with st.expander("Vous n'avez pas cette information ?"):
            st.write(""" Dans ce cas, vous pouvez cocher que vous aurez tous vos trimestres lorsque vous partirez en 
                    retraite. La simulation sera moins précise.""")
        trimestres_retraite = st.number_input("Entrer un nombre de trimestres", step=1, format="%i", min_value=1,
                                              max_value=172)
    else:
        trimestres_retraite = 172

st.divider()

# Calcul du brut
df = df.iloc[::-1]
df["inflation cumulée"] = (1 + (df["inflation"] / 100)).cumprod()
salaires["brut corrigé"] = salaires["salaires"] * df.loc[
    (df['année'] >= debut) & (df['année'] <= fin), "inflation cumulée"]
salaires["brut annuel corrigé"] = salaires["brut corrigé"] * 12

# Calcul du gain abattement
abattement = df.loc[(df['année'] >= debut) & (df['année'] <= fin), "abattement"]
salaires['brut annuel corrigé abattu'] = salaires["brut annuel corrigé"].mul((1 - abattement / 100))
salaires['net annuel corrigé'] = salaires['brut annuel corrigé'] * 0.8
salaires['net annuel corrigé abattu'] = (salaires["brut annuel corrigé abattu"] * 0.8 +
                                         salaires["brut annuel corrigé"].sub(salaires["brut annuel corrigé abattu"]))
gain_abattement_total = salaires['net annuel corrigé abattu'].sum() - salaires['net annuel corrigé'].sum()

# Calcul retraite
retraites_annuelles_non_abattues = 0.5 * salaires["brut annuel corrigé"].mean() * (trimestres_retraite / 172)
retraites_annuelles_abattues = 0.5 * salaires["brut annuel corrigé abattu"].mean() * (trimestres_retraite / 172)
difference_retraite = retraites_annuelles_non_abattues - retraites_annuelles_abattues

# Calcul nombre d'années à la retraite nécessaire pour être gagnant
if difference_retraite == 0:
    annees_de_retraites = 0
else :
    annees_de_retraites = gain_abattement_total / difference_retraite

# Affichage du nombre d'années nécessaires
with st.container():
    st.subheader("Bilan : ")
    st.write("A partir des données de la simulation et si les années de la période comptent pour votre retraite, nous "
             "estimons un gain de ", int(gain_abattement_total), "€ via l'abattement mais une perte de ",
             int(difference_retraite), "€/an sur votre retraite. Ainsi à partir de plus de", int(annees_de_retraites),
             " années après la retraite, faire de l'abattement n'est pas avantageux pour vous.")
