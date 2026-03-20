name = input("Enter your name in incorrect casing: ")

snake_case = name.lower().split()
result = "_".join(snake_case)
print(result)