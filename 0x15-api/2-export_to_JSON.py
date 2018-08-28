#!/usr/bin/python3
"""Get information from the JSONplaceholder API"""


if __name__ == "__main__":
    import json
    import requests
    import sys

    user = requests.get("http://jsonplaceholder.typicode.com/users/"
                        + sys.argv[1]).json()
    todos = requests.get("http://jsonplaceholder.typicode.com/todos?userId="
                         + sys.argv[1]).json()

    with open("USER_ID.json", "w") as jsonfile:
        username = user.get("username")
        userid = str(user.get("id"))
        tasklist = []
        for task in todos:
            taskdict = {"task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": username}
            tasklist.append(taskdict)
        userdict = {userid: tasklist}
        json.dump(userdict, jsonfile)
