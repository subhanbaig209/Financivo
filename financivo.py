def financivo():
    print("Hello! Welcome to Financivo! This app is a simple budget app that will conveniently manage your finances based on the information you input")
    rate = float(input("Please enter the number value of the amount of money you make per hour: "))
    hours = float(input("Please enter the number of hours you work in between paydays: "))


    print ("Amount of money made per hour: $" + str(rate) + ".")
    print("Number of hours worked between each payday: " + str(hours) + ".")
    reply = input("Is the information stated above correct? Respond 'yes' if true, or 'no' if false.: ")
    while reply == "no":
        rate = float(input("Please enter the number value of the amount of money you make per hour: "))
        hours = float(input("Please enter the number of hours you work in between paydays: "))
        reply = input("Is the information stated above correct? Respond 'yes' if true, or 'no' if false.: ")
    total_income = (rate) * (hours)
    print("Yout total income over the specified time is $" + str(total_income) + ".")

    sav = input("How much percent of the money earned would you like to save?: ")
    while int(sav) > 100:
        print("You can only save what you have!")
        sav = input("How much percent of the money earned would you like to save?: ")

    sav = int(sav)/100
    sav1 = ((1)-(sav)) 
    useable = sav1 * total_income

    print("The amount of money that you have to use over this period of time is $" + str(useable) + ".")
    needs = float(input("Enter the total amount of money that is needed for necessities (rent, travel, food, any other spefic needs): $"))

    anyuse = useable - needs
    broke = anyuse * -1
    if anyuse > 0:
        print ("The total amount of money that you can spend for other uses is $" + str(anyuse) + ".")
    elif anyuse == 0:
        print("You do not have any money to spend for other uses. We recommend you either take money out of savings, or work more hours.")
    else:
        print("You have no money to spend. Instead, you owe $" + str(broke) + ". We recommend you take money out of savings or work more hours in order to pay off debt.")
    print("Thank you for using Financivo! If you have any concerns, please notify us!")

financivo()