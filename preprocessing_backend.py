import pandas as pd
import system

review_datas = pd.read_excel('reviews.xlsx')
reviews = review_datas['Reviews']
label_reviews = review_datas['Label']

reviews = system.lowerCaseAndNoNumber(reviews)
reviews = system.emojiRemover(reviews)
reviews = system.punctuationRemover(reviews)
reviews = system.normalization(reviews)
reviews = system.no_abbreviation(reviews)
reviews = system.translate_to_indo(reviews)
reviews = system.tokenization(reviews)
reviews = system.stopWord(reviews)
reviews_stem = system.stemming(reviews)
reviews_stem = system.remove_empty_token(reviews_stem)
reviews_word = system.wordSort(reviews_stem)
# print(reviews_word)

Bow_result = system.basicBow(reviews_stem,reviews_word)
Bow_result.to_csv('Result_Preprocessing/BOW_result.csv')