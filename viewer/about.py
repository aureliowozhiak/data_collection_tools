import streamlit as st
from streamlit_option_menu import option_menu

class ViewerAbout:

    def page(self):
        st.title("About")
        st.write("""
        Our data consulting project involves helping retail companies optimize their sales forecasting and data collection processes. We will review current methods, design a new data collection system, improve forecasting models using advanced statistical techniques, and provide ongoing support and monitoring. Our goal is to help companies make better data-driven decisions to drive business growth.
        """)