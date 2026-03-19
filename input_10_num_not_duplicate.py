numbers = []
for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

unique_numbers = set(numbers)

print("Numbers without duplicates:", unique_numbers)