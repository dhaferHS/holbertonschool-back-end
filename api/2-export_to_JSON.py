#!/usr/bin/python3
"""script to export data in the CSV format"""


import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos",
                         params={"userId": sys.argv[1]}).json()

    for task in todos:

        taskDict = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user.get('username')}

    filename = sys.argv[1] + '.json'

    with open(filename, mode='w') as f:
        json.dump(taskDict, f)
