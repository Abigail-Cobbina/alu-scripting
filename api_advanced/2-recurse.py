#!/usr/bin/python3
"""Module that recursively gets all hot article titles for a subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return list of titles of all hot articles for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {"User-Agent": "MyBot/1.0"}
    params = {"after": after} if after else {}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get("data", {})
    posts = data.get("children", [])
    if not posts:
        return hot_list if hot_list else None
    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))
    after = data.get("after")
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
