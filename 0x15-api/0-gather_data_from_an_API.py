#!/usr/bin/python3
""" using a REST API, for a given employee ID, returns information
about his/her TODO list progress."""


if __name__ == "__main__":
    import requests
    import sys

    url = "https://jsonplaceholder.typicode.com/users/{}"
    url = url.format(sys.argv[1])

    employee_name = requests.get(url).json().get("name")

    url = "https://jsonplaceholder.typicode.com/todos?userId={}"
    url = url.format(sys.argv[1])
    todos = requests.get(url).json()
    done_tasks = []


    for item in todos:
        if item.get("completed") is True:
            done_tasks.append(item.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), len(todos)))

    for item in done_tasks:
        print("\t {}".format(item))
