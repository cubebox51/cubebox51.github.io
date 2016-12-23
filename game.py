def Eat():
    global money    
    global plan
    global drink
    global food
    money = 15
    plan = 150
    drink = 1
    food = 1.25
    print ("Hello welcome to Mcdonald's how may I help you")
    print ("Type 1 for food")
    print ("Type 2 for drinks")
    user_input = input ("Type 3 for money")
    if int(user_input) == 1:
        print ("We have Hamburgers, fries, and cancer")
        print ("Type 1 for hamburgers")
        print ("Type 2 for fries")
        user_input = input ("Type 3 cancer")
        if int(user_input) == 1:
            print ("That will cost you $1.25")
            print ("Type 1 to pay")
            user_input = input ("Type 2 to steal")
            if int(user_input) == 1:
                print ("Thank you for comming")
                money = float(money) - float(food)
                print ("You now have") + (money) + ("dollars")
            elif int(user_input) == 2:
                print ("HEY COME BACK AND PAY!") 
        elif int(user_input) == 2:
            print ("Potato!")
        elif int(user_input) == 3:
            print ("Sorry we are out of cancer")
    elif int(user_input) == 2:
        print ("We have Coke, and Pepsi")
        print ("Type 1 for Coke")
        user_input = input ("Type 2 for Pepsi")
        if int(user_input) == 1:
            print ("COKE SUCKS NO DRINKS FOR YOU!!!!!")
        elif int(user_input) == 2: 
            print ("Nice I LOVE Pepsi Coke sucks that will cost you $1.00")
            print ("Type 1 to pay")
            user_input = input ("Type 2 to steal")
            if int(user_input) == 1:
                print ("Thank you for comming")
                money = float(money) - float(drink)
                print ("You now have") + (money) + ("dollars")
            elif int(user_input) == 2:
                print ("HEY COME BACK AND PAY!")
    elif int(user_input) == 3:
        print ("So heres the plan you take the register ill destract the others.")
        print ("Type 1 To call the cops")
        user_input = input ("Type 2 to do the plan")
        if int(user_input) == 1:
            money = float(money) + float(plan)
            print ("You got $150 for calling the cops")
            print('You now have {0} Dollars '.format(money))
        elif int(user_input) == 2:
            money = float(money) + float(plan)
            print ("You got $150 for doing the plan")
            print('You now have {0} Dollars '.format(money))
    else:
        print ("Sorry I did not get your order")
        Eat()
    
    input("Press Enter To Exit")

print ("Welcome to Life Simulater")
print ("Type 1 to Work")
user_input = input ("Type 2 to go to Mcdonalds")
if int(user_input) == 1:
    print ("Under Dev")
    print ("Redirecting to Mcdonalds")
if int(user_input) == 2:
    Eat()

        
