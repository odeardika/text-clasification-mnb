import system


def preprocess(reviews):
    reviews = system.lowerCaseAndNoNumber(reviews)
    reviews = system.emojiRemover(reviews)
    reviews = system.punctuationRemover(reviews)
    reviews = system.normalization(reviews)
    reviews = system.no_abbreviation(reviews)
    reviews = system.translate_to_indo(reviews)
    reviews = system.tokenization(reviews)
    reviews = system.stopWord(reviews)
    reviews_stem = system.stemming(reviews)
    reviews_word = system.wordSort(reviews_stem)
    BoW_reviews = system.basicBow(reviews_stem,reviews_word).transpose()
    return BoW_reviews

def check_emotion(df, model, input):
    input = input.reindex(columns=df.columns, fill_value=0)
    prediction = model.predict(input)
    label_to_emotion = {
        0: "sad",
        1: "happy",
    }

    return label_to_emotion[prediction[0]]