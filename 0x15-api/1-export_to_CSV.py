#!/usr/bin/python3
""" using a REST API, for a given employee ID, exports information
about his/her TODO list progress to csv."""


if __name__ == "__main__":
    import csv
    import requests
    import sys

    if len(sys.argv) == 1:
        print("Usage: ./0-gather_data_from_an_API.py <employeeID>")
    else:
        employeeID = sys.argv[1]
        url = "https://jsonplaceholder.typicode.com/users/{}"
        url = url.format(employeeID)

        employee_name = ""
        completed_task_titles = []

        with requests.get(url) as res:
            json = res.json()
            employee_name = json.get("username")

        url = "https://jsonplaceholder.typicode.com/todos?userId={}"
        url = url.format(employeeID)

        with open("USER_ID.csv", mode="w") as file:
            with requests.get(url) as res:
                todos = res.json()
                writer = csv.writer(
                        file,
                        delimiter=",",
                        quotechar='"',
                        quoting=csv.QUOTE_ALL)

                for item in todos:
                    writer.writerow([
                        employeeID,
                        employee_name,
                        item.get("completed"),
                        item.get("title")
                        ])
