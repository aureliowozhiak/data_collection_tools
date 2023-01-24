import pandas as pd
import pandas_profiling
import streamlit as st

from streamlit_pandas_profiling import st_profile_report

class ModelIndex:
    

    def __init__(self):
        pass

    def get_default_data(self, file, decimal=",", sep=";"):
        return pd.read_csv(file, sep=sep, decimal=decimal)
    
    def generate_st_profile_report(self, df):
        st_profile_report(df.profile_report())
            


