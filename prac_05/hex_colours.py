"""
Based on the state name example program,
create a program that allows you to look up hexadecimal colour codes
at http://www.color-hex.com/color-names.html
"""

import requests                     # Gets URL
from bs4 import BeautifulSoup       # Parses HTML
import json                         # Saves Dictionary

url = "https://www.color-hex.com/color-names.html"

# Appear as a web browser to access URL
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# Store URL content into variable
response = requests.get(url, headers=headers)
response.raise_for_status()          # raise an error if the request failed

# Turn URL content to a structure that is easier to work with
soup = BeautifulSoup(response.text, "html.parser")

# All COLOURS are in a table. Find and Grab the table.
table = soup.find("table")

# Create Dictionary
COLOUR_TO_HEXCODE = {}

for row in table.find_all("tr")[1:]:            # skip header, loop through all rows
    cells = row.find_all("td")                  # store each row into list -> cells
    if len(cells) >= 3:                         # filter for complete rows

        name = cells[0].get_text(strip=True).upper()
        hex_code = cells[2].get_text(strip=True)

        if hex_code and not hex_code.startswith("#"):
            hex_code = "#" + hex_code

        if name and hex_code:
            COLOUR_TO_HEXCODE[name] = hex_code                      # Dictionary

print(f"Extracted {len(COLOUR_TO_HEXCODE)} colours")
print(dict(list(COLOUR_TO_HEXCODE.items())[:5]))    # show a few examples

# Save Dictionary as JSON file
with open("colours_to_hexcode.json", "w", encoding="utf-8") as file:
    json.dump(COLOUR_TO_HEXCODE, file, indent=2, ensure_ascii=False)

# Get Colour name. Display HEXCODE
colour_name = str(input("Enter Colour Name: ")).upper()
while colour_name != "":
    try:
        print(f"{colour_name} HEXCODE is {COLOUR_TO_HEXCODE[colour_name]}")
    except KeyError:
        print("Invalid Colour Name")
    colour_name = str(input("Enter Colour Name: ")).upper()

print("Finished")
