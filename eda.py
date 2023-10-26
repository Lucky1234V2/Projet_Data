import warnings
warnings.simplefilter('ignore')

import pandas as pd

data = pd.read_csv("datasets/used_cars_data.csv")
shape = data.shape

#print(shape)
head = data.head()
#print (head)
tail = data.tail()
#print(tail)

#print(data.info())
#print(data.nunique())
#print(data.isnull().sum())

#data = data.drop(['S.No.'],axis=1)
#print(data.info())
