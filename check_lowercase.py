#input string
text = input("Enter the text: ")
result = ""
#check if the text are in lower case
for character in text:
    if 'a' <= character <= 'z':
        #Output
        print(character, "is lower case")
