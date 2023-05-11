#!/usr/bin/python3
"""This script contains a function that queries the reddit API"""
import json
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'alx'}

    res = requests.get(url, headers=headers)

    if res.status_code == 404:
        return 0
    return res.json()["data"]["subscribers"]
