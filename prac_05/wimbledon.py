"""
Write a program to read this file, process the data and display processed information:
the champions and how many times they have won.
the countries of the champions in alphabetical order
Estimate: 2 hr
Actual: 3 hr
"""

FILENAME = "wimbledon.csv"


def main():
    """Process Wimbledon Data and execute formatted prints"""
    # Build dictionaries from Data
    wimbledon_data = load_data(FILENAME)
    champion_to_wins, country_to_champions = build_dictionaries(wimbledon_data)

    # Champion to Wins in Alphabetical order
    sorted_champion_to_wins = sort_champion_to_wins(champion_to_wins)
    # Print Wimbledon Champions
    print_wimbledon_champions(sorted_champion_to_wins)

    # Country to Champions in Alphabetical order
    sorted_country_to_champions = sort_country_to_champions(country_to_champions)
    # Print Countries who won wimbledon
    print_countries(sorted_country_to_champions)


def load_data(filename) -> list[list]:
    """Read CSV file. Return List of lists."""
    wimbledon_data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for line in in_file:
            line = line.strip()
            line_parts = line.split(',')
            wimbledon_data.append(line_parts)
    return wimbledon_data


def build_dictionaries(wimbledon_data: list[list]) -> tuple[dict[str, int], dict[str, set[str]]]:
    """Build chmapion_to_wins and country_to_champions dictionaries"""
    champion_to_wins = {}
    country_to_champions = {}

    # Build Dictionaries
    for match_data in wimbledon_data:
        # Champion to Wins
        champion_to_wins[match_data[2]] = champion_to_wins.get(match_data[2], 0) + 1
        # Country to Champions
        if match_data[1] not in country_to_champions:
            country_to_champions[match_data[1]] = {match_data[2]}
        else:
            country_to_champions[match_data[1]].add(match_data[2])

    return champion_to_wins, country_to_champions


def sort_champion_to_wins(champion_to_wins: dict[str, int]) -> dict[str, int]:
    """Sort Champion to Wins in Alphabetical order"""
    sorted_champion_to_wins = {}
    for champion in sorted(champion_to_wins.keys()):
        sorted_champion_to_wins[champion] = champion_to_wins[champion]

    return sorted_champion_to_wins


def print_wimbledon_champions(champion_to_wins: dict[str, int]):
    """Print Wimbledon Champions and their # of wins"""
    # Find Max Widths: Champion to Wins
    max_champion_width = max(len(champion) for champion in list(champion_to_wins.keys()))
    max_wins_width = max(len(str(wins)) for wins in list(champion_to_wins.values()))

    # Print Wimbledon Champions
    print("Wimbledon Champions:")
    for champion in champion_to_wins:
        print(f"{champion:<{max_champion_width}} : {champion_to_wins[champion]:>{max_wins_width}}")


def sort_country_to_champions(country_to_champions: dict[str, set[str]]) -> dict[str, set[str]]:
    """Sort Country to Champions in Alphabetical order"""
    sorted_country_to_champions = {}
    for country in sorted(country_to_champions.keys()):
        champions = country_to_champions[country]
        sorted_champions = sorted(champions)

        sorted_country_to_champions[country] = sorted_champions
    return sorted_country_to_champions


def print_countries(country_to_champions: dict[str, set[str]]):
    """Print Countries as a string"""
    print(f"These {len(country_to_champions.keys())} countries have won Wimbledon:")
    countries_string = ", ".join(country_to_champions.keys())
    print(countries_string)


main()
