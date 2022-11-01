# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 10:55:13 2022

@author: Kolawole Olanrewaju
"""

import streamlit as st
import pickle
from streamlit_option_menu import option_menu
from sklearn.feature_extraction.text import TfidfVectorizer




spam_mail= pickle.load(open("spam.sav","rb"))


with st.sidebar:
    selected= option_menu("Mail Prediction System",
                          ["Spam Mail Prediction System"],
                          icons=["activity"],
                          default_index=0)
    
if (selected == 'Spam Mail Prediction System'):
    # page title
    st.title('Spam Mail Prediction System using ML')
    
    #Mail= st.text_input('Enter Mail Message')
    Message= st.text_input('Enter Mail Message')
    
    #vectorizer= TfidfVectorizer(min_df=1,stop_words="english",lowercase=True)
    
    #Message= vectorizer.fit_transform(Mail)
    
    
    spam_mail_= ""
    
    if st.button('Mail Result'):
      Spam_Mail_Prediction= spam_mail.predict([[Message]])
      
      if (Spam_Mail_Prediction[0]==1):
          spam_mail_="This Mail is Spam"
          
      else:
          spam_mail_="This Mail is Not Spam"
          
    st.success(spam_mail_)
    
    
