#!/usr/bin/python3
"""todo api"""
import requests
from sys import argv
import json


if __name__ == "__main__":
    ru = requests.get('https://jsonplaceholder.typicode.com/users').json()
    rt = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    with open('todo_all_employees.json', 'w+') as f:
        dicc_ker = {}
        for u in ru:
            lista = []
            for elem in rt:
                username = u.get("username")
                lista.append({"username": username,
                             "task": elem.get("title"),
                              "completed": elem.get("completed")})
                dicc_ker[elem.get("userId")] = lista
        json.dump(dicc_ker, f)
