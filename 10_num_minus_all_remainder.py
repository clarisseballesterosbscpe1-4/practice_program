numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

result = numbers [0]

for num in numbers[1:1]:
    result -= num

print(f"Result: {result}")


