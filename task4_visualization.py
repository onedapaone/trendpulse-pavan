#TrendPulse: What's Actually Trending Right Now
#Task 4 — Visualizations

#Load the CSV from Task 3 and create 3 charts using Matplotlib. 
# Then combine them into a single dashboard figure. 
# Save everything as PNG files.

#1 — Setup 
'''
Load data/trends_analysed.csv into a DataFrame
Create a folder called outputs/ if it doesn't exist
Use plt.savefig() before any plt.show() on all charts
'''
import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("./data/trends_analysed.csv")
os.makedirs("./outputs", exist_ok=True)

#2 — Chart 1: Top 10 Stories by Score 
'''
Create a horizontal bar chart showing the top 10 stories by score
Use the story title on the y-axis (shorten titles longer than 50 characters)
Add a title and axis labels
Save as outputs/chart1_top_stories.png
'''
top_10 = df.sort_values('score', ascending=False).head(10)
top_10['title'] = top_10['title'].apply(
    lambda x: x if len(x) <= 50 else x[:47] + '...'
)

plt.figure(figsize=(10,6))
bars = plt.barh(top_10['title'], top_10['score'], color='skyblue')
plt.xlabel("Score")
plt.ylabel("Title")
plt.title("Top 10 Stories by Score")
plt.tight_layout()  # ensures labels fit
plt.bar_label(bars, labels=top_10["score"], padding=3)
plt.savefig("./outputs/chart1_top_stories.png")
plt.show()


#3 — Chart 2: Stories per Category
'''
Create a bar chart showing how many stories came from each category
Use a different colour for each bar
Add a title and axis labels
Save as outputs/chart2_categories.png
'''

category_stories = df['category'].value_counts().reset_index()
category_stories.columns = ['category', 'count']
colors = ['red', 'blue', 'green', 'orange','purple']
plt.bar(category_stories['category'], category_stories['count'], color=colors)
plt.xlabel("Category")
plt.ylabel("Story Count")
plt.title("Stories Count by Category")
plt.tight_layout()  # ensures labels fit
plt.savefig("./outputs/chart2_categories.png")
plt.show()


#4 — Chart 3: Score vs Comments 
'''
Create a scatter plot with score on the x-axis and num_comments on the y-axis
Colour the dots differently for popular vs non-popular stories (use the is_popular column)
Add a legend, title, and axis labels
Save as outputs/chart3_scatter.png
'''

# Plot popular stories (green dots)
plt.scatter(
    df[df['is_popular'] == True]['score'],
    df[df['is_popular'] == True]['num_comments'],
    color='green', label='Popular', alpha=0.6
)

# Plot non-popular stories (red dots)
plt.scatter(
    df[df['is_popular'] == False]['score'],
    df[df['is_popular'] == False]['num_comments'],
    color='red', label='Non-Popular', alpha=0.6
)

# Labels and title
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Number of Comments")
plt.legend()

# Save before showing
plt.tight_layout()
plt.savefig("./outputs/chart3_scatter.png")
plt.show()

#Bonus — Dashboard 
'''
Combine all 3 charts into one figure:
Use plt.subplots(1, 3) or plt.subplots(2, 2) to lay them out together
Add an overall title: "TrendPulse Dashboard"
Save as outputs/dashboard.png
'''
fig, axs = plt.subplots(1, 3, figsize=(18, 6))
# Chart 1: Top 10 Stories by Score
bars = axs[0].barh(top_10['title'], top_10['score'], color='skyblue')
axs[0].set_xlabel("Score")
axs[0].set_ylabel("Title")
axs[0].set_title("Top 10 Stories by Score")
axs[0].bar_label(bars, labels=top_10["score"], padding=3)
# Chart 2: Stories per Category
axs[1].bar(category_stories['category'], category_stories['count'], color=colors)
axs[1].set_xlabel("Category")
axs[1].set_ylabel("Story Count")
axs[1].set_title("Stories Count by Category")
axs[1].tick_params(axis='x', rotation=45)
# Chart 3: Score vs Comments
axs[2].scatter(
    df[df['is_popular'] == True]['score'],
    df[df['is_popular'] == True]['num_comments'],
    color='green', label='Popular', alpha=0.6
)
axs[2].scatter(
    df[df['is_popular'] == False]['score'],
    df[df['is_popular'] == False]['num_comments'],
    color='red', label='Non-Popular', alpha=0.6
)
axs[2].set_xlabel("Score")
axs[2].set_ylabel("Number of Comments")
axs[2].set_title("Score vs Number of Comments")
axs[2].legend()
plt.suptitle("TrendPulse Dashboard", fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to fit the suptitle
plt.savefig("./outputs/dashboard.png")
plt.show()


