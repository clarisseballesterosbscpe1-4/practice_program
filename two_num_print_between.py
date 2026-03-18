num_1 = int(input("enter a number: "))
num_2 = int(input("enter a number: "))

start = min(num_1, num_2)
end = max(num_1, num_2)

i = start + 1

while i <= end:
    print(i)
    i += 1
