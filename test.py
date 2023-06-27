import pandas as pd


# test = pd.DataFrame([1,2,3,4,5],index=[f'test-{i}' for i in range(5)])
# print(test.transpose())

# test = {}
# test['y']= [1,2,3,4,4,5]

# print(test)

# test = ]temp = []
# for i in range(len(test)):
#     if test[i] != ' ':
#         temp.append(test[i])
        
# print(temp)

test = pd.read_csv('Result_Preprocessing/tfidf_result.csv')
print(test.iloc[:,1:])