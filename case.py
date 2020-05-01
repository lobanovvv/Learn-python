def switch(number_of_day):
    case = {
        1: "Monday",
        2: "Thuesday",
        3: "Wednesday",
        4: "Thuesday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return case.get(number_of_day)


print(switch(3))
