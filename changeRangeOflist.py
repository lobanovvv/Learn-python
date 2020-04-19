arr = [1,2,3,4,5]

for i in arr:
    print(f"{arr} - array before changing")
    print(f"i = {i}")
    arr.remove(i)
    print(f"{arr} - modified array")
    print()

