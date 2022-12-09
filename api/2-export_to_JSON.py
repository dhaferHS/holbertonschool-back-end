#!/usr/bin/python3
"""script to export data in the CSV format"""


import json
import requests
import sys


if __name__ == "__main__":

    userId = sys.argv[1]
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(userId))

    todos = user = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todos = todos.json()

    todoUser = {}
    tasklist = []

    for task in todos:
        if task.get('userId') == int(userId):
            taskDict = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": user.json().get('username')}
            taskList.append(taskDict)
            todoUser[userId] = tasklist

        filename = userId + '.json'
        with open(filename, mode='w') as f:
            json.dump(todoUser, f)
