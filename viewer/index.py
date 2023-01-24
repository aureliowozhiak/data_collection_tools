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
        return option_menu(None, ["Home", "Upload", 'About'], 
            icons=['house', 'cloud-upload', 'briefcase'], 
            menu_icon="cast", default_index=0, orientation="horizontal")


        # oculta o menu de configuração
        #st.markdown(""" <style>
        ##MainMenu {visibility: hidden;}
        #footer {visibility: hidden;}
        #</style> """, unsafe_allow_html=True)

    def home(self):
        st.title("Welcome to the data solutions")


    def about(self):
        st.title("About")
        st.write("""
        Our data consulting project involves helping retail companies optimize their sales forecasting and data collection processes. We will review current methods, design a new data collection system, improve forecasting models using advanced statistical techniques, and provide ongoing support and monitoring. Our goal is to help companies make better data-driven decisions to drive business growth.
        """)