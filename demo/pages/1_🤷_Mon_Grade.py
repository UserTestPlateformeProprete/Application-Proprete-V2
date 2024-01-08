import streamlit as st


st.set_page_config(
    page_title="Mon Grade",
    page_icon="📖",
)


st.write("# Tout savoir sur mon Grade")
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")

with tab1:
    st.button('Hit me:question:')
    st.checkbox('Check me out')
    st.radio('Pick one:', ['nose', 'ear'])
    st.selectbox('Select', [1, 2, 3])
    st.multiselect('Multiselect', [1, 2, 3])
    st.slider('Slide me', min_value=0, max_value=10)
    st.select_slider('Slide to select', options=[1, '2'])
    st.text_input('Enter some text')
    st.number_input('Enter a number')
    st.text_area('Area for textual entry')
    st.date_input('Date input')
    st.time_input('Time entry')
    st.color_picker('Pick a color')

with tab2:
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        box1 = st.container()
        with box1 :
            st.write('This is column 1')
    with col2:
        st.write('This is column 2')
        st.code("This is column 2")
    with col3:
        st.write('This is column 3')