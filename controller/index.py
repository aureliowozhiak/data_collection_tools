import sys
sys.path.append('../')

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

from st_aggrid import AgGrid

from model.index import ModelIndex
from viewer.index import ViewerIndex

class ControllerIndex:

    def __init__(self):
        self.selected = "Home"
        pass

    def get_main_page(self):
        self.selected = ViewerIndex().main()
        self.get_page()

    def get_page(self):
        if self.selected == 'Home':
            st.title("Home page")

        if self.selected == 'Upload':
            st.title("Upload page")
            file = st.file_uploader("Data: ", type=['csv'])

            

            if file is not None:
                st.session_state['data'] = ModelIndex().get_default_data(file)
                #st.dataframe(st.session_state['data'])
                ModelIndex().generate_st_profile_report(st.session_state['data'])

        if self.selected == 'Tasks':
            st.title("Tasks page")

        if self.selected == 'Settings':
            st.title("Settings page")


