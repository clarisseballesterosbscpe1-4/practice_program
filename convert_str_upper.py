#input string
text = input("Enter the text: ")
result = ""
#convert lowercase to upper case
for character in text:
    if text.lower():
         result += chr(ord(character) - 32)

print(result)