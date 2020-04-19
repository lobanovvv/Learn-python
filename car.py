startedFlag = False

while True:
    userInput = input(">").lower()
    if userInput == "help":
        print ("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif userInput == "start":
        if startedFlag == True:
            print("Hey, car is started!!!")
        else:
            print("Car started...Ready to go!")
        startedFlag = True
    elif userInput == "stop":
        if startedFlag == False:
            print("Hey, car is stopped!!!")
        else:
            print("Car stopped.")
        startedFlag = False
    elif userInput == "quit":
        break
    else:
        print("I don't understand that...")
