phoneNum = input("Input phone number: ")
translated = ''

translateNumToWord = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    0: "Zero"
}

for item in phoneNum:
    translated += translateNumToWord[int(item)] + ' '

print(translated)
