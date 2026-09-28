place = input("You wake up. Where will you go today? (Please make sure that you put first letter in all answers as CAPITAL) ")
if place == "Market":
    bought = input("You go to the Market. What do you buy? ")
    if bought == "Apples" or bought == "Apple":
        print("You choose the one bad apple. ")
        eat1 = input("Do you want to go to the hospital? ")
        if eat1 == "Yes":
            print("You get insta-cured! :0")
        elif eat1 == "No":
            print("You feel unwell.")
        else:
            print("Say 'Yes' or 'No'")
    else:
        print(f"There are no more {bought} in stock. Next time, choose an Apple.")
elif place == "Downtown":
    place2 = input("Do you want to go to the Space Needle, Go Golfing, or Get Fish? ")
    if place2 == "Space Needle":
        heights = input("You get scared of heights. Do you want to power through or exit the building? (Please answer 'Power' or 'No') ")
        if heights == "Power":
            print("You survive, but hate Seattle")
        elif heights == "No":
            print("You get out, and now hate Seattle")
        else:
            print("Please choose either 'Power' or 'No'")
    elif place2 == "Go Golfing":
        number1 = int(input("Pick a number from 1 - 100 "))
        if 63 <= number1 <= 83:
            print("You get selected by a scout!")
        else:
            print("You get the worst possible score. :( )")
    elif place2 == "Get Fish":
        restaurant = input("You LOVE fish now. Do you want to open a fish restaurant? ('Yes' or 'No') ")
        if restaurant == "Yes":
            number2 = int(input("Pick a number from 1 - 100 "))
            if 17 <= number2 <= 37:
                print("You open the best Michelin fish restaurant in the world, and you get richy-rich. ")
            else:
                print("You fail miserably, and lose a bunch of money. You are poor, but you still love fish. :) ")
        elif restaurant == "No":
            print("You still love fish. ")
        else:
            print("*sigh*. You came all this way, all the questions, just to not type 'Yes' or 'No'. Make sure you do that next time. :( )")
else:
    print("Please type in 'Market' or 'Downtown'. ")