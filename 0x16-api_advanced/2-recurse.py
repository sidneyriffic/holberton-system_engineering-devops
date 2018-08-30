#!/usr/bin/python3
"""Function to get number of subscribers in a subreddit"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Get number of subscribers in a subreddit.
    Return 0 if subreddit doesn't exist
    """

    if len(hot_list) == 0 and subreddit is not None:
        subredditinfo = requests.get("http://reddit.com/r/" + subreddit +
                                     "/hot.json",
                                     headers={"User-Agent": "APILearning"})

        if subredditinfo.status_code != 200:
            return None
        subredditinfo = subredditinfo.json()
        if subredditinfo["kind"] == "Listing":
            hot_list.extend(subredditinfo["data"]["children"])
            if len(hot_list) == 0:
                return None
        else:
            return None

    if type(hot_list[0]) is dict:
        hot_list.append(hot_list[0]["data"]["title"])
        hot_list.pop(0)
        recurse(None)
    return hot_list
