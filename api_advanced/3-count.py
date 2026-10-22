#!/usr/bin/python3
"""Module that counts keywords in hot articles for a subreddit."""
import requests


def count_words(subreddit, word_list, counts={}, after=None):
    """Print sorted count of keywords found in hot article titles."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {"User-Agent": "MyBot/1.0"}
    params = {"after": after} if after else {}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json().get("data", {})
    posts = data.get("children", [])
    if not posts:
        if counts:
            sorted_counts = sorted(counts.items(),
                                   key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print("{}: {}".format(word, count))
        return
    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            w = word.lower()
            for t in title:
                if t == w:
                    counts[w] = counts.get(w, 0) + 1
    after = data.get("after")
    if after is None:
        if counts:
            sorted_counts = sorted(counts.items(),
                                   key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print("{}: {}".format(word, count))
        return
    return count_words(subreddit, word_list, counts, after)
