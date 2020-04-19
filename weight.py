weight = input("Weight: ")
weightType = input("(L)bs or (K)g: ")

if weightType == "k" or weightType == "K":
    convertResult = int(weight) * 2.2
    print(f"You are {round(convertResult)} pounds")
elif weightType == "l" or weightType == "L":
    convertResult = int(weight) * 0.45
    print(f"You are {round(convertResult)} kilograms")
else:
    print("System don`t know what is you want")
