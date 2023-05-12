#!/usr/bin/python3
"""queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], params=None):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alx"}

    res = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

    if res.status_code == 404:
        return hot_list
    else:
        posts = res.json()["data"]["children"]
        after = res.json()["data"]["after"]
        post_titles = [post["data"]["title"] for post in posts]

        hot_list.extend(post_titles)

        if after is None:
            return hot_list
        params = {"after": after}

        return recurse(subreddit, hot_list, params)
