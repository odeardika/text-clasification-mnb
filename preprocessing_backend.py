import pandas as pd
import system
from  naive_bayes_model import model_prediction_accuracy

def do_preprocessing():
    review_datas = pd.read_excel('reviews.xlsx')
    reviews = review_datas['Reviews']
    label_reviews = review_datas['Label']

    reviews = system.lowerCaseAndNoNumber(reviews)
    print(1)
    reviews = system.emojiRemover(reviews)
    print(2)
    reviews = system.punctuationRemover(reviews)
    print(3)
    reviews = system.normalization(reviews)
    print(4)
    reviews = system.no_abbreviation(reviews)
    print(5)
    # reviews = system.translate_to_indo(reviews)
    print(6)
    reviews = system.tokenization(reviews)
    print(7)
    reviews = system.stopWord(reviews)
    print(8)
    reviews_stem = system.stemming(reviews)
    print(9)
    reviews_stem = system.remove_empty_token(reviews_stem)
    print(system.list_to_csv(reviews_stem,'Result_Preprocessing/Stem_result.csv'))
    print(10)
    reviews_word = system.wordSort(reviews_stem)
    pd.DataFrame(reviews_word).to_csv('Result_Preprocessing/Word Sorted_result.csv')

    print(11)
    print(reviews_word)

    tfidf_result = system.TFIDF(reviews_stem,reviews_word)
    print(tfidf_result)
    tfidf_result.to_csv('Result_Preprocessing/tfidf_result.csv')

    one_hot_result = system.oneHotEncoder(data = reviews_stem, word_sorted= reviews_word).transpose()
    print(one_hot_result)
    one_hot_result.to_csv('Result_Preprocessing/One Hot Encoder_result.csv')

    Bow_result = system.basicBow(data = reviews_stem, word_sorted= reviews_word).transpose()
    print(Bow_result)
    Bow_result.to_csv('Result_Preprocessing/BOW_result.csv')


    temp = pd.read_csv('Result_Preprocessing/tfidf_result.csv').iloc[:,1:]
    tfidf_model = model_prediction_accuracy(X=temp.iloc[:,1:],y=label_reviews)
    temp = pd.read_csv('Result_Preprocessing/One Hot Encoder_result.csv').iloc[:,1:]
    one_hot_model = model_prediction_accuracy(X=temp.iloc[:,1:],y=label_reviews)
    temp = pd.read_csv('Result_Preprocessing/BOW_result.csv').iloc[:,1:]
    bow_model = model_prediction_accuracy(X=temp.iloc[:,1:],y=label_reviews)

    model_result = [one_hot_model,bow_model,tfidf_model]
    model_result = pd.DataFrame(model_result, index=['One Hot Encoder','Bag of Words','TFIDF'], columns=['F1-Score','Recall','Precision','Accuracy'])
    model_result.to_csv('Result_Preprocessing/Prediction_result.csv')
    print('done')