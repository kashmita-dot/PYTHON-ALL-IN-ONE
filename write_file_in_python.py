# Python writing files (.txt, .json, .csv)

import json

employee = {
    "name": "Spongebob",
    "age": "30",
    "job": "cook"
}

file_path = "E:\\PYTHON\\output.json"

try:
    with open(file_path, "a") as file:
        json.dump(employee, file, indent=4)
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")


# csv
import csv

employees = [["name", "Age", "Job"],
            ["Spongebob", 30, "cook"],
            ["Patrick", 37, "Unemployed"],
            ["Sandy", 27, "Scientist"]]

file_path = "E:\\PYTHON\\output.csv"

try:
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")