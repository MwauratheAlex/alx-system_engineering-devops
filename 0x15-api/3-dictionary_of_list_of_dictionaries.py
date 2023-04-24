#!/usr/bin/python3
""" using a REST API, for a given employee ID, returns information
about his/her TODO list progress."""


if __name__ == "__main__":
    import json
    import requests
    import sys

    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()
    employees = {}

    for user in users:
        url = "https://jsonplaceholder.typicode.com/todos?userId={}"
        user_id = user.get("id")
        url = url.format(user_id)

        todos = requests.get(url).json()
        employees[user_id] = []

        for item in todos:
            employees[user_id].append({
                    "username": user.get("username"),
                    "task": item.get("title"),
                    "completed": item.get("completed")
                    })

    with open("todo_all_employees.json", mode="w", encoding="utf-8") as file:
        file.write(json.dumps(employees))
