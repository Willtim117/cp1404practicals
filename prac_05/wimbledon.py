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
    # Build List to work with
    wimbledon_data = []
    for line in in_file:
        line = line.strip()
        line_parts = line.split(',')
        wimbledon_data.append(line_parts)

champion_to_wins = {}
country_to_champions = {}

for match_data in wimbledon_data:
    champion_to_wins[match_data[2]] = champion_to_wins.get(match_data[2], 0) + 1

    if match_data[1] not in country_to_champions:
        country_to_champions[match_data[1]] = {match_data[2]}
    else:
        country_to_champions[match_data[1]].add(match_data[2])

# Champion to wins in Alphabetical order
sorted_champion_to_wins = {}
for champion in sorted(champion_to_wins.keys()):
    sorted_champion_to_wins[champion] = champion_to_wins[champion]

print(sorted_champion_to_wins)

# Country to wins in Alphabetical order
sorted_country_to_champions = {}

for country in sorted(country_to_champions.keys()):

    champions = country_to_champions[country]
    sorted_champions = sorted(champions)

    sorted_country_to_champions[country] = sorted_champions

print(sorted_country_to_champions)

