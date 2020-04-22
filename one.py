price = 1000000
has_good_credit = False

if has_good_credit:
    downPayment = int(price * 0.1)
    print("You down payment = " + str(downPayment))
else:
    downPayment = int(price * 0.2)
    print("You down payment = " + str(downPayment))
print("The end")
