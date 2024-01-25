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

    with st.expander("Question 3"):
        st.write("I#m blue")

st.divider()

with st.container():
    st.header("Section 2")

    with st.expander("Question 1"):
        st.write("I#m blue")

    with st.expander("Question 2"):
        st.write("I#m blue")

    with st.expander("Question 3"):
        st.write("I#m blue")