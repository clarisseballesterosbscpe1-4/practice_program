#input string
text = input("enter text: ")
character = input("enter character to find: ")
#position of character
position = -1
#finding the number position of the character
for i in range(len(text)):
    if text[i] == character:
        position = i
        break

if position == -1:
    print("value error")
else:
    print("first location:", position)