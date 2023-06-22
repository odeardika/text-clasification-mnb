import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re
import pandas as pd


def lowerCaseAndNoNumber(list):
    aftrerLower = []
    for sentence in list :
        noNumber = ""
        for word in sentence:
            if word.isdigit() == False :
                noNumber += word
        noNumber = noNumber.lower()
        aftrerLower.append(noNumber)
    return aftrerLower

def punctuationRemover(list):
    noPunctuation = []               
    for i in list:
        #^ = negasi  
        #\s = white space  
        #\w = word character
        clean = re.sub(r"[^\w\s]", "", i) 
        noPunctuation.append(clean)
    
    return noPunctuation

def emojiRemover(list):
    noEmoji = []
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                    "]+", re.UNICODE)
    for i in list:
        clean = re.sub(emoj, "", i)
        noEmoji.append(clean)
    
    return noEmoji

def normalization(list):
    normalText = []
    for sentence in list:
         #\1 char pertama dari char yang diulang
         #\1+ char yang berulang
        tempNormal =  re.sub(r'(\w)\1+', r'\1', sentence) 
        normalText.append(tempNormal)
    
    return normalText

def split_sentence(sentence):
    result = []
    while(len(sentence) >= 5000):
        i = 5000
        while(sentence[i] != ' '):
            i-=1
        temp = sentence[:i]
        print(temp)
        result.append(temp)
        sentence = sentence[i:]
    result.append(sentence)
    print(sentence)
    return result

from mtranslate import translate
def translate_to_indo(data):
    result = []
    for sentence in data:
        if(len(sentence) >= 5000):
            temp = ' '
            list_sentence = split_sentence(sentence)
            for i in list_sentence:
               temp = temp + translate(i, 'id')
        else:
            temp = translate(sentence, 'id')
        result.append(temp)
        
    return result

def tokenization(list):
    token = []
    for sentence in list:
        tempToken = []
        for word in sentence.split():
            tempToken.append(word)
        token.append(tempToken)
    return token

def stopWord(list):
    stopwordIndo = set(stopwords.words('indonesian'))
    
    afterStopwords = []
    for sentence in list :
        tempFilter = []
        for word in sentence:
            if word not in stopwordIndo:
                tempFilter.append(word)
        afterStopwords.append(tempFilter)
    
    return afterStopwords

def stemming(list):
    stemFactory = StemmerFactory()
    nazief = stemFactory.create_stemmer('nazief')
    
    stem = []
    for data in list:
        tempStem = []
        for word in data:
            tempStem.append(nazief.stem(word))
        stem.append(tempStem)
        
    return stem

def wordSort(lists):
    words = []
    for Doc in lists:
        # print(Doc)
        for word in Doc:
            # print(word)
            if word not in words:
                # print(type(word))
                words.append(word)
                # print(words)

    words.sort()
    
    return words

import math
def TFIDF(list, words):
    #banyak dokumen
    #term frecuency
    tf = []
    for doc in list:
        tempDoc = [1 for i in range(len(words))]
        for word in doc:
            tempDoc[words.index(word)] += 1
        tf.append(tempDoc)
    n = len(list) 
    df = [0 for i in range(len(words))]
    for doc in list:
        for word in set(doc):
            if word in words:
                index = words.index(word)
                df[index] =+ 1
    
    idf = [0 for i in range(len(words))]
    for i in range(len(df)):
        if df[i] > 0:
            idf[i] = math.log(n/df[i])
    
    tf_idf = []
    for subList in range(len(tf)):
        tempTFIDF = []
        for i in words:
            a = tf[subList][words.index(i)]
            b = idf[words.index(i)]
            tempTFIDF.append(a*b)
        tf_idf.append(tempTFIDF)
    
    tf_idf = pd.DataFrame(tf_idf, index=["Dokumen" + str(i+1) for i in range(len(tf_idf))])
    for i in range(len(words)):
        tf_idf = tf_idf.rename(columns={i:words[i]})
    
    return tf_idf
