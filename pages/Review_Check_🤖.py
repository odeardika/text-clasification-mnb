import streamlit as st
import review_backend as rb
import joblib
import pandas as pd

model = joblib.load("model_naive_bayes/model_bow.pkl")
df = pd.read_csv("Result_Preprocessing/BOW_result.csv").iloc[:,1:]

st.title('Review Checker')
review = st.text_input('Input Reviews : ',value='')
if st.button("Classify"):
    input = rb.preprocess(review)
    result = rb.check_emotion(df, model, input)
    st.write("Emosi dari review diatas adalah : " + result)