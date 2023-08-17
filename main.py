import pandas as pd
import streamlit as st



st.set_page_config(
    page_title="MY_COST",
    page_icon="💰",
    layout="wide"
)



private_gsheets_url='''https://docs.google.com/spreadsheets/
d/1uFiN9FccfKZilmfi8zV2zhuN4tdZgmNRDHItoHTP1Dg/edit?usp=sharing'''



st.title('FOR HAPPINESS........')


with st.form('form 1'):
    c1,c2=st.columns(2)
    c1.text_input('HOW ?')
    c2.text_input('HOW MUCH ?')
    st.selectbox('CATEGORY',options={'food','college','other'})
    st.form_submit_button()
