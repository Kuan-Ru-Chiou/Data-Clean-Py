import pandas as pd
import numpy as np
import re 


def clean_article(x):
    return re.sub('[^A-Za-z0-9\u4e00-\u9fa5]', '',  str(x))

df = pd.read_csv('ptt_sample_data.csv')
df['article_cleaned'] = df['article'].map(clean_article)
df[['article_cleaned', 'article']].head(5)
df.to_csv("clean_data.csv",index = 0)

def top_post_users():
    df = pd.read_csv("ptt_sample_data.csv")
    df = df.dropna()
    top_author = df["author"]
    top_author = top_author.groupby(top_author).count().sort_values()
    top_author = top_author[top_author.values > 1]
    top_author.to_csv("top_author.csv")

top_post_users()
 
def Search_Word():
    df = pd.read_csv("ptt_sample_data.csv")
    df = df.dropna()
    df = df.values
    tuple_inex = df.shape
    for x in range(0, tuple_inex[0]):
        for y in range(0,tuple_inex[1]):
           df[x, y] = str(df[x, y])
    for x in range(0, tuple_inex[0]):
        for y in range(0, tuple_inex[1]):
          df[x, y] = re.sub('[^A-Za-z0-9\u4e00-\u9fa5]', '',  df[x, y])
    df = pd.DataFrame(df)
    return df[df[1].str.contains("情報", na = False)]
    
Search_String = Search_Word()
Search_String.to_csv("Search_String.csv", index = 0)
