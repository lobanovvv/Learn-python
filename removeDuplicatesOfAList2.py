numbers = [ 1, 2, 3, 4, 5, 1, 3, 4, 5, 1, 2, 3]
clearNumbers = []

for item in numbers:
    if item not in clearNumbers:
        clearNumbers.append(item)

print(clearNumbers)

