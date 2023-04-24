#!/usr/bin/python3
""" using a REST API, for a given employee ID, returns information
about his/her TODO list progress."""


if __name__ == "__main__":
    import json
    import requests
    import sys

    user_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/users/{}"
    url = url.format(user_id)

    employee_name = requests.get(url).json().get("username")

    url = "https://jsonplaceholder.typicode.com/todos?userId={}"
    url = url.format(user_id)
    todos = requests.get(url).json()
    employee_data = {user_id: []}

    for item in todos:
        employee_data[user_id].append({
                    "task": item.get("title"),
                    "completed": item.get("completed"),
                    "username": employee_name
                    })

    with open("{}.json".format(user_id), mode="w", encoding="utf-8") as file:
        file.write(json.dumps(employee_data))
