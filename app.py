from view.web.web_view import WebView
import streamlit as st

st.markdown(WebView.index(), unsafe_allow_html=True)