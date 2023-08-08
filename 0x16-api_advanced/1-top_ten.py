#!/usr/bin/python3
"""This module contains a function that queries the reddit api"""


import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alx /0.0.2"}

    res = requests.get(url, headers=headers)
    if not res.ok:
        print("None")
        return

    posts = res.json().get("data").get("children")[:10]

    for post in posts:
        print(post["data"]["title"])
