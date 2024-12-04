# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:52:39 2024

@author: GuillermoLopez
"""
import openai
import requests
import os
import tweepy

# OpenAI setup
XAI_API_KEY = os.getenv("xxxxxxxxx")  # Use actual environment variable name
openai.api_key = XAI_API_KEY

def answer_question(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an intelligent assistant."},
            {"role": "user", "content": question},
        ],
    )
    return response.choices[0].message["content"]

print(answer_question("What is the capital of France?"))

# Bing API setup
def search_web(query):
    api_key = os.getenv("xxxxxxxxx")  # Use environment variable for security
    url = f"https://api.bing.microsoft.com/v7.0/search?q={query}"
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get("webPages", {}).get("value", [])
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return []

results = search_web("Latest AI trends")
for result in results:
    print(f"{result['name']}: {result['url']}")

# Tweepy setup
TWITTER_BEARER_TOKEN = os.getenv("xxxxxxxxx")  # Use env var for security
twitter_client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)

def brainstorm_from_twitter(topic):
    tweets = twitter_client.search_recent_tweets(query=topic, max_results=10)
    if tweets.data:
        return [tweet.text for tweet in tweets.data]
    return []

print(brainstorm_from_twitter("AI innovation"))

# Grok lite function
def grok_lite(input_type, content):
    if input_type == "question":
        return answer_question(content)
    elif input_type == "search":
        return search_web(content)
    elif input_type == "brainstorm":
        return brainstorm_from_twitter(content)
    else:
        return "Invalid input type."
