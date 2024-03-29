import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(
    page_title="Mon salaire brut",
    page_icon="📖",
)
st.title("Tout savoir sur mon salaire brut")

# Importation de la fiche des salaires
grades = pd.read_csv('App/data/fiche_classes_et_salaires.csv')

# Inscription en dur des niveaux de prime d'ancienneté
primes = [[4, 2], [6, 3], [8, 4], [10, 5], [15, 5.5], [20, 6]]


def trouver_index(dataf, key):
    i = 0
    for elt in dataf:
        if elt == key: break
        i += 1
    return i


# Initialisation des variables dans le session state
if 'qualification' not in st.session_state:
    st.session_state['qualification'] = None

# Conteneur d'intro
with st.container(border=True):
    st.write("""Cet outil permet de retrouver et de comprendre son salaire minimum brut mensuel pour un contrat à temps
    partiel. Afin de pouvoir fournir les informations nécessaires, il est conseillé de prendre avec soi la fiche de paie
    du mois concerné ainsi que son contrat de travail.""")

# Conteneur pour le renseignement de son grade
with st.container():
    st.subheader("Je renseigne mon grade")
    with st.expander("Où trouver votre grade"):
        st.write("""Vous pouvez retrouver votre grade, ou votre qualification, sur le haut de votre fiche de paye. Il 
        est aussi possible d'utiliser notre calculateur de classe pour retrouver votre classe ou encore pour la 
        comparer à celle indiquée sur votre fiche de paie.""")

    niveaux = grades["Niveau"].drop_duplicates().drop_duplicates()
    index_n, index_e = 0, 0
    qualification = st.session_state['qualification']
    if 'qualification' in st.session_state and st.session_state.qualification is not None:
        index_n = trouver_index(niveaux, qualification["Niveau"].iloc[0])
    niveau = st.selectbox('Selectionner votre niveau', niveaux, index=index_n)

    ech = grades.loc[grades['Niveau'] == niveau, 'Echelon'].drop_duplicates().drop_duplicates()
    if 'qualification' in st.session_state and st.session_state.qualification is not None:
        index_e = trouver_index(ech, qualification['Échelon'].iloc[0])
    echelon = st.selectbox('Selectionner votre échelon', ech, index=index_e)

st.divider()

# Conteneur pour renseigner son ancienneté
with st.container():
    st.subheader("Je renseigne mon ancienneté")
    with st.expander("Comment connaitre son niveau d'expérience ?"):
        st.write("""Connaitre son ancienneté permet de calculer le montant de la prime d'expérience. Cette prime est 
        versée mensuellement aux employés. On compte comme expérience tout emploi effectué dans la profession pouvant 
        être justifié via un contrat de travail (ou autre justificatif). Une pause ou interruption de plus de 12 mois 
        dans la profession remet le compteur d'expérience à 0. 
        La prime est calculée comme une bonification des heures du contrat à temps partiel selon les niveaux
        d'expériences suivant :    
        - après 4 ans d'expérience professionnelle : 2 % ;    
        - après 6 ans d'expérience professionnelle : 3 % ;     
        - après 8 ans d'expérience professionnelle : 4 % ;    
        - après 10 ans d'expérience professionnelle : 5 % ;     
        - après 15 ans d'expérience professionnelle au 1er janvier 2012 : 5,5 % ;    
        - après 20 ans d'expérience professionnelle au 1er janvier 2013 : 6 %.    
        On retrouve son ancienneté en haut de sa fiche de paie.    
        Si l'expérience indiquée sur votre fiche de paie ne correspond pas à celle qui vous est due, il est conseillé de
         contacter les Ressources Humaines (RH) de son entreprise.""")
    anciennete = st.number_input("Entrer un nombre d'années", step=1, format="%i")

st.divider()

# Conteneur pour renseigner son nombre d'heures
with st.container():
    st.subheader("Je renseigne mon nombre d'heures travaillées mensuelles")
    heures_contractuelles = st.number_input("Entrer le nombre d'heures mensuelles "
                                            "inscrites au contrat (hors complément d'heures) ", step=1, format="%i")
    with st.expander("Ou retrouver son nombre d'heures ?"):
        st.write("""Vous pouvez retrouver ce nombre d'heures sur votre contrat de travail.""")

    st.write("")

# Conteneur pour complement heures
    a_complement_heures = st.checkbox("J'ai signé un avenant à mon contrat ce mois-ci pour un complément d'heures")
    with st.expander("Qu'est-ce qu'un complément d'heures ?"):
        st.write("""Un complément d'heure est un avenant au contrat de travail pouvant 
        être proposé au travailleur en temps partiel. Il s'agit d'ajouter des heures 
        (au minimum 1/10 des heures du contrat initial). C'est un ajout **temporaire**
        bien déterminé entre une date de début et une date de fin. Les heures 
        travaillées du complément d'heure sont bonifiées à 10%.""")
    if a_complement_heures:
        with st.container():
            heures_du_complement = st.number_input("Entrer le nombre d'heure du complément pour le mois voulu",
                                                   step=1,
                                                   format="%i")

    st.write("")

    heures_travaillees = st.number_input("Entrer le nombre total d'heures effectivement travaillées ce mois-ci",
                                         step=1,
                                         format="%i")

    est_taux_horaire_B = st.checkbox("Je suis au taux horaire B.")

    with st.expander("Qu'elle est la différence entre le taux horaire A et B ?"):
        st.write("""Qu'importe votre classe, le taux horaire B est supérieur au taux horaire B. Vous correspondez au taux horaire B si vous avez au moins trois mois d'ancienneté, 
        votre contrat ne concerne pas une mission de remplacement et qui vous avez plusieurs rôles dans l'entreprise.
        Cela peut être par exemple, s'occuper des missions classiques demandé aux agents d'entretien, mais avoir en plus de celles-ci le gardiennage des clés, la fermeture du portail...
        Pour plus de renseignements, vous pouvez consulter la FAQ pour trouver une liste de contact utile.
        """)

st.divider()

# Conteneur pour les informations sur le travail de nuit
a_travail_de_nuit = st.checkbox("J'ai effectué du travail de nuit")
with st.expander("Qu'est-ce qu'une heure de nuit ?"):
    st.write("""Les heures de nuits sont les heures de travail effectuées entre **21h et 5h** du
    matin si vous n'avez pas le statut de travailleur de nuit, et entre **21h et 6h** du matin 
    si vous avez le statut de travailleur de nuit.    
    Le statut de travailleur de nuit concerne les personnes qui travaillent au moins **2 
    fois par semaine** plus de **3h** entre 21h et 6h.    
    De plus, il concerne aussi les personnes ayant effectuées **plus de 270h** de travail
    de nuit sur les **12 mois précédents**.    
    Le statut de travailleur de nuit donne droit à des compensations en heures de repos
    supplémentaires.
    """)

heures_de_nuit_regulieres = 0
heures_de_nuit_occasionnelles = 0

if a_travail_de_nuit:
    with st.container():
        st.subheader("Je renseigne mes heures de nuit (de 21h à 5-6h) pour des travaux réguliers")
        with st.expander("Qu'est-ce qu'une heure de nuit pour des travaux réguliers ?"):
            st.write("""Les travaux réguliers concernent tous les travaux planifiés et
            potentiellement inscrits dans le contrat de travail. Les heures de travail
            de nuit exercées dans ce cadre sont bonifiées à hauteur de 20%""")
        heures_de_nuit_regulieres = st.number_input("Entrer le nombre d'heures faites de nuit (de 21h à 5-6h)"
                                                    "pour des travaux réguliers", step=1, format="%i")

    with st.container():
        st.subheader("Je renseigne mes heures de nuit (de 21h à 5-6h) pour des travaux occasionnels")
        with st.expander("Qu'est-ce qu'une heure de nuit pour des travaux occasionnels ?"):
            st.write("""Les travaux occasionnels désignent tous les travaux non planifiés.
            Les heures de travail de nuit exercées dans ce cadre sont bonifiées à hauteur 
            de 100%""")
        heures_de_nuit_occasionnelles = st.number_input("Entrer le nombre d'heures faites de nuit (de 21h à 5-6h) "
                                                        "pour des travaux occasionnels", step=1, format="%i")

st.divider()

# Conteneur pour renseigner son nombre d'heures le dimanche

a_travail_le_jour_du_dimanche = st.checkbox("J'ai travaillé le dimanche")
with st.expander("Quelle est la rémunération ?"):
    st.write("""Les heures de travail du dimanche sont majorées dans les conditions ci-après :    
    - heures de travail effectuées normalement le dimanche conformément au contrat de travail du salarié et/ou planning 
    (sur un document écrit) : 20 % ;    
    - heures de travail effectuées exceptionnellement le dimanche non prévues au planning ni au contrat de travail : 
    100 %.""")

heures_du_dimanche = 0

if a_travail_le_jour_du_dimanche:
    with st.container():
        a_contrat_de_travail_jour_du_dimanche = st.checkbox("Il est écrit dans mon contrat de travail que je "
                                                            "travaille le dimanche. ")
        st.subheader("Je renseigne mes heures effectuées le dimanche")
        heures_du_dimanche = st.number_input("Entrer le nombre d'heures faites le dimanche", step=1, format="%i")

st.divider()

# Conteneur pour renseigner son nombre d'heures les jours fériés

a_travail_le_jour_ferie = st.checkbox("J'ai travaillé des jours fériés")
with st.expander("Quelle est la rémunération pour les jours fériés? "):
    st.write("""Les heures de travail les jours fériés sont majorées dans les conditions ci-après :    
    – heures de travail effectuées normalement les jours fériés conformément au contrat de travail et/ou planning (sur un document écrit)
    du salarié : 50%;    
    – heures de travail effectuées exceptionnellement les jours fériés non prévues au planning ni au contrat de 
    travail : 100 %.""")

heures_du_ferie = 0

if a_travail_le_jour_ferie:
    with st.container():
        a_contrat_de_travail_jour_ferie = st.checkbox(
            "Il est écrit dans mon contrat de travail que je travaille les jours fériés. ")
        st.subheader("Je renseigne mes heures effectuées les jours fériés ce mois-ci")
        heures_du_ferie = st.number_input("Entrer le nombre d'heures faites les jours fériés", step=1, format="%i")

st.divider()

# Conteneur pour afficher le salaire
with (st.container()):
    st.header("Mon salaire brut")

    # Disclaimer
    with st.container(border=True):
        st.write("""
        Ce calculateur est fourni à titre informatif seulement, il ne remplace pas les conseils professionnels, et 
        il est donc de la responsabilité de l'utilisateur en cas de d'irrégularité détectée de rencontrer un professionnel
        pour qu'il puisse constater.
        """)

    salaire_brut_total = 0

    # Détermination de la base
    if est_taux_horaire_B:
        base = float(
            grades.loc[(grades["Niveau"] == niveau) & (grades["Echelon"] == echelon), 'Taux Horaire B'].iloc[0])
        text = "Je suis sur le :blue[taux horaire B] donc "
    else:
        base = float(
            grades.loc[(grades["Niveau"] == niveau) & (grades["Echelon"] == echelon), 'Taux Horaire A'].iloc[0])
        text = "Je suis sur le :blue[taux horaire A] donc "
    text += "mon taux horaire brut est de :blue[" + str(base) + "€/h]"
    st.write(text)

    # Détermination des heures complémentaires / de la rémunération du complément d'heures
    salaire_complements_heures = 0
    prime_heures_complementaires_maj_11 = 0
    prime_heures_complementaires_maj_25 = 0
    if a_complement_heures:
        salaire_complements_heures = base * 1.1 * heures_du_complement
        prime_heures_complementaires_maj_25 = base * 1.25 * (
                heures_travaillees - heures_contractuelles - heures_du_complement)
        st.write("Mon complément d'heures de ", round(heures_du_complement, 2), "h me rapporte ",
                 round(salaire_complements_heures, 2), "€")
        st.write("""Mes heures "supplémentaires" en dehors de compléments d'heures me rapportent """,
                 round(salaire_complements_heures, 2), "€")
        salaire_brut_total += salaire_complements_heures + prime_heures_complementaires_maj_25

    else:
        heures_complementaires_maj_11 = min(max(heures_travaillees - heures_contractuelles, 0),
                                            0.1 * heures_contractuelles)
        prime_heures_complementaires_maj_11 = base * 1.11 * heures_complementaires_maj_11
        st.write("J'ai ", heures_complementaires_maj_11, "heures complémentaires majorées à 11%, soit un revenu de : ",
                 round(prime_heures_complementaires_maj_11, 2), "€")

        heures_complementaire_maj_25 = min(
            max(heures_travaillees - (heures_contractuelles + heures_contractuelles * 0.1), 0),
            1 / 3 * heures_contractuelles - 0.1 * heures_contractuelles)
        prime_heures_complementaires_maj_25 = base * 1.25 * heures_complementaire_maj_25
        st.write("J'ai ", round(heures_complementaire_maj_25, 2),
                 "heures complémentaires majorées à 25%, soit un revenu de : ",
                 round(prime_heures_complementaires_maj_25, 2), "€")
        salaire_brut_total += prime_heures_complementaires_maj_25 + prime_heures_complementaires_maj_11

    # Calcul de la majoration heures de nuit
    if a_travail_de_nuit:
        prime_heures_de_nuit_prevues = 1.2 * base * heures_de_nuit_regulieres
        prime_heures_de_nuit_imprevues = 2 * base * heures_de_nuit_occasionnelles
        st.write("Le cumul de mes ",
                 round(heures_de_nuit_occasionnelles + heures_de_nuit_regulieres),
                 "h de travail de nuit me rapporte ",
                 round(prime_heures_de_nuit_prevues + prime_heures_de_nuit_imprevues),
                 "€")
        salaire_brut_total += prime_heures_de_nuit_imprevues + prime_heures_de_nuit_prevues

    # Calcul de la majoration heures du dimanche
    if a_travail_le_jour_du_dimanche:
        if a_contrat_de_travail_jour_du_dimanche:
            prime_heures_le_dimanche = 1.2 * base * heures_du_dimanche
        else:
            prime_heures_le_dimanche = 2 * base * heures_du_dimanche
        st.write("Le cumul de mes ", round(heures_du_dimanche),
                 "h de travail le dimanche me rapporte ", round(prime_heures_le_dimanche), "€")
        salaire_brut_total += prime_heures_le_dimanche

    # Calcul de la majoration heures jours fériés
    if a_travail_le_jour_ferie:
        if a_contrat_de_travail_jour_ferie:
            prime_heures_jour_ferie = 1.5 * base * heures_du_ferie
        else:
            prime_heures_jour_ferie = 2 * base * heures_du_ferie
        st.write("Le cumul de mes ", round(heures_du_ferie),
                 "h de travail les jours fériés me rapporte ", round(prime_heures_jour_ferie), "€")
        salaire_brut_total += prime_heures_jour_ferie

    # Determine le niveau d'ancienneté
    niveau_prime_anciennete = 0
    remuneration_minimale_hierarchique = base * heures_contractuelles
    if anciennete > 3:
        for prime in reversed(primes):
            if anciennete >= prime[0]:
                niveau_prime_anciennete = prime[1]
                break
    prime_anciennete = niveau_prime_anciennete / 100 * remuneration_minimale_hierarchique
    st.write("Ma prime d'ancienneté me rapporte ", round(prime_anciennete, 2), "€")
    salaire_brut_total += prime_anciennete

    salaire_brut_total += base * (heures_contractuelles - heures_de_nuit_occasionnelles
                                  - heures_de_nuit_regulieres - heures_du_dimanche - heures_du_ferie)
    st.write("**Mon salaire minimum brut est donc de :", round(salaire_brut_total, 2), "€**")
    st.write("""Pour calculer votre salaire net, vous pouvez utiliser le site du gouvernement suivant : 
    [Calculateur de salaire net](https://code.travail.gouv.fr/outils/simulateur-embauche)""")

st.write("Mon salaire ne correspond pas :")
if st.button(label="Vers la FAQ"):
    st.switch_page("pages/4_❓_FAQ.py")

st.write("Je veux vérifier si l'abattement est intéressant pour moi :")
if st.button(label="Vers la page sur l'Abattement"):
    st.switch_page("pages/3_⚖️_L'abattement_ou_DFS.py")
