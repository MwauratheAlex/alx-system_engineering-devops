#!/usr/bin/python3
""" using a REST API, for a given employee ID, returns information
about his/her TODO list progress."""


if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) == 1:
        print("Usage: ./0-gather_data_from_an_API.py <employeeID>")
    else:
        employeeID = sys.argv[1]
        url = "https://jsonplaceholder.typicode.com/users/{}"
        url = url.format(employeeID)

        employee_name = ""
        number_of_done_tasks = 0
        total_number_of_tasks = 0
        completed_task_titles = []

        with requests.get(url) as res:
            json = res.json()
            employee_name = json.get("name")

        url = "https://jsonplaceholder.typicode.com/todos?userId={}"
        url = url.format(employeeID)

        with requests.get(url) as res:
            todos = res.json()
            total_number_of_tasks = len(todos)
            for item in todos:
                if item.get("completed") is True:
                    number_of_done_tasks += 1
                    completed_task_titles.append(item.get("title"))

        print("Employee {} is done with tasks({}/{}):".format(
            employee_name,
            number_of_done_tasks,
            total_number_of_tasks
            ))

        for title in completed_task_titles:
            print("\t {}".format(title))
