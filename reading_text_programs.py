# Word count
# Unique word count
# Character count (with and without spaces)
# Average word length
# Most common word(s) and their frequency

with open("input.txt", "r") as f:
    text = f.read()

def count_words(words):
    word_count = words.split()
    return len(words)

print(count_words(text))