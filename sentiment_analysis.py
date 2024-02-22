import spacy
import pandas as pd
import string
import spacytextblob
from textblob import TextBlob
from spacytextblob.spacytextblob import SpacyTextBlob
#import csv


# Loading model in spacy

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe("spacytextblob")



# importing dataset and checking database information

data = pd.read_csv('/Users/namusale/Documents/bootcamp/bootcamp_tasks/task_21/amazon_product_reviews.csv')
#print(data.head())
#print(data.info())
#print(data.isnull().sum())


# Data preprocessing

clean_data = data.dropna(subset =["reviews.text"]) # removing missing values from dataset
review_data = clean_data['reviews.text'] # trimming dataset to only contain reviews column
#print(review_data[600])

data_lower_cased = []
data_stopless =[]

#Lowercasing  data in the dataset

for item in range(0,len(review_data)):
    lower_case = review_data[item].lower()
    data_lower_cased.append(lower_case)

    
# removing stopwords,punctuations and empty spaces from text entries
    
for item in range(0,len(data_lower_cased)):
    token_list = []
    for token in nlp(data_lower_cased[item].strip()):
        if not (token.is_stop or token.is_punct or token.is_space):
            token_list.append(str(token.lemma_))
    #print(token_list)
    data_stopless_entry = (" ".join(token_list))
    data_stopless.append(data_stopless_entry)
        
          

# Sentiment Analysis of text

def sentiment_analysis(senti):
    doc = nlp(senti)
    return doc._.blob.sentiment,senti


# Function for testing similarity of texts

def check_similarity(text1,text2):
    similarity = nlp(text1).similarity(nlp(text2))
    return similarity,text1,text2

# Texts to test the sentment analysis function

testing_list =[data_stopless[10],data_stopless[100],data_stopless[200],data_stopless[500],data_stopless[600]]

# Checking polarity values for testing list
for i in range(0,len(testing_list)):
    print(sentiment_analysis(testing_list[i]))


#Checking similarity between text
  
for i in range(0,len(testing_list[:3])):
    for j in range(0,len(testing_list[:3])):
        print(check_similarity(testing_list[:3][i],testing_list[:3][j]))


