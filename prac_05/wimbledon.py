"""
Write a program to read this file, process the data and display processed information:
the champions and how many times they have won.
the countries of the champions in alphabetical order
Estimate: 2 hr
Actual:
"""

filename = "wimbledon.csv"

with open(filename, "r", encoding="utf-8-sig") as in_file:
    next(in_file)

    wimbledon_data = []
    for line in in_file:
        line = line.strip()
        line_parts = line.split(',')
        print(line_parts)
        wimbledon_data.append(line_parts)

champion_to_wins = {}
country_to_champions = {}

for match_data in wimbledon_data:
    champion_to_wins[match_data[2]] = champion_to_wins.get(match_data[2], 0) + 1

    if match_data[1] not in country_to_champions:
        country_to_champions[match_data[1]] = {match_data[2]}
    else:
        country_to_champions[match_data[1]].add(match_data[2])

print(champion_to_wins)
print(country_to_champions)
