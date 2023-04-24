#!/usr/bin/python3
"""Records all tasks that are owned by this employee.
Exports the data to USER_ID.json"""


if __name__ == "__main__":
    import sys
    import json
    import requests

    if len(sys.argv) == 1:
        print("Usage: ./0-gather_data_from_an_API.py <employeeID>")
    else:
        employeeID = sys.argv[1]
        url = "https://jsonplaceholder.typicode.com/users/{}"
        url = url.format(employeeID)

        employee_name = ""

        with requests.get(url) as res:
            data = res.json()
            employee_name = data.get("username")

        url = "https://jsonplaceholder.typicode.com/todos?userId={}"
        url = url.format(employeeID)
        employee_data = {employeeID: []}

        with requests.get(url) as res:
            todos = res.json()

            for item in todos:
                employee_data[employeeID].append({
                        "task": item.get("title"),
                        "completed": item.get("completed"),
                        "username": employee_name
                        })

        filename = "{}.json".format(employeeID)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(json.dumps(employee_data))
