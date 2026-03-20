name = input("Enter your name: ")

characters = name.split()
pascal_case = ""
for character in characters:
    pascal_case += character.capitalize()
    
print(pascal_case)