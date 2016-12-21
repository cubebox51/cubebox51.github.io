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
            user_input = input ("Thank you for comming")
        elif int(user_input) == 2:
            user_input = input ("HEY COME BACK AND PAY!") 
    elif int(user_input) == 2:
        user_input = input ("Potato!")
    elif int(user_input) == 3:
        user_input = input ("Sorry we are out of cancer")
elif int(user_input) == 2:
    print ("We have Coke, and Pepsi")
    print ("Type 1 for Coke")
    user_input = input ("Type 2 for Pepsi")
    if int(user_input) == 1:
        user_input = input ("COKE SUCKS NO DRINKS FOR YOU!!!!!")
    elif int(user_input) == 2: 
        print ("Nice I LOVE Pepsi Coke sucks that will cost you $1.00")
        print ("Type 1 to pay")
        user_input = input ("Type 2 to steal")
        if int(user_input) == 2:
            user_input = input ("HEY COME BACK AND PAY!")
elif int(user_input) == 3:
    print ("So heres the plan you take the register ill destract the others.")
    print ("Type 1 To call the cops")
    user_input = input ("Type 2 to do the plan")
    if int(user_input) == 1:
        user_input = input ("You got $150 for calling the cops")
    elif int(user_input) == 2:
        user_input = input ("You got $150 for doing the plan")
else:
    print ("Sorry I did not get your order")
input("Press Enter To Exit")

        
