import pandas as pd


test = pd.DataFrame([1,2,3,4,5],index=[f'test-{i}' for i in range(5)])
print(test.transpose())