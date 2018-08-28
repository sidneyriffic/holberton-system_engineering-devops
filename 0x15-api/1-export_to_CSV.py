#!/usr/bin/python3
"""Get information from the JSONplaceholder API"""


if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    user = requests.get("http://jsonplaceholder.typicode.com/users/"
                        + argv[1]).json()
    todos = requests.get("http://jsonplaceholder.typicode.com/todos?userId="
                         + argv[1]).json()

    with open("USER_ID.csv", "w") as csvfile:
        csvexport = csv.writer(csvfile, quoting=csv.QUOTE_ALL,
                               lineterminator='\n')
        username = user.get("username")
        userid = user.get("id")
        for task in todos:
            csvexport.writerow([userid, username, task.get("completed"),
                                task.get("title")])
