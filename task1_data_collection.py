import requests
import time as time
import pprint, json
from datetime import datetime

#Step 1 — Get the list of top story IDs:
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url)

topstories_ids = response.json()[:500]

#Step 2 — Get each story's details:

#Category assignment function
categories = {
    "technology": ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
    "entertainment": ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]
}

def assign_category(text):
     if not text:
          return None
     text_lower = text.lower()
     for category, keywords in categories.items():
          for kw in keywords:
               if kw.lower() in text_lower:
                    return category
     return "Others"


stories = [] #Creating a blank List

headers = {"User-Agent": "TrendPulse/1.0"}

#Fetching Each Story
for id in topstories_ids:
    try:
            response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json", headers= headers, timeout=10)
            response.raise_for_status()
            story_data = response.json()
            
            category = assign_category(story_data.get("title"))           
            if category == "Others":
                   continue #Skipping th current story item as it did not match to any of our category
            else:
                   #Custom field mapping if current story item matches to one of our category
                    custom_story ={
                        "post_id" : story_data.get("id"),
                        "title" : story_data.get("title"),
                        "category" : category,
                        "score" : story_data.get("score"),
                        "num_comments" :story_data.get("descendants"),
                        "author" : story_data.get("by"),
                        "collected_at" : datetime.now().isoformat()
                    }
                    stories.append(custom_story)
                    time.sleep(1)
    
    except requests.exceptions.RequestException as e:
            print("Connection Error: ", e)       
            print("Unable to fetch story details for id:", id)    
            time.sleep(0.5)
 
with open("./data/trends.json", "w") as outfile:
    json.dump(stories, outfile, indent=4)

print(f"Collected {len(stories)} stories. Saved to .data/trend.json")  
