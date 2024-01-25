import streamlit as st

st.set_page_config(
    page_title="F.A.Q.",
    page_icon="❓",
    layout="centered",
)
st.title("Foire Aux Questions")

st.empty()

with st.container():
    with st.expander("Que faire si le salaire calculé ne correspond pas à mon salaire ?"):
        st.write("""Dans ce cas, nous vous conseillons de prendre contact avec le service des ressources humaines
                    pour obtenir des informations supplémentaires. 
                    Calculer un salaire demande de nombreuses données, il est aussi possible 
                    que certaines d'entre elles n’aient pas été comprises dans le calcul,
                    ce qui peut expliquer cette différence.""")

    with st.expander("Que faire si ma classe ne correspond pas ?"):
        st.write("""
        En cas de sous-classification identifiée  il est possible de :    
        - négocier avec l’employeur en ayant éventuellement recours à un représentant du personnel ou à un Syndicat. 
        - ou, effectuer une saisie du conseil de prud’hommes """)

    with st.expander("Qui puis-je contacter pour obtenir plus d’informations et être accompagné?"):
        st.write("""
        Vous pouvez faire appel :     
        - à un syndiqué.    
        - à une Association d’Avocats, des permanences gratuites existent.    
        - à l’Inspection du travail, vous pouvez vous renseigner auprès d'eux, sans que cela amène à une enquête si 
        vous ne souhaitez pas en faire une.""")

    with st.expander("Où trouver des informations sur mes droits?"):
        st.markdown("""
        - Vous pouvez consulter la Convention Collective ici : [Convention collective Entreprises de 
        propreté et services associés](https://www.legifrance.gouv.fr/conv_coll/id/KALIARTI000027172464/?idConteneur=KALICONT000027172335&origin=list)    
        - Et voici une autre page qui explique de manière simplifiée la Convention Collective : [Convention 
        collective Propreté 2024](https://www.convention.fr/convention-proprete-entreprises-de-3173.html)
        """)

