numbers = [ 1, 2, 3, 4, 5, 1, 3, 4, 5, 1, 2, 3]

for item in numbers:
    if numbers.count(item) > 1:
        for removeItem in range(numbers.count(item) - 1):
            numbers.remove(item)
            print(numbers)

print(numbers)
