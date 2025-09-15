# Word count
# Unique word count
# Character count (with and without spaces)
# Average word length
# Most common word(s) and their frequency

# Word Count Function
with open("input.txt", "r") as f:
    text = f.read()

def count_words(words):
    word_count = words.split()
    return len(words)

print(count_words(text))

# Unique word count

def count_unique_words(words):
    unique_word_count = words.split()
    return len(set(unique_word_count))

print(count_unique_words(text))

# Character count (with and without spaces)

def count_characters(words):
    return len(text)

print(count_characters(text))