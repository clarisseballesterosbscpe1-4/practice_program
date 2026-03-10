text = input("Enter a number: ")
width = int(input("Enter the width: "))

# calculate how many zeros to add
zeros_to_add = width - len(text)

# add zeros at the beginning
if zeros_to_add > 0:
    text = "0" * zeros_to_add + text

print(f"Result: {text}")