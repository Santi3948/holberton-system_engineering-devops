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

    rt = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    for elem in rt:
        if elem.get("userId") == int(uid):
            if elem.get("completed") is True:
                done_tasks = done_tasks + 1
                tasks.append(elem.get("title"))
            total_tasks = total_tasks + 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, done_tasks, total_tasks))
    for t in tasks:
        print("\t {}".format(t))
