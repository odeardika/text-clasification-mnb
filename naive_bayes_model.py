from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score
import joblib
import pandas as pd

def model_prediction_accuracy(X, y, model_name):
    # split the data to train data and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2 , # Train Data 80:20 Test Data
                                                    random_state=42)
    model = MultinomialNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    f1 = f1_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)

    joblib.dump(model, f'model_naive_bayes/model_{model_name}.pkl')
    
    return [f1,recall,precision,accuracy]