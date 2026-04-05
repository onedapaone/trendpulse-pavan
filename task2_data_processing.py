import json
import pandas as pd
import numpy as np

#Task 1 — Load the JSON File
df = pd.read_json("./data/trends.json") #Load the JSON file from the data/ folder into a Pandas DataFrame

print("Rows loaded: ", len(df)) #Print how many rows were loaded


#Task 2 Clean the data

#Duplicates — remove any rows with the same post_id
duplicated_ids_count = df['post_id'].duplicated().sum()

if duplicated_ids_count > 0:
    #print(f"Found {duplicated_ids_count} duplicate rows in column post_id and dropping them")
    df.drop_duplicates(subset =['post_id'], inplace=True)
#else:
    #print("No Duplicates for column Post_id")    
print("After removing duplicates: ", len(df))

#Missing values — drop rows where post_id, title, or score is missing

df.dropna(subset=['post_id','title','score'], inplace= True)
print("After removing nulls from post_id or title or score columns: ", len(df))

#Data types — make sure score and num_comments are integers
#Checking data types of score and num_comments columns before conversion
if df['score'].dtype != 'int64':
    df['score'] = df['score'].astype(int)
if df['num_comments'].dtype != 'int64':    
    df['num_comments'] = df['num_comments'].fillna(0).astype(np.int64)

#print("Data types of score and num_comments columns: ", df.dtypes[['score', 'num_comments']])    
 
#Low quality — remove stories where score is less than 5
df.drop(df[df['score']<5].index, inplace = True)
print("After removing low scroes: ", len(df))

#Whitespace — strip extra spaces from the title column
df['title'] = df['title'].str.strip()

#---#
#Task 3 — Save as CSV
df.to_csv("./data/trends_clean.csv", index=False)
print(f"Saved {len(df)} rows to data/trends_clean.csv")

print("Stories per category:\n", df["category"].value_counts())