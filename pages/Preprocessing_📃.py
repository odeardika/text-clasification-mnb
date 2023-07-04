import streamlit as st
import pandas as pd
import system
import preprocessing_backend as preback

# if st.button('Press this to update data'):
#     preback.do_preprocessing()


review_datas = pd.read_excel('reviews.xlsx')
reviews = review_datas['Reviews'][:10]
label_reviews = review_datas['Label'][:10]

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
reviews = pd.read_csv('Result_Preprocessing/Stem_result.csv').iloc[:,1:]
st.table(reviews[:10])

st.write('Sorted Word')
list_word_sorted = pd.read_csv('Result_Preprocessing/Word Sorted_result.csv').iloc[:,1:]
reviews = [i for i in reviews]
st.table(list_word_sorted[:30])

st.title('One Hot Encoder vectorization')
one_hot = pd.read_csv('Result_Preprocessing/One Hot Encoder_result.csv').iloc[:,1:]
st.table(one_hot[:10])

st.title('Bag Of Word vectorization')
Bag_of_word = pd.read_csv('Result_Preprocessing/BOW_result.csv').iloc[:,1:]
st.table(Bag_of_word[:10])

st.title('TF-IDF vectorization')
TFIDF = pd.read_csv('Result_Preprocessing/tfidf_result.csv').iloc[:,1:]
st.table(TFIDF[:10])
    
st.pyplot(system.show_prediction())

