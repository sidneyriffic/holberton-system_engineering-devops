#!/usr/bin/python3
"""Get information from the JSONplaceholder API"""


if __name__ == "__main__":
    import requests
    from sys import argv

    user = requests.get("http://jsonplaceholder.typicode.com/users/" +
                        argv[1]).json()
    todos = requests.get("http://jsonplaceholder.typicode.com/todos?userId=" +
                         argv[1]).json()

    userid = str(user.get("id"))
    with open(userid + ".csv", "w") as csvfile:
        username = user.get("username")
        userid = user.get("id")
        for task in todos:
            csvfile.write('"{}","{}","{}","{}"\n'.
                          format(userid, username, task.get("completed"),
                                 task.get("title")))
