numbers = [ 2, 3, 5, 7, 1, 23, 11, 9, 2 ]
maxNum = 0
firstIteration = True

for num in numbers:
    if firstIteration == True:
        maxNum = num
        firstIteration = False
    if num > maxNum:
        maxNum = num
print(maxNum)