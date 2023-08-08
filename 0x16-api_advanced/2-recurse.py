#!/usr/bin/python3
"""This module contains a function that querries the reddit api"""
import requests


def recurse(subreddit, hot_list=[], params={"after": None}):
    """queries the Reddit API.
        returns: list of titles of all hot articles for subreddit.
        If no results are found for the given subreddit, return None."""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alx /0.0.3"}

    res = requests.get(
            url, headers=headers, allow_redirects=False, params=params)
    if not res.ok:
        return None
    if res.status_code != 200:
        return None

    data = res.json()["data"]
    posts = data["children"]
    titles = [post["data"]["title"] for post in posts]
    hot_list += titles

    params["after"] = data["after"]

    if params["after"]:
        recurse(subreddit, hot_list, params)

    return hot_list
