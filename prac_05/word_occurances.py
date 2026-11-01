"""
Word Occurrences
Estimate: 45 minutes
Actual:   12:17 minutes
"""

get_text = str(input("Write Text: ")).strip()

words = get_text.split()

word_to_count = {}

for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

max_word_width = max(len(word) for word in list(word_to_count.keys()))
max_count_width = max(len(str(count)) for count in list(word_to_count.values()))

for word in word_to_count:
    print(f"{word:>{max_word_width}}: {word_to_count[word]:>{max_count_width}}")
