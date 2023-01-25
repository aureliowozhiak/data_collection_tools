import streamlit as st

from model.linear_regression import ModelLinearRegressionForecast
from viewer.linear_regression import ViewerLinearRegressionForecast

from model.index import ModelIndex

class DataAnalysis:

    def get_full_analysis(self, data):
        if not data.empty: 
            st.dataframe(data)      
            columns = data.columns      
            column_of_date = st.selectbox('What is the date column?', columns)
            column_to_predict = st.selectbox('What do you want to predict?', columns)       
            if st.selectbox('Did you find any outliers?', ['No', 'Yes']) == 'Yes':
                outlier_cutoff = st.number_input('What is the cutoff value for outlier:')
                df = data
                data = df[df[column_to_predict] < outlier_cutoff]       
            periods = int(st.selectbox('How many months do you want to predict into the future?', [3, 6, 9, 12]))
            if st.button("See Linear Regression"):
                if periods > 0:
                    lrf = ModelLinearRegressionForecast(
                        df=data,
                        periods=periods,
                        column_to_predict=column_to_predict,
                        column_of_date=column_of_date)      
                    forecast, X_train, y_train, reg = lrf.predict()
                    st.write(forecast)      
                    ViewerLinearRegressionForecast().plot(X_train, y_train, reg)        
            if st.button("View data report"):
                #st.dataframe(data)
                ModelIndex().generate_st_profile_report(data)