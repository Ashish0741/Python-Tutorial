# import pandas as pd

# list Series
# l1 = [1, 2, 3, 4, 5]
# s1 = pd.Series(l1)
# print(s1)

# # dict Series
# dict1 = {1:100, 2:200, 3:300}
# s2 = pd.Series(dict1)
# print(s2)


# # list DataFrame
# df1 = pd.DataFrame(l1)
# print(df1)


# # dict DataFrame
# df2 = pd.DataFrame([dict1])
# print(df2)


# # multi Objects as Series

# # list
# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 6, 7, 8, 9]
# listMul = [list1, list2]


# sListMul = pd.Series(listMul)
# # print(sListMul)
# #using multi dictionary as series
# dic1 = {1:10, 2:20}
# dic2 = {3:30, 4:40}
# dicMul = [dic1, dic2]


# sDicMul = pd.Series(dicMul)
# print(sDicMul)


# # multi Objects as DataFrame
# # using list
# dfListMul= pd.DataFrame(listMul)
# print(dfListMul)


# # using dictionary
# dfDicMul = pd.DataFrame(dicMul)
# print(dfDicMul)
# dicNames = {"name" : ["aman", "atishay", "himani"],
#             "sname": ["sharma", "jain", "bhatheja"]}
# myNamesDataFrame = pd.DataFrame(dicNames)
# print(myNamesDataFrame)


# # Data Indexing
# listNew = [1, 2, 3]
# myIndex = range(3)
# dfAboutPara = pd.DataFrame(data=listNew, index=myIndex)
# dfAboutPara = pd.DataFrame(data=listNew, index=["a", "b", "c"])
# print(dfAboutPara)
# # Daily Lecture - Full stack with Python (FSPYDV0323)


# # Data Accessing
# # loc --> Location
# print(dfAboutPara.loc["b"])

# # iloc --> Index Location
# print(dfAboutPara.iloc[1])


# listFindEl1 = [1, 2, 3, 4, 5]
# listFindEl2 = [6, 7, 8, 9, 0]
# findEleList = [listFindEl1, listFindEl2]

# dfFinfEle = pd.DataFrame(findEleList)
# print(dfFinfEle)
# print("[0][0] location elements -", dfFinfEle[0][0])
# print("[1][2] location elements -", dfFinfEle[1][2])  --> Gives Error
# print("[1][2] location elements -", dfFinfEle.iloc[1][2])

# ============================================================================

# Use of Pandas :

# 1. leverages the power and speed of numpy
# 2. provides highly robust data operations

# Pandas has two types of DS :

# 1. Series : it is one dimensional array with indexes, it stores a single column or row of data in DF.
# 2. Dataframe : it is tabular spreedsheet like structure representing rows each of which contains one or multiple columns.
# 3. DF is combination of series
# ==============================================================================

import numpy as np
import pandas as pd

dict1 = {
    "name": ['ashish', 'shivani', 'yash', 'saloni'],
    "marks": [34, 56, 78, 90],
    "city": ['mumbai', 'nashik', 'pune', 'goa']
}

# creating data frame for above dictionary

df = pd.DataFrame(dict1)
print(df)

# convert data frame to csv file

# df.to_csv('DAY_26/friends.csv')

# here , index = row

# to remove index

# df.to_csv('DAY_26/friends_index_false.csv',index=False)

# to check head & tail of data frame

print(df.head(2))

print(df.tail(2))

print(df.describe())   # this will give min, max , count , etc of all int column


# read csv

df_csv = pd.read_csv("DAY_26/friends_index_false.csv")
print(df_csv)

print(df_csv['name'][0])

# change index format

# df_csv.index = ["first","second","third","fourth"]

# print(df_csv)


# Series vs DF:

ser = pd.Series(np.random.rand(34))

print(ser)

print(type(ser))

newdf = pd.DataFrame(np.random.rand(334,5), index=np.arange(334))

print(newdf.head())

print(type(newdf))

print(newdf.index)

print(newdf.columns)

print(newdf.to_numpy())  # convert to array

# sort
print(newdf.sort_index(axis=0,ascending=False).head())  # by default ascending is true

# loc function :

print(newdf.loc[0,0])

# to drop column 

newdf = newdf.drop(0,axis=1)

print(newdf)

# updating existing values :

print(newdf.loc[[1,2],[3,4]])  # this is use when column contains any charcter # loc[[row],[column]]

print(newdf.loc[:,[3,4]])

print(newdf.loc[(newdf[1]<0.3) & (newdf[4]>0.4)])  # condition based

# to get index value

print(newdf.iloc[0,3])

print(newdf.iloc[[1,3],[1,2]])  # iloc[[row],[column]]

# print(newdf.drop(0,axis=1,inplace=True))   --> this will change df inplace

newdf.drop([1,5],axis=0,inplace=True)

print(newdf)

print(newdf.reset_index())  # reset index and this will add one extra column of index

newdf.reset_index(drop=True,inplace=True) # this will help to remove extra index column

print(newdf)

print(newdf.shape)

print(newdf.info())

print(newdf[1].value_counts())

