numbers = []
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except:
        break
if len(numbers) > 0:
    print("The lowest number is: ", min(numbers))
else:
    print("No valid Input")
