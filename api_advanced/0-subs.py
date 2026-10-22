#!/usr/bin/python3
"""Module that queries Reddit API for number of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """Return number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyBot/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get("data", {}).get("subscribers", 0)
