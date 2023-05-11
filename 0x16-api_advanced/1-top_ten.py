#!/usr/bin/python3
"""queries the Reddit API"""
import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the first 10
    hot posts listed for a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alx"}
    params = {"limit": 10}

    res = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

    if res.status_code == 404:
        print(None)
        return

    posts = res.json()["data"]["children"]

    for post in posts:
        print(post["data"]["title"])
