#!/usr/bin/python3
"""queries the Reddit API"""
import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the first 10
    hot posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/top.json".format(subreddit)
    headers = {"User-Agent": "alx"}

    res = requests.get(url, headers=headers)

    posts = res.json()["data"]["children"]

    for post in posts[: 10]:
        print(post["data"]["title"])
