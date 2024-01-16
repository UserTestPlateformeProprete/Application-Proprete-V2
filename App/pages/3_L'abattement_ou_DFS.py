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
    Cet outil est là pour aider à visualiser les gains sur son salaire mais aussi les pertes sur sa future retraite.
    """)




