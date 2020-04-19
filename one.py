name = input("Input your name")
lenName = len(name)

if lenName < 3:
    print("Your name must have 3 characters")
elif lenName > 50:
    print("Your name must have maximum 50 characters")
else:
    print("Name looks good!")
