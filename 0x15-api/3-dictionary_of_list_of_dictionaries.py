#!/usr/bin/python3
"""Get information from the JSONplaceholder API"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    users = requests.get("http://jsonplaceholder.typicode.com/users").json()
    with open("todo_all_employees.json", "w") as jsonfile:
        dictlist = []
        for userid in users:
            username = userid.get("username")
            userid = str(userid.get("id"))
            todos = requests.get("http://jsonplaceholder.typicode.com/todos?" +
                                 "userId=" + userid).json()

            tasklist = []
            for task in todos:
                taskdict = {"task": task.get("title"),
                            "completed": task.get("completed"),
                            "username": username}
                tasklist.append(taskdict)
            userdict = {userid: tasklist}
            dictlist.append(userdict)
        json.dump(dictlist, jsonfile)
