import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd


class ViewerIndex:
    st.set_page_config(page_title='Inventory Optimzer', page_icon='📉')

   

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
        return option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
            icons=['house', 'cloud-upload', "list-task", 'gear'], 
            menu_icon="cast", default_index=0, orientation="horizontal")


        # oculta o menu de configuração
        #st.markdown(""" <style>
        ##MainMenu {visibility: hidden;}
        #footer {visibility: hidden;}
        #</style> """, unsafe_allow_html=True)