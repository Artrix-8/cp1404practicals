"""
Gets user inputted string and outputs a list with number of word occurrences.
"""

text = input("Text: ")
while not text:
    print("Invalid input")
    text = input("Text: ")
words = text.split()
word_and_count = {}
for word in words:
    count = word_and_count.get(word, 0)
    word_and_count[word] = count + 1
words = sorted(list(word_and_count.keys()))
max_length = max((len(word) for word in words))
for word in words:
    print(f"{word + ' :':{max_length + 2}} {word_and_count[word]}")
