#!/usr/bin/python3
"""todo api"""
import json
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

    rt = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    with open(uid + '.json', 'a') as f:
        lista = []
        dicc_ker = {}
        dicc = {}
        dicc_ker[uid] = lista
        for elem in rt:
            if elem.get("userId") == int(uid):
                lista.append({"task": elem.get("title"),
                             "completed": elem.get("completed"),
                              "username": username})
        dicc_ker[uid] = lista
        json.dump(dicc_ker, f)
