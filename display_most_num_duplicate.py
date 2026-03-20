numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except:
        break

counts = {}
for num in numbers:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

max_count = 0
most_duplicate = None

for num in counts:
    if counts[num] > max_count:
        max_count = counts[num]
        most_duplicate = num

if max_count > 1:
    print("Most duplicate number is:", most_duplicate)
else:
    print("No duplicates found")

