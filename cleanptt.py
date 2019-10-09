import pandas as pd
import numpy as np
import re 

# Read data from csv file
dataset = pd.read_csv("ptt_sample_data.csv")


# delete nan in row (row means horizantal direction)
dataset = dataset.dropna()


# transform DataFrame data to Numpy array
dataset = dataset.values



#Define the Function to clean the bizaare data attribute values.
def Clean(dataset):
# Loop all 2-d array element and transform all the elements to str type data
    tuple_inex = dataset.shape
    for x in range(0, tuple_inex[0]):
        for y in range(0, tuple_inex[1]):
           dataset[x, y] = str(dataset[x, y])
# Loop all 2-d array element and filter all the elements that are special pattern or symbol.
    for x in range(0, tuple_inex[0]):
        for y in range(0, tuple_inex[1]):
          dataset[x, y] = re.sub('[^A-Za-z0-9\u4e00-\u9fa5]', '',  dataset[x, y])
    return pd.DataFrame(dataset)


#Check output dimension is ok or not.
#print(Clean(dataset).shape)



#####Below is the major  output

# 1. Output cleaning data to csv file
Clean(dataset).to_csv("clean data")

# 2. Output the highest Four authors that have more articles in the data
def FourAuthor():
    dataset = pd.read_csv("ptt_sample_data.csv")
    dataset = dataset.dropna()
    A = dataset["author"]
    author = A.groupby(dataset["author"]).count().sort_values()   
    return author
   

fourauthor = FourAuthor()
#print(len(fourauthor))
#print(type(fourauthor))
#fourauthor = fourauthor[53:57]
fourauthor = fourauthor[fourauthor.values > 1]
fourauthor.to_csv("fourauthor")


 # 3. Output the title attribute that has the word "情報*" 
def SearchWord():
    # Search all the titles containing the word "情報"
    dataset = pd.read_csv("ptt_sample_data.csv")
    dataset = dataset.dropna()
    # transform DataFrame data to Numpy array
    dataset = dataset.values
    # Loop all 2-d array element and transform all the elements to str type data
    tuple_inex = dataset.shape
    for x in range(0, tuple_inex[0]):
        for y in range(0,tuple_inex[1]):
           dataset[x, y] = str(dataset[x, y])
# Loop all 2-d array element and filter all the elements that are special pattern or symbol.
    for x in range(0, tuple_inex[0]):
        for y in range(0, tuple_inex[1]):
          dataset[x, y] = re.sub('[^A-Za-z0-9\u4e00-\u9fa5]', '',  dataset[x, y])
    dataset = pd.DataFrame(dataset)
    return dataset[dataset[1].str.contains("情報", na = False)]
    
     


#print(type(SearchWord()))
#print(SearchWord().shape)
SearchString = SearchWord()
SearchString.to_csv("SearchString")



 






