#!/usr/bin/python3
""" using a REST API, for a given employee ID, returns information
about his/her TODO list progress."""


if __name__ == "__main__":
    import csv
    import requests
    import sys

    url = "https://jsonplaceholder.typicode.com/users/{}"
    url = url.format(sys.argv[1])

    employee_name = requests.get(url).json().get("username")

    url = "https://jsonplaceholder.typicode.com/todos?userId={}"
    url = url.format(sys.argv[1])
    todos = requests.get(url).json()
    done_tasks = []

    with open("USER_ID.csv", mode="w") as file:
        writer = csv.writer(
                        file,
                        delimiter=",",
                        quotechar='"',
                        quoting=csv.QUOTE_ALL)
        for item in todos:
            writer.writerow([
                        sys.argv[1],
                        employee_name,
                        item.get("completed"),
                        item.get("title")
                        ])
