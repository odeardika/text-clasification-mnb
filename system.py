import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re
import pandas as pd
from mtranslate import translate
import math
import matplotlib.pyplot as plt
import numpy as np


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

def no_abbreviation(list):
    dictonary = {
        'maf' : 'maaf',
        'tdk' : 'tidak',
        'lgi' : 'lagi',
        'bgta' : 'begitu',
        'ngisknpa' : 'kenapa',
        'ga' : 'tidak',
        'jdi' : 'jadi',
        'rapicuman' : 'rapi cuman',
        'emang' : 'memang',
        'emg' : 'memang',
        'gerahand' : 'gerah dan',
        'bhong' : 'bohong',
        'dri' : 'dari',
        'jga' : 'juga',
        'krna' : 'karena',
        'trlalu' : 'terlalu',
        'bgt' : 'banget',
        'asliny':'asli',
        'yg' : 'yang',
        'dlu' : 'dulu',
        'seler' : 'seller',
        'ky':'kayak',
        'dgn' : 'dengan',
        'baklgus' : 'bagus',
        'yh':'yah',
        'realpict' : 'foto asli',
        'yearbok' : 'yearbook',
        'tingi' : 'tinggi',
        'lgsg':'langsung',
        'cm' : 'cuma',
        'tak' : '',
        'gak' :'tidak',
        'thankyou': 'terimakasih',
        'sih':'',
        'it' : '',
        'nya' : '',
        'ny' : '',
        'karna' : 'karena',
        'bahanya': 'bahan',
        'camera' : 'kamera',
        'thanks' : 'terimakasih',
        'seller' : 'penjual',
        'ya' : '',
        'bukak': 'buka',
        'real' : 'asli',
        'next' : 'lanjut',
        'order' : 'pesanan',
        'deh':'',
        'worth':'bernilai',
        'and' : 'dan',
        'bet': '',
        'dah': '',
        'tebel':'tebal',
        'kak':'kakak',
        'datengnya': '',
        'kasi':'berikan',
        'kainya':'kain',
        'jahitanya':'jahit',
        'dateng' : 'datang',
        'nyampe' : 'sampai',
        'yah': '',
        'se': '',
        
         
    }
    result = []
    for sentence in list:
        pattern =  re.compile(r'\b('+'|'.join(dictonary.keys())+r')\b')        
        temp = pattern.sub(lambda x: dictonary[x.group()], sentence)
        result.append(temp)
    return result

def remove_empty_token(data_list):
    result_data = []
    for document in data_list:
        temp_dokumen = []
        # print(document)
        for token_index in range(len(document)):
            # print(document[token_index])
            if document[token_index] != '':
                temp_dokumen.append(document[token_index])
        result_data.append(temp_dokumen)
    
    return result_data
                
                

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

def TFIDF(list, words):
    #banyak dokumen
    #term frecuency
    tf = []
    for doc in list:
        # list berisi 1
        tempDoc = [1 for i in range(len(words))]
        for word in doc:
            # menambahkan 1 untuk setiap kata yang ditemukan
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
            # tf * idf
            tempTFIDF.append(a*b)
        tf_idf.append(tempTFIDF)
    
    tf_idf = pd.DataFrame(tf_idf, index=["document_" + str(i+1) for i in range(len(tf_idf))])
    for i in range(len(words)):
        tf_idf = tf_idf.rename(columns={i:words[i]})
    
    return tf_idf

def oneHotEncoder(data, word_sorted):
    # One-hot encoding
    one_hot = {}
    for word in word_sorted:
        one_hot[word] = [1 if word in doc else 0 for doc in data]
    # Convert to dataframe
    df = pd.DataFrame(one_hot, index=["document_" + str(i+1) for i in range(len(data))])

    return df.transpose()

def basicBow(data, word_sorted):
            
    # inisialisasi empty array untuk menampung bag-of-words
    bag_of_words = []
    for d in data:
        row = []
        for word in word_sorted:
            count = d.count(word)
            row.append(count)
        bag_of_words.append(row)
    df = pd.DataFrame(bag_of_words, columns=list(word_sorted), 
                      index=["document_" + str(i+1) for i in range(len(data))])
    df = df.transpose()
    return df

def list_to_csv(data, path_and_name):
    pd.DataFrame(data, index=[f'document_{i+1}' for i in range(len(data))]).to_csv(path_and_name)
    

def show_prediction():
    prediction = pd.read_csv('Result_Preprocessing/Prediction_result.csv').iloc[:,1:].transpose()
    print(prediction.iloc[1])
    prediction_bar = []
    for i in range(4):
        temp = []
        for j in prediction.iloc[i]:
            temp.append(round(j * 100,2))
        prediction_bar.append(temp)
    # set width of bar
    barWidth = 0.20
    fig = plt.subplots(figsize =(10, 8))

    # set height of bar
    # f1_score = [0.92 * 100, 0.923077, 0.828025]
    # recall = [28, 10,5]
    # precision = [29, 10, 5]
    # accuracy = [29, 10, 5]

    # Set position of bar on X axis
    br1 = np.arange(len(prediction_bar[0]))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    br4 = [x + barWidth for x in br3]

    # Annotate bar heights
    for i, v in enumerate(prediction_bar[0]):
        plt.text(br1[i] - 0.08, v + 1, str(v), color='black')

    for i, v in enumerate(prediction_bar[1]):
        plt.text(br2[i] - 0.08, v + 1, str(v), color='black')

    for i, v in enumerate(prediction_bar[2]):
        plt.text(br3[i] - 0.08, v + 1, str(v), color='black')

    for i, v in enumerate(prediction_bar[3]):
        plt.text(br4[i] - 0.04, v + 1, str(v), color='black')

    # Make the plot
    plt.bar(br1, prediction_bar[0], color ='r', width = barWidth,
            edgecolor ='grey', label ='F1-Score', data='10')
    plt.bar(br2, prediction_bar[1], color ='g', width = barWidth,
            edgecolor ='grey', label ='Recall')
    plt.bar(br3, prediction_bar[2], color ='b', width = barWidth,
            edgecolor ='grey', label ='Precision')
    plt.bar(br4, prediction_bar[3], color ='c', width = barWidth,
            edgecolor ='grey', label ='Accuracy')
    # Adding Xticks
    plt.xlabel('Text Representation', fontweight ='bold', fontsize = 15)
    plt.ylabel('Prediction Result', fontweight ='bold', fontsize = 15)
    plt.xticks([r + barWidth for r in range(3)],
            ['One Hot Encoder', 'BoW', 'TFIDF'])

    plt.legend(loc='upper right', bbox_to_anchor=(1.20, 1))
    plt.show()
    
    return plt
