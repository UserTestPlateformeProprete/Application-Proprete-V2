import streamlit as st

st.set_page_config(
    page_title="Mon salaire",
    page_icon="📖",
)
st.title("Tout savoir sur mon salaire")


with st.container():
    st.subheader("Je renseigne mon grade")
    with st.expander("En savoir plus"):
        st.write("""Lorem Ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
                 ut labore et dolore magna aliqua. Ut enim ad minim veniam ut aliquip ex ea commodo consequat""")
        st.image("img/bulletincorps2020.jpg")
    st.selectbox('Select', [1, 2, 3])

st.divider()

with st.container():
    st.subheader("Je renseigne mon ancienneté")
    with st.expander("En savoir plus"):
        st.write("""Lorem Ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
                 ut labore et dolore magna aliqua. Ut enim ad minim veniam ut aliquip ex ea commodo consequat""")
    st.number_input('Enter a number', step=1, format="%i")

st.divider()

with st.container():
    st.subheader("Je renseigne le nombre d'heures travaillées")
    with st.expander("En savoir plus"):
        st.write("""Lorem Ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
                 ut labore et dolore magna aliqua. Ut enim ad minim veniam ut aliquip ex ea commodo consequat""")
    st.number_input("Nombre d'heures contractuelle",step=1, format="%i")
    with st.expander("En savoir plus"):
        st.write("""Lorem Ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
                 ut labore et dolore magna aliqua. Ut enim ad minim veniam ut aliquip ex ea commodo consequat""")
    st.number_input("Nombre d'heures travaillées", step=1, format="%i")
    with st.expander("En savoir plus"):
        st.write("""Lorem Ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
                 ut labore et dolore magna aliqua. Ut enim ad minim veniam ut aliquip ex ea commodo consequat""")
    st.number_input("Nombre d'heures contractuelles travaillées le dimanche", step=1, format="%i")
    with st.expander("En savoir plus"):
        st.write("""Lorem Ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
                 ut labore et dolore magna aliqua. Ut enim ad minim veniam ut aliquip ex ea commodo consequat""")
    st.number_input("Nombre d'heures complémentaires travaillées le dimanche", step=1, format="%i")
    with st.expander("En savoir plus"):
        st.write("""Lorem Ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
                 ut labore et dolore magna aliqua. Ut enim ad minim veniam ut aliquip ex ea commodo consequat""")
    st.number_input("Nombre d'heures contractuelles travaillées de nuit", step=1, format="%i")
    with st.expander("En savoir plus"):
        st.write("""Lorem Ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
                 ut labore et dolore magna aliqua. Ut enim ad minim veniam ut aliquip ex ea commodo consequat""")
    st.number_input("Nombre d'heures complémentaires travaillées de nuit", step=1, format="%i")
    with st.expander("En savoir plus"):
        st.write("""Lorem Ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
                 ut labore et dolore magna aliqua. Ut enim ad minim veniam ut aliquip ex ea commodo consequat""")

st.divider()

with st.container():
    salaire_brut = 1400
    st.subheader("J'obtients mon salaire :")
    st.write("Mon salaire brut mensuel est de "+str(salaire_brut)+"€")  