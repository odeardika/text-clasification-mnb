import streamlit as st
import review_backend as rb
import joblib
import pandas as pd

model = joblib.load("D:/Project/PPDM/text-clasification-mnb-master/train_model_reviews.pkl")
df = pd.read_csv("D:/Project/PPDM/text-clasification-mnb-master/BOW_result.csv").iloc[:,1:]

st.title('Review Checker')
review = st.text_input('Input Reviews : ',value='')
if st.button("Classify"):
    input = rb.preprocess(review)
    result = rb.check_emotion(df, model, input)
    st.write("Emosi dari review diatas adalah : " + result)