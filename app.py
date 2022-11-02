# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 10:55:13 2022

@author: Kolawole Olanrewaju
"""

import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
import re
from streamlit_option_menu import option_menu



spam_mail= pickle.load(open("spam.sav","rb"))


port_stem= PorterStemmer()

def stemming(content):
    stemmed_content = re.sub("[^a-zA-Z]"," ",content)
    stemmed_content= stemmed_content.lower()
    stemmed_content= stemmed_content.split()
    stemmed_content=[port_stem.stem(word) for word in stemmed_content if not word in stopwords.words("english")]
    stemmed_content=" ".join(stemmed_content)
    return stemmed_content


with st.sidebar:
    selected= option_menu("Mail Prediction System",
                          ["Spam Mail Prediction System"],
                          icons=["activity"],
                          default_index=0)
   
if (selected == 'Spam Mail Prediction System'):
    # page title
    st.title('Spam Mail Prediction System using ML')
    
    Mail= st.text_input('Enter Mail Message')
    #Message= st.text_input('Enter Mail Message')
    
    Mess= stemming(Mail)
    
    
    
    spam_mail_= ""
    
    if st.button('Mail Result'):
      Spam_Mail_Prediction= spam_mail.predict([[Mess]])
      
      if (Spam_Mail_Prediction[0]==1):
          spam_mail_="This Mail is Spam"
          
      else:
          spam_mail_="This Mail is Not Spam"
          
    st.success(spam_mail_)
    
