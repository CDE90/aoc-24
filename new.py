import datetime
import os

import requests
from dotenv import load_dotenv

load_dotenv()

# Get the current date (day only)
day = datetime.date.today().day
year = datetime.date.today().year

# Check if the day directory exists
if os.path.exists(f"d{day}"):
    print(f"Day {day} already exists")
    exit(1)

# Get the template file
with open("template.py") as f:
    template = f.read()

# Get the input from the AoC website
url = f"https://adventofcode.com/{year}/day/{day}/input"

session = os.getenv("AOC_SESSION")
if session is None:
    print("AOC_SESSION environment variable not set")
    exit(1)

response = requests.get(url, cookies={"session": session})
input = response.text

# Create a new directory for the day
os.mkdir(f"d{day}")

# Create a new file for the input
with open(f"d{day}/input.txt", "w") as f:
    f.write(input)

# Create a new file for the code
with open(f"d{day}/d{day}.py", "w") as f:
    f.write(template.replace("{{day}}", str(day)))

print(f"Created day {day}")
