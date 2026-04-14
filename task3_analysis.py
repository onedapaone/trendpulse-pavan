import numpy as np
import pandas as pd

#1 — Load and Explore
'''
Load data/trends_clean.csv into a Pandas DataFrame
Print the first 5 rows
Print the shape of the DataFrame (rows and columns)
Print the average score and average num_comments across all stories
'''

df = pd.read_csv("./data/trends_clean.csv")
print("First 5 rows of the Data:\n", df.head(5))
print("Shape of the Data Frame: ", df.shape)
print(f"Average Score: {df['score'].mean():.2f} \nAverage Comments: {df['num_comments'].mean():.2f}")

#2 — Basic Analysis with NumPy
'''
What is the mean, median, and standard deviation of score?
What is the highest score and lowest score?
Which category has the most stories?
Which story has the most comments? Print its title and comment count.
'''
#What is the mean, median, and standard deviation of score?
#What is the highest score and lowest score?
score = df["score"].to_numpy()

print(f'''
Mean of the Score: {score.mean():.2f}
Median of the score: {np.median(score):.2f}
Standard Deviation of the score: {score.std():.2f}
Highest Score: {score.max()}
Lowest Score: {score.min()}
      '''
      )

#Which category has the most stories?
CategoryWithMostStories = df['category'].value_counts().idxmax()
count = df['category'].value_counts().max()
print(f"Most stories in: '{CategoryWithMostStories}' category with {count} stories")


#Which story has the most comments? Print its title and comment count.
max_comments = df['num_comments'].max()
top_title = df[df['num_comments'] == max_comments]
print(f"Most Commented Story: '{top_title['title'].values[0]}' - {max_comments} comments") 


#3-Add New Columns

'''
Add these two new columns to your DataFrame:

Column	Formula
engagement	num_comments / (score + 1) — how much discussion a story gets per upvote
is_popular	True if score > average score, else False
'''

df['engagement'] = df['num_comments'] / (df['score'] + 1)

df['is_popular'] = df['score'] > df['score'].mean() 


#4 — Save the Result
'''
Save the updated DataFrame (with the 2 new columns) to data/trends_analysed.csv
Print a confirmation message
'''

df.to_csv("./data/trends_analysed.csv")
print("Updated Data frame saved to data/trends_analysed.csv")