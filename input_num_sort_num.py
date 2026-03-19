numbers = []
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except:
        break

numbers.sort()

print("Sorted numbers:", numbers)