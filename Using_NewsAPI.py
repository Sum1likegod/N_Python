import requests as re

import json as jn

import pyshorteners

queryy = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={queryy}&from=2024-07-06&language=en&sortBy=publishedAt&apiKey=9355f3b02376442a80557318d8e91c50"

s = pyshorteners.Shortener()
response = re.get(url)
data = jn.loads(response.text)
for i, article in enumerate(data['articles']):
    print(f"{i+1}.Here is the tittle of news on the topic of {queryy}\n", "\t\t", article['title'])
    short_url = s.tinyurl.short(article['url'])
    print("And here is the link to it -\t\t", short_url)
    print("Some description about the news is:- \n", article['description'])
    print("-------------------------------------------------------")
    if i == 4:
        break