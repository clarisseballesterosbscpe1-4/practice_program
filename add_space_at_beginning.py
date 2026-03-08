#input string
text = input("Enter the text: ")
width = int(input("Enter the width: "))
#calculate how many spaces do we add
spaces_to_add = width - len(text)
#if spaces is greater than 0, add at the beginning
if spaces_to_add > 0:
    text += " " * spaces_to_add + text
#output
print(f"result: '{text}'")
