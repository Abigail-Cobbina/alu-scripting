#!/usr/bin/python3
"""Module that prints the titles of the top ten hot posts."""

import requests


def top_ten(subreddit):
    """Print the titles of the first ten hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "python:alu-scripting:v1.0 (by /u/Abigail-Cobbina)"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False
        )

        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get("data", {}).get("children", [])

        if not posts:
            print(None)
            return

        for post in posts:
            print(post.get("data", {}).get("title"))

    except requests.RequestException:
        print(None)
