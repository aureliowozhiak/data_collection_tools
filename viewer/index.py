import streamlit as st
from streamlit_option_menu import option_menu

class ViewerIndex:

    # Reduz os espaços em branco nos cabeçalhos para melhroar a usabilidade
    PADDING = 0
    st.markdown(f""" <style>
        .reportview-container .main .block-container{{
            padding-top: {PADDING}rem;
            padding-right: {PADDING}rem;
            padding-left: {PADDING}rem;
            padding-bottom: {PADDING}rem;
        }} </style> """, unsafe_allow_html=True)

    def main(self):
        #st.sidebar.title("Data Solutions")
        #with st.sidebar:
        # horizontal Menu
        return option_menu(None, ["Home", "Analysis", 'About', 'Another Tools'], 
            icons=['house', 'graph-up', 'briefcase', 'tools'], 
            menu_icon="cast", default_index=0, orientation="horizontal")


        # oculta o menu de configuração
        #st.markdown(""" <style>
        ##MainMenu {visibility: hidden;}
        #footer {visibility: hidden;}
        #</style> """, unsafe_allow_html=True)

    def page(self):
        st.title("Welcome to the data solutions")

