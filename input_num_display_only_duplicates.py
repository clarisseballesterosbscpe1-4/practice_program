numbers = []
duplicates = []
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Numbers with Duplicates: ", duplicates)
