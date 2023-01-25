import sys
sys.path.append('../')

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

from st_aggrid import AgGrid

from model.index import ModelIndex
from viewer.index import ViewerIndex
from viewer.about import ViewerAbout


from controller.another_tools.math import controllerMath
from viewer.web.another_tools.math import viewMath

from controller.extract.scraper import controllerScraper

from model.data_analysis import DataAnalysis

class ControllerIndex:
    
    def __init__(self):
        self.selected = "Home"
        pass

    def get_main_page(self):
        self.selected = ViewerIndex().main()
        self.get_page()

    def get_page(self):
        if self.selected == 'Home':
            ViewerIndex().page()

        if self.selected == 'Analysis':
            st.title("Analysis page")

            upload_method = st.selectbox("What do you want to do?", ['Upload a new file', 'Load a saved data table'])
            
            if upload_method == "Upload a new file":
                st.session_state['tmp_data'] = pd.DataFrame()
                file = st.file_uploader("Data: ", type=['csv'])
                decimal = st.selectbox('Select the decimal:', ['.',','])
                sep = st.selectbox('Select the separator', [',', ';'])

                if file is not None:
                    st.session_state['tmp_data'] = ModelIndex().get_default_data(file=file, decimal=decimal, sep=sep)
                    DataAnalysis().get_full_analysis(st.session_state['tmp_data'])
                    tmp_name = st.text_input("Name your table")
                    if tmp_name != "":
                        st.session_state[tmp_name] = st.session_state['tmp_data']
                        st.write("your table has been renamed, and is saved in the session (temporarily)")


            if upload_method == 'Load a saved data table':
                st.session_state['tmp_data'] = pd.DataFrame()
                table_date_name = st.selectbox("Select the data table", list(dict(st.session_state).keys()))
                st.session_state['tmp_data'] = st.session_state[table_date_name]
                DataAnalysis().get_full_analysis(st.session_state['tmp_data'])



        if self.selected == 'About':
            ViewerAbout().page()

        if self.selected == 'Another Tools':
            tool_selected = st.selectbox('Select a tool', ['Math Tool', 'Table Scraping', 'Web Scraping'])
            
            if tool_selected == 'Math Tool':
                expression = st.text_input("Enter a math expression")
                result = controllerMath.main(input_value=expression, math_type='calc_expression')
                st.write(viewMath.calc_expression(expression, result), unsafe_allow_html=True)
            
            if tool_selected == 'Table Scraping':
                input_value = st.text_input("Enter the url page")

                if input_value:
                    index_list = []
                    index_list.extend(range(1, len(controllerScraper.main(input_value, 'table_scraping'))))
                    index = int(st.selectbox('Select the table position.', index_list))
                    if index > 0:
                        st.session_state['tmp_data'] = controllerScraper.main(input_value, 'table_scraping', index)
                    
                        st.write(st.session_state['tmp_data'], unsafe_allow_html=True)

                        tmp_name = st.text_input("Name your table")
                        if tmp_name != "":
                            st.session_state[tmp_name] = st.session_state['tmp_data']
                            st.write("your table has been renamed, and is saved in the session (temporarily)")

                

            if tool_selected == 'Web Scraping':
                pass


