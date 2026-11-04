"""
Word Occurrences
Estimate: 45 minutes
Actual:   1 hr 15 minutes
"""

get_text = str(input("Write Text: ")).strip()
words = get_text.split()

# Build Dictionary
word_to_count = {}
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

if not word_to_count:
    print("No text entered.")
else:
    max_word_width = max(len(word) for word in list(word_to_count.keys()))
    max_count_width = max(len(str(count)) for count in word_to_count.values())

# Format Print sorted dictionary
for word in sorted(word_to_count):
    print(f"{word:>{max_word_width}}: {word_to_count[word]:>{max_count_width}}")
