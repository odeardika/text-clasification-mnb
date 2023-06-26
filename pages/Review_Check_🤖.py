import streamlit as st

st.title('Review Checker')
review = st.text_input('Input Reviews : ',value='')
if review != '':
    result = 'The Reviews is Positif'
    st.write(result)