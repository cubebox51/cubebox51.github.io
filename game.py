global money    
global plan
global drink
global food
global drinks
global foods
global hunger
global thirst
global energy
hunger = 10
thirst = 10
energy = 10
drinks = 0
foods = 0
money = 0
plan = 150
drink = 1
food = 1.25
def Eat():
    global money    
    global plan
    global drink
    global food
    global drinks
    global foods
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
                print('You now have {0} Dollars '.format(money))
            foods = float(foods) + (1)
            if int(user_input) == 2:
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
                print('You now have {0} Dollars '.format(money))
            elif int(user_input) == 2:
                print ("HEY COME BACK AND PAY!")
            drinks = float(drinks) + (1)
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
    
    print ("Type 1 to order again")
    user_input = input ("Type 2 for main menu")
    if int(user_input) == 1 and (money) > 1:
        Eat()
    elif int(user_input) == 2:
        menu()
    else:
        menu()
    

def work():
    global gain
    global money
    global energy
    gain = 1
    from random import randint
    work1 = (randint(1,20))
    hours = (randint(1,8))
    answer = float(work1) * float(hours)
    print('Bob worked {0} hours and got {1} dollars per hour '.format(hours,work1))
    work2 = input('How much money did bob make')
    if int(work2) == int(answer):
        print ("you gained 1 Dollars")
        money = float(money) + float(gain)
        print('You now have {0} Dollars '.format(money))
        print("Type 1 to work again") 
        user_input = input ("Type 2 to go to main menu")
        energy = float(energy) - float(gain)
        if int(user_input) == 1:
            work()
        if int(user_input) == 2:
            menu()
    else:
        print ("You lost 1 Dollar")
        if money > 0:
            money = float(money) - float(gain)
            print('You now have {0} Dollars '.format(money))
            print("Type 1 to work again") 
            user_input = input ("Type 2 to go to main menu")
            energy = float(energy) - float(gain)
            if int(user_input) == 1:
                work()
            if int(user_input) == 2:
                menu()
        else:
            print('You now have {0} Dollars '.format(money))
            print("Type 1 to work again") 
            user_input = input ("Type 2 to go to main menu")
            energy = float(energy) - float(gain)
            if int(user_input) == 1:
                work()
            if int(user_input) == 2:
                menu()
def timer():
    import time
    global thirst
    global hunger
    if int(hunger) > 0 or int(hunger) > 0:
        time.sleep(1)
        thrist = float(thirst) - (.01)
        hunger = float(hunger) - (.01)
    else:
        print ("YOU DED GG")



def items():
    global energy
    global money
    global hunger
    global thirst
    global foods
    global drinks
    print('You have a wallet (${0})  '.format(money))
    if int(foods) > 0: 
        print('You have {0} hamburgers type 1 to eat hamburger'.format(foods))
    if int(drinks) > 0:
        print('You have {0} Pepsi type 2 to drink Pepsi'.format(drinks))
    user_input = input('Type 3 to go to main menu')
    if int(user_input) == 1 and int(foods) > 0:
        hunger = float(hunger) + (3)
        energy = float(energy) + (3)
        foods = float(foods) - (1)
    if int(user_input) == 2 and int(drinks) > 0:
        thirst = float(thirst) + (2)
        energy = float(energy) + (1)
        drinks = float(drinks) - (1)
    if int(user_input) == 3:
        menu()
    menu()
def menu():
    print ("Welcome to Life Simulater")
    print ("Type 1 to Work")
    print ("Type 2 to go to Mcdonalds")
    print ("Type 3 to see your inventory")
    print('You have {0} / 10 hunger'.format(hunger))
    print('You have {0} / 10 thirst'.format(thirst))
    print('You have {0} / 10 energy'.format(energy))
    user_input = input('You have {0} dollars '.format(money))
    if int(user_input) == 1:
        work()
    elif int(user_input) == 2 and (money) > 1:
        Eat()
    if int(user_input) == 3:
        items()
    
    else:
        print ("You need more money")
        menu()
timer()
menu()



