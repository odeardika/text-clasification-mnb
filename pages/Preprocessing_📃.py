import streamlit as st
import pandas as pd
import system
from naive_bayes_model import model_prediction_accuracy 

review_datas = pd.read_excel('reviews.xlsx')
reviews = review_datas['Reviews']
label_reviews = review_datas['Label']

st.write('Data Reviews')
st.table(pd.concat([reviews,label_reviews], axis=1)[:30])

st.title('PreProcessing')
st.write('Lowercase and Number Cleaning')
reviews = system.lowerCaseAndNoNumber(reviews[:10])
st.table(reviews[:10])

reviews = system.emojiRemover(reviews)
st.write('Clean the emoji')
st.table(reviews[:10])

reviews = system.punctuationRemover(reviews)
st.write('Remove punctuation')
st.table(reviews[:10])

reviews = system.normalization(reviews)
st.write('Normalizing some word')
st.table(reviews[:10])

reviews = system.no_abbreviation(reviews)
st.write('Remove abbreviation')
st.table(reviews[:10])

reviews = system.translate_to_indo(reviews)
st.write('Translate to Indonesia')
st.table(reviews[:10])

reviews = system.tokenization(reviews)
st.write('Tokenizing the sentence')
st.table(reviews[:10])

st.write('Stopword')
reviews = system.stopWord(reviews)
st.table(reviews[:10])

st.write('Stemming')
reviews = system.stemming(reviews)
st.table(reviews[:10])

st.write('Sorted Word')
list_word_sorted = system.wordSort(reviews)
st.table(list_word_sorted)

st.title('One Hot Encoder vectorization')
one_hot = system.oneHotEncoder(reviews, list_word_sorted)
st.table(one_hot)

st.title('Bag Of Word vectorization')
Bag_of_word = pd.read_csv('TFIDF_result')
st.dataframe(Bag_of_word[:10])

st.title('TF-IDF vectorization')
TFIDF = system.TFIDF(reviews,list_word_sorted)
st.table(TFIDF)
    
TFIDF = Bag_of_word.drop(Bag_of_word.columns[-1], axis=1)
st.table(TFIDF[:10])
prediction_tfidf = model_prediction_accuracy(X=TFIDF[:10],y=label_reviews[:10])
st.table(prediction_tfidf)


