#input string
text = input("Enter the text: ")
prefix = input("Enter the prefix: ")
# get the length
length = len(prefix)
#compare first character
if text[:length] == prefix:
    print(f"Yes, '{text}' starts with '{prefix}'")
else:
    print(f"No, '{text}' does NOT start with '{prefix}'")