#!/usr/bin/python3
"""queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API
        returns: number of subscribers for a given subreddit.
        If an invalid subreddit is given, return 0 """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "alx/0.0.1"}

    res = requests.get(url, headers=headers)

    if not res.ok:
        return 0

    json_data = res.json()
    subscribers = json_data.get("data").get("subscribers")

    return subscribers
