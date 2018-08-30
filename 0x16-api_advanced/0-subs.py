#!/usr/bin/python3
"""Function to get number of subscribers in a subreddit"""

import requests


def number_of_subscribers(subreddit):
    """
    Get number of subscribers in a subreddit.
    Return 0 if subreddit doesn't exist
    """

    subredditinfo = requests.get("http://reddit.com/r/" + subreddit +
                                 "/about.json",
                                 headers={"User-Agent": "APILearning"})

    if subredditinfo.status_code != 200:
        return 0
    subredditinfo = subredditinfo.json()
    if subredditinfo["kind"] == "t5":
        return subredditinfo["data"]["subscribers"]
    else:
        return 0
