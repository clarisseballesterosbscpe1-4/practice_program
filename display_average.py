numbers = []

while True:
    try:
        num = float(input("Enter a number: "))
        numbers.append(num)
    except:
        break

if len(numbers) > 0:
    average = sum(numbers) / len(numbers)
    print("Average is:", average)
else:
    print("No valid input")