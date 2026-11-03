"""
Write a program to read this file, process the data and display processed information:
the champions and how many times they have won.
the countries of the champions in alphabetical order
Estimate: 2 hr
Actual:
"""
import csv
from operator import itemgetter

filename = "wimbledon.csv"

with open(filename, "r", encoding="utf-8-sig") as in_file:
    wimbledon_data = []
    for line in in_file:
        line = line.strip()
        line_parts = line.split(',')
        print(line_parts)
        wimbledon_data.append(line_parts)

champion_to_wins = {}
for match_data in wimbledon_data:
    champion_to_wins[match_data[2]] = champion_to_wins.get(match_data[2], 0) + 1

print(champion_to_wins)

# Format Print sorted dictionary
for word in sorted(word_to_count):
    print(f"{word:>{max_word_width}}: {word_to_count[word]:>{max_count_width}}")

    #
    # def load_song_data(filename=FILENAME) -> list:
    #     """Load song data from a CSV file into a list of lists.
    # 
    #     Each line in the file is expected to be in the format:
    #     song_name, artist_name, year, learn/unlearn (l/u)
    #     """
    #     song_list = []
    #     try:
    #         with open(filename, "r") as input_file:
    #             for line in input_file:
    #                 line = line.strip()
    #                 parts = line.split(',')
    # 
    #                 # [song name, artist name, year, learn/unlearn]
    #                 song_in_list = [parts[0], parts[1], int(parts[2]), parts[3]]
    #                 song_list.append(song_in_list)
    # 
    #     except FileNotFoundError:  # Handle no file
    #         print(f"ERROR: '{filename}' not found")
    # 
    #     return song_list
