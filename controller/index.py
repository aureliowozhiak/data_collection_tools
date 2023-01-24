import sys
sys.path.append('../')

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

from st_aggrid import AgGrid

from model.index import ModelIndex
from model.linear_regression import ModelLinearRegressionForecast
from viewer.index import ViewerIndex
from viewer.linear_regression import ViewerLinearRegressionForecast

class ControllerIndex:

    def __init__(self):
        self.selected = "Home"
        pass

    def get_main_page(self):
        self.selected = ViewerIndex().main()
        self.get_page()

    def get_page(self):
        if self.selected == 'Home':
            ViewerIndex().home()

        if self.selected == 'Upload':
            st.title("Upload page")
            file = st.file_uploader("Data: ", type=['csv'])
            decimal = st.selectbox('Select the decimal:', [',','.'])
            sep = st.selectbox('Select the separator', [',', ';'])

            if file is not None:
                st.session_state['data'] = ModelIndex().get_default_data(file=file, decimal=decimal, sep=sep)
                st.dataframe(st.session_state['data'])

                columns = st.session_state['data'].columns
                
                column_of_date = st.selectbox('What is the date column?', columns)
                column_to_predict = st.selectbox('What do you want to predict?', columns)

                if st.selectbox('Did you find any outliers?', ['No', 'Yes']) == 'Yes':
                    outlier_cutoff = st.number_input('What is the cutoff value for outlier:')
                    df = st.session_state['data']
                    st.session_state['data'] = df[df[column_to_predict] < outlier_cutoff]
                
                periods = int(st.selectbox('How many months do you want to predict into the future?', [3, 6, 9, 12]))
                if st.button("Predict the future"):
                    if periods > 0:
                        lrf = ModelLinearRegressionForecast(
                            df=st.session_state['data'],
                            periods=periods,
                            column_to_predict=column_to_predict,
                            column_of_date=column_of_date)

                        forecast, X_train, y_train, reg = lrf.predict()
                        st.write(forecast)

                        ViewerLinearRegressionForecast().plot(X_train, y_train, reg)


                if st.button("View data report"):
                    #st.dataframe(st.session_state['data'])
                    ModelIndex().generate_st_profile_report(st.session_state['data'])

        if self.selected == 'About':
            ViewerIndex().about()


