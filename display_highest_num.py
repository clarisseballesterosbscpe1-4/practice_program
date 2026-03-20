numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except:
        break

if numbers:
    print("Highest number is:", max(numbers))
else:
    print("No input")

