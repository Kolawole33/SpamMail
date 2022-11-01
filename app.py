# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 10:55:13 2022

@author: Kolawole Olanrewaju
"""

import streamlit as st
import pickle
from streamlit_option_menu import option_menu

spam_mail= pickle.load(open("spam.sav","rb"))

with st.sidebar:
    selected= option_menu("Prediction System",[
        "Spam Mail"],
        icons=["activity"],
        default_index=0)

if (selected == 'Spam Mail'):
    
    # page title
    st.title('Spam Mail using ML')
    
    
    # getting the input data from the user
    col1= st.columns(1)
    
    with col1:
        Message = st.text_input('Enter Your Mail')
    
    mail_spam= ""
    
if st.button('Spam Mail Result'):
    spam_prediction= spam_mail.predict([[Message]])
        
    if (spam_prediction[0] ==1):
        mail_spam="This Mail is Spam"
    else:
        mail_spam="This Mail is Not Spam"
        
st.sucess(mail_spam)
            
        