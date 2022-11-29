def ordinalSuffix(number):
    numberstr = str(number)
    if len(numberstr) > 1 and numberstr[-2] == "1":
        print(numberstr + "th")
    elif numberstr[-1] == "1":
        print(numberstr + "st")
    elif numberstr[-1] == "2":
        print(numberstr + "nd")
    elif numberstr[-1] == "3":
        print(numberstr + "rd")
    else:
        print(numberstr + "th")





ordinalSuffix(0)

ordinalSuffix(1)

ordinalSuffix(2)

ordinalSuffix(3)

ordinalSuffix(4)

ordinalSuffix(10)

ordinalSuffix(11)

ordinalSuffix(12)

ordinalSuffix(13)

ordinalSuffix(14)

ordinalSuffix(101)
