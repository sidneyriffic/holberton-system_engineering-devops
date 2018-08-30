#!/usr/bin/python3
"""Function to get number of subscribers in a subreddit"""

import requests


def top_ten(subreddit):
    """
    Get number of subscribers in a subreddit.
    Return 0 if subreddit doesn't exist
    """

    subredditinfo = requests.get("http://reddit.com/r/" + subreddit +
                                 "/hot.json?limit=10",
                                 headers={"User-Agent": "APILearning"})

    if subredditinfo.status_code != 200:
        return 0
    subredditinfo = subredditinfo.json()
    if subredditinfo["kind"] == "Listing":
        for post in subredditinfo["data"]["children"]:
            print(post["data"]["title"])
    else:
        return 0
