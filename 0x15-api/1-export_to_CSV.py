#!/usr/bin/python3
"""todo api"""
import requests
from sys import argv


if __name__ == "__main__":
    total_tasks = 0
    done_tasks = 0
    uid = argv[1]
    tasks = []

    ru = requests.get('https://jsonplaceholder.typicode.com/users').json()
    for u in ru:
        if u.get("id") == int(uid):
            name = u.get("name")
            username = u.get("username")
            break

    rt = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    with open(uid + '.csv', 'a') as f:
        for elem in rt:
            if elem.get("userId") == int(uid):
                f.write('"{}","{}","{}","{}"\n'
                        .format(elem.get("userId"),
                                username, elem.get("completed"),
                                elem.get("title")))
                f.write("\n")
