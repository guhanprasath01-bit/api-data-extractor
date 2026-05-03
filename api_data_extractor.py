import requests
import csv
import json
from datetime import datetime

url = "https://jsonplaceholder.typicode.com/users"


start_time = datetime.now()
try:
    response = requests.get(url, timeout=10)
    if response.status_code != 200:
        print("Error: Status code", response.status_code)
        exit()
    data = response.json()
    with open("raw_response.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    with open("users.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["ID", "Name", "Email", "City", "Company"])
        count = 0

        for user in data:
            id_value = int(user.get("id", 0)) # convert type
            name = user.get("name", "N/A") # handle missing
            email = user.get("email", "N/A")
            city = user.get("address", {}).get("city", "N/A")
            company = user.get("company", {}).get("name", "N/A")
            writer.writerow([id_value, name, email, city, company])
            count += 1
        end_time = datetime.now()

        print("Data Saved Successfully!")
        print("Total Records:", count)
        print("Time Taken:", end_time - start_time)
        print("Output File: users.csv")
except Exception as e:
    print("Error occurred:", e)
