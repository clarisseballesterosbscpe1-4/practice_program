#input string
text = input("Enter the text: ")
word = input("Enter the word to count: ")
#counting a word
count = 0

for i in range(len(text) - len(word) + 1):
    if text[i:i+len(word)] == word:
        count += 1

print(f"result: {count}")
