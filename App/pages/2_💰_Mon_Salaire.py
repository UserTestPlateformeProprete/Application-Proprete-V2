import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(
    page_title="Mon salaire",
    page_icon="📖",
)
st.title("Tout savoir sur mon salaire")

# Importation de la fiche des salaires
grades = pd.read_csv('App/fiche_grades_et_salaires.csv')

# Inscription en dur des niveaux de prime d'ancienneté
primes = [[4, 2], [6, 3], [8, 4], [10, 5], [15, 5.5], [20, 6]]

# Container pour le renseignement de son grade
with st.container():
    st.subheader("Je renseigne mon grade")
    with st.expander("Où trouver votre grade"):
        st.write("""Vous pouvez retrouver votre grade, ou votre qualification, sur le haut de votre fiche de paye.
        Exemple+""")
    niveau = st.selectbox('Selectionner votre niveau', grades["Niveau"].drop_duplicates().drop_duplicates())
    echelon = st.selectbox('Selectionner votre échelon', grades.loc[grades['Niveau'] == niveau, 'Echelon'].drop_duplicates().drop_duplicates())

st.divider()

# Container pour renseigner son ancienneté
with st.container():
    st.subheader("Je renseigne mon ancienneté")
    with st.expander("Comment connaitre son niveau d'expérience"):
        st.write("""Connaitre son ancienneté permet de calculer le montant de la prime d'expérience. Cette prime est versée
         mensuellement aux employés. On compte comme expérience tout emploi effectué dans la profession pouvant être 
         justifié via un contrat de travail (ou autre justificatif). Une pause ou interruption de plus de 12 mois dans la 
         profession remet le compteur d'expérience à 0.   
         La prime est calculée comme une bonification des heures du contrat à temps partiel selon les niveaux d'expériences
         suivant :   
         - après 4 ans d'expérience professionnelle : 2 % ;   
         - après 6 ans d'expérience professionnelle : 3 % ;   
         - après 8 ans d'expérience professionnelle : 4 % ;   
         - après 10 ans d'expérience professionnelle : 5 % ;   
         - après 15 ans d'expérience professionnelle au 1er janvier 2012 : 5,5 % ;   
         - après 20 ans d'expérience professionnelle au 1er janvier 2013 : 6 %.""")
    anciennete = st.number_input("Entrer un nombre d'année", step=1, format="%i")

st.divider()

# Container pour renseigner son nombre d'heures
with st.container():
    st.subheader("Je renseigne mon nombre d'heures travaillées mensuelles")
    heures_contractuelles = st.number_input("Entrer le nombre d'heures mensuelles du contrat (hors complément d'heures) ", step=1, format="%i")
    with st.expander("Ou retrouver son nombre d'heures ?"):
        st.write("""Vous pouvez retrouver ce nombre d'heures sur votre contrat. 
        Si vous faites du complément d'heures, ne les comptez pas ici.""")
    heures_travaillees = st.number_input("Entrer le nombre d'heures travaillées ce mois (heures supplémentaires et compléments d'heures compris)", step=1, format="%i")
    est_taux_horaire_B = st.checkbox("J'ai travaillé trois mois en continu et je ne suis pas en remplacement")

st.divider()

# Container pour les informations sur le travail de nuit
a_travail_de_nuit = st.checkbox("J'ai effectué du travail de nuit")
with st.expander("Qu'est-ce qu'une heure de nuit ?"):
    st.write("""Les heures de nuits sont les heures de travail effectuées entre 21h et 5h du
    matin si vous n'avez pas le statut de travailleur de nuit, et entre 21h et 6h du matin 
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
        st.subheader("Je renseigne mes heures de nuit pour des travaux réguliers")
        with st.expander("Qu'est-ce qu'une heure de nuit pour des travaux réguliers ?"):
            st.write("""Les travaux réguliers concernent tous les travaux planifiés et
            potentiellement inscrits dans le contrat de travail. Les heures de travail
            de nuit exercées dans ce cadre sont bonifiées à hauteur de 20%""")
        heures_de_nuit_regulieres = st.number_input("Entrer le nombre d'heures faites de nuit pour des travaux réguliers", step=1, format="%i")

    with st.container():
        st.subheader("Je renseigne mes heures de nuit pour des travaux occasionnels")
        with st.expander("Qu'est-ce qu'une heure de nuit pour des travaux occasionnels ?"):
            st.write("""Les travaux occasionnels désignent tous les travaux non planifiés.
            Les heures de travail de nuit exercées dans ce cadre sont bonifiées à hauteur 
            de 100%""")
        heures_de_nuit_occasionnelles = st.number_input("Entrer le nombre d'heures faites de nuit pour des travaux occasionnels", step=1, format="%i")

st.divider()

# Container pour renseigner son nombre d'heures le dimanche

a_travail_le_jour_du_dimanche = st.checkbox("J'ai travaillé le dimanche")
with st.expander("Qu'elle est la rémunération "):
    st.write("""Les heures de travail du dimanche sont majorées dans les conditions ci-après :    
 - heures de travail effectuées normalement le dimanche conformément au planning et/ou contrat de travail du salarié : 20 % ;
 - heures de travail effectuées exceptionnellement le dimanche non prévues au planning ni au contrat de travail : 100 %.""")

heures_du_dimanche = 0

if a_travail_le_jour_du_dimanche:
    with st.container():
        a_contrat_de_travail_jour_du_dimanche = st.checkbox("Il est écrit dans mon contrat de travail que je travaille le dimanche. ")
        st.subheader("Je renseigne mes heures effectuées le dimanche")
        heures_du_dimanche = st.number_input("Entrer le nombre d'heures faites le dimanche", step=1, format="%i")

st.divider()

# Container pour renseigner son nombre d'heures les jours fériés

a_travail_le_jour_ferie = st.checkbox("J'ai travaillé des jours fériés")
with st.expander("Qu'elle est la rémunération pour les jours fériés? "):
    st.write("""Les heures de travail les jours fériés sont majorées dans les conditions ci-après :
 – heures de travail effectuées normalement les jours fériés conformément au planning et/ou contrat de travail du salarié : 50 % ;
 – heures de travail effectuées exceptionnellement les jours fériés non prévues au planning ni au contrat de travail : 100 %.""")

heures_du_ferie = 0

if a_travail_le_jour_ferie:
    with st.container():
        a_contrat_de_travail_jour_ferie = st.checkbox("Il est écrit dans mon contrat de travail que je travaille les jours fériés. ")
        st.subheader("Je renseigne mes heures effectuées les jours fériés ce mois-ci")
        heures_du_ferie = st.number_input("Entrer le nombre d'heures faites les jours fériés", step=1, format="%i")

st.divider()

# Container pour complement heures

a_complement_heures = st.checkbox("J'ai un ou plusieurs compléments d'heures")
with st.expander("Qu'est-ce qu'un complément d'heures"):
    st.write("""Un complément d'heure est un avenant au contrat de travail pouvant 
    être proposé au travailleur en temps partiel. Il s'agit d'ajouter des heures 
    (au minimum 1/10 des heures du contrat initial). C'est un ajout **temporaire**
    bien déterminer entre une date de début et une date de fin. Les heures 
    travaillées du complément d'heure sont bonifiées à 10%.""")

if a_complement_heures:
    with st.container():
        heures_du_complement = st.number_input("Entrer le nombre d'heure du complément pour le mois voulu", step=1, format="%i")

st.divider()

# Container pour afficher le salaire
with (st.container()):
    st.subheader("Bilan")

    salaire_brut_total = 0

    # Détermination de la base
    if est_taux_horaire_B:
        base = float(grades.loc[(grades["Niveau"] == niveau) & (grades["Echelon"] == echelon), 'Taux Horaire B'])
    else: base = float(grades.loc[(grades["Niveau"] == niveau) & (grades["Echelon"] == echelon), 'Taux Horaire A'])
    st.write("Mon taux horaire est", base, "€/heure")

    # Détermination des heures complémentaires / de la rémunération du complément d'heures
    salaire_complements_heures = 0
    prime_heures_complementaires_maj_11 = 0
    prime_heures_complementaires_maj_25 = 0
    if a_complement_heures:
        salaire_complements_heures = base * 1.1 * heures_du_complement
        prime_heures_complementaires_maj_25 = base * 1.25 * (heures_travaillees - heures_contractuelles - heures_du_complement)
        st.write("Mon complément d'heures de ", heures_du_complement, "h me rapporte ", round(salaire_complements_heures, 2), "€")
        st.write("""Mes heures "supplémentaire" en dehors de compléments d'heures me rapporte """, round(salaire_complements_heures, 2), "€")
        salaire_brut_total += salaire_complements_heures + prime_heures_complementaires_maj_25

    else :
        heures_complementaires_maj_11 = min(max(heures_travaillees - heures_contractuelles, 0), 0.1 * heures_contractuelles)
        prime_heures_complementaires_maj_11 = base * 1.11 * heures_complementaires_maj_11
        st.write("J'ai ", heures_complementaires_maj_11, "heures complémentaire majorées à 11%, soit un revenu de : ", round(prime_heures_complementaires_maj_11, 2), "€")

        heures_complementaire_maj_25 = min(max(heures_travaillees - (heures_contractuelles + heures_contractuelles * 0.1), 0), 1 / 3 * heures_contractuelles - 0.1 * heures_contractuelles)
        prime_heures_complementaires_maj_25 = base * 1.25 * heures_complementaire_maj_25
        st.write("J'ai ", heures_complementaire_maj_25, "heures complémentaire majorées à 25%, soit un revenu de : ", round(prime_heures_complementaires_maj_25, 2), "€")
        salaire_brut_total += prime_heures_complementaires_maj_25 + prime_heures_complementaires_maj_11

    # Calcul de la majoration heures de nuit
    if a_travail_de_nuit:
        prime_heures_de_nuit_prevues = 1.2 * base * heures_de_nuit_regulieres
        prime_heures_de_nuit_imprevues = 2 * base * heures_de_nuit_occasionnelles
        st.write("Le cumul de mes ", heures_de_nuit_occasionnelles+heures_de_nuit_regulieres, "h de travail de nuit me rapporte ", prime_heures_de_nuit_prevues + prime_heures_de_nuit_imprevues, "€")
        salaire_brut_total += prime_heures_de_nuit_imprevues + prime_heures_de_nuit_prevues

    # Calcul de la majoration heures du dimanche
    if a_travail_le_jour_du_dimanche:
        if a_contrat_de_travail_jour_du_dimanche:
            prime_heures_le_dimanche = 1.2 * base * heures_du_dimanche
        else:
            prime_heures_le_dimanche = 2 * base * heures_du_dimanche
        st.write("Le cumul de mes ", heures_du_dimanche,
                     "h de travail le dimanche me rapporte ", prime_heures_le_dimanche,"€")
        salaire_brut_total += prime_heures_le_dimanche

    # Calcul de la majoration heures jours fériés
    if a_travail_le_jour_ferie:
        if a_contrat_de_travail_jour_ferie:
            prime_heures_jour_ferie = 1.5 * base * heures_du_ferie
        else:
            prime_heures_jour_ferie = 2 * base * heures_du_ferie
        st.write("Le cumul de mes ", heures_du_ferie,
                    "h de travail les jours fériés me rapporte ", prime_heures_jour_ferie, "€")
        salaire_brut_total += prime_heures_jour_ferie

    # Determine le niveau d'ancienneté
    niveau_prime_anciennete = 0
    remuneration_minimale_hierarchique = base * heures_contractuelles
    if anciennete > 3:
        for prime in reversed(primes) :
            if anciennete >= prime[0]:
                niveau_prime_anciennete = prime[1]
                break
    prime_anciennete = niveau_prime_anciennete / 100 * remuneration_minimale_hierarchique
    st.write("Ma prime d'ancienneté me rapporte ", round(prime_anciennete, 2), "€")
    salaire_brut_total += prime_anciennete

    salaire_brut_total += base * (heures_contractuelles - heures_de_nuit_occasionnelles - heures_de_nuit_regulieres-heures_du_dimanche-heures_du_ferie)
    st.write("Mon salaire minimum brut est donc de :", round(salaire_brut_total,2), "€")


