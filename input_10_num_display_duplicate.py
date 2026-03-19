numbers = []
unique_numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("Output: ", end=" ")
for num in unique_numbers:
    print(num, end=" ")

