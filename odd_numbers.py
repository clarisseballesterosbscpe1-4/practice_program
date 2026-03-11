odd_count = 0
#input 10 numbers
for i in range(10):
    number = int(input("Enter the number: "))
#check odd numbers
    if number % 2 != 0:
#count odd numbers
        odd_count += 1
print("total numbers", odd_count)
