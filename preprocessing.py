import streamlit as st
import pandas as pd
import system

review_datas = pd.read_excel('reviews.xlsx')
reviews = review_datas['Reviews'][:20]
label_reviews = review_datas['Label'][:20]

st.write('Data Reviews')
# st.dataframe(review_datas)
st.table(pd.concat([reviews,label_reviews], axis=1))

st.title('PreProcessing')
st.write('Lowercase and Number Cleaning')
reviews = system.lowerCaseAndNoNumber(reviews)
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
reviews =  system.stopWord(reviews[:10])
st.table(reviews[:10])

st.write('Stemming')
reviews = system.stemming(reviews[:10])
st.table(reviews[:10])

st.write('Sorted Word')
list_word_sorted = system.wordSort(reviews)
st.write(list_word_sorted)

st.title('TF-IDF vectorization')
TFIDF = system.TFIDF(reviews,list_word_sorted)
st.table(TFIDF)
    


