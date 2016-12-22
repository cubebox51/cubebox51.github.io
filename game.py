money = str(15)
plan = str(150)
drink = str(1)
food = str(1.25)

print ("Welcome to Life Simulater")
print ("Type 1 to Work")
user_input = input ("Type 2 to go to Mcdonalds")
if int(user_input) == 1:
    print ("Under Dev")
if int(user_input) == 2:
    Eat()


def Eat():
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
                print ("You now have") + (money - food) + ("dollars")
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
                print ("You now have") + (money - drink) + ("dollars")
            elif int(user_input) == 2:
                print ("HEY COME BACK AND PAY!")
    elif int(user_input) == 3:
        print ("So heres the plan you take the register ill destract the others.")
        print ("Type 1 To call the cops")
        user_input = input ("Type 2 to do the plan")
        if int(user_input) == 1:
            print ("You got $150 for calling the cops")
            print ("You now have") + (money + plan) + ("dollars")
        elif int(user_input) == 2:
            print ("You got $150 for doing the plan")
            print ("You now have") + (money + plan) + ("dollars")
    else:
        print ("Sorry I did not get your order")
        Eat()
    input("Press Enter To Exit")
Eat()

        
