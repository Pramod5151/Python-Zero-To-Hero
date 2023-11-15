numbers =list( range(1,25))

even, odd = [], []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)


print(even)
print(odd)