################################################################################
# python C:\Users\user\Downloads\game.py                                       #   
# python C:\Users\student\Downloads\game.py                                    #
#                                                                              #
#                                                                              #
################################################################################
import datetime
import time
from random import randint
import pickle
user_input = input ("Would you like to continue your save? (1=Yes) (2=No)")
if int(user_input) == 1:
    with open('objs.pickle', "rb") as f:  
        money, hunger, thirst, energy, gun, wanted, timer, drinks, foods, salary, house, machine,moneymachine, collect, collecter = pickle.load(f)
        
else:
    timer2 = 0
    now = datetime.datetime.now()
    timer = ('{0}{1}'.format(now.hour, now.minute))
    hunger = 10
    thirst = 10
    energy = 10
    drinks = 0
    foods = 0
    money = 0
    drink = 1
    wanted = 0
    gun = 0
    salary = 1
    house = 0
    collecter = 0
    machine = ("|          |")
    moneymachine = 0
    collect = 0
    print ("Chapter 1")
    print ("The Big City")
    time.sleep(1)
    print ("You lost your brother recently and are very sad about it but something about his death bugs you the doctors told you that he died of a heart attack but you dont belive this and think he was murdered he used to write in a diary and he would keep it with him whenever he went to Mcdonalds You decide to move to the Big City")
def Eat():
    food = 1.25
    try:
        global money, plan, drink, drinks, foods, wanted, gun, house, machine, moneymachine, collecter
        print (" ")
        print (" Hello welcome to Mcdonald's how may I help you")
        print ("\r Type 1 for food")
        print ("\r Type 2 for drinks")
        print ("\r Type 3 for money")
        print ("Type 4 to walk over to the shady guy")
        user_input = input ("\r Type 5 to walk over to the realtor")
        print (" ")
        if int(user_input) == 1:
            print (" ")
            print (" We have Hamburgers, fries, and cancer")
            print ("\r Type 1 for hamburgers")
            print ("\r Type 2 for fries")
            user_input = input ("\r Type 3 cancer")
            print (" ")
            if int(user_input) == 1:
                print (" ")
                print (" That will cost you $1.25")
                print ("\r Type 1 to pay")
                user_input = input ("Type 2 to steal")
                print (" ")
                if int(user_input) == 1:
                    print (" ")
                    print ("Thank you for comming")
                    money = float(money) - float(food)
                    print('You now have {0} Dollars '.format(money))
                    print (" ")
                foods = float(foods) + (1)
                if int(user_input) == 2:
                    print (" ")
                    print ("HEY COME BACK AND PAY!")
                    wanted = float(wanted) + (1) 
                    print('Your wanted level is now {0}'.format(wanted))
                    print (" ")
            elif int(user_input) == 2:
                print (" ")
                print ("Potato!")
                print (" ")
            elif int(user_input) == 3:
                print (" ")
                print ("Sorry we are out of cancer")
                print (" ")
        elif int(user_input) == 2:
            print (" ")
            print ("We have Coke, and Pepsi")
            print ("Type 1 for Coke")
            user_input = input ("Type 2 for Pepsi")
            print (" ")
            if int(user_input) == 1:
                print (" ")
                print ("COKE SUCKS NO DRINKS FOR YOU!!!!!")
                print (" ")
            elif int(user_input) == 2:
                print (" ")
                print ("Nice I LOVE Pepsi Coke sucks that will cost you $1.00")
                print ("Type 1 to pay")
                user_input = input ("Type 2 to steal")
                print (" ")
                if int(user_input) == 1:
                    print (" ")
                    print ("Thank you for comming")
                    print (" ")
                    money = float(money) - (1)
                    print (" ")
                    print('You now have {0} Dollars '.format(money))
                    print (" ")
                elif int(user_input) == 2:
                    print (" ")
                    print ("HEY COME BACK AND PAY!")
                    wanted = float(wanted) + (1) 
                    print('Your wanted level is now {0}'.format(wanted))
                    print (" ")
                drinks = float(drinks) + (1)
        elif int(user_input) == 3:
            print (" ")
            print ("So heres the plan you take the register ill destract the others.")
            user_input = input ("Type 1 to do the plan")
            print (" ")
            if int(user_input) == 1:
                plan = (randint(1,20))
                money = float(money) + float(plan)
                print (" ")
                print('You got {0} Dollars for doing the plan'.format(plan))
                print('You now have {0} Dollars '.format(money))
                wanted = float(wanted) + (1) 
                print('Your wanted level is now {0}'.format(wanted))
                print (" ")
        elif int(user_input) == 4:
            print (" ")
            print ("Heres the deal I can sell you a Gun or Hack the wanted list.")
            print ("Type 1 to buy a gun for 500$")
            user_input = input ("Type 2 to hack for 100$")
            print (" ")
            if int(user_input) == 1:
                if money > 500:
                    print (" ")
                    print ("Here take it now run off before the cops come")
                    print (" ")
                    gun = 1
                    money = float(money) - (500)
            if int(user_input) == 2:
                if money > 100:
                    print (" ")
                    print ("Here im done now run off before the cops come")
                    print (" ")
                    wanted = 0
                    money = float(money) - (100)
        elif int(user_input) == 5:
            print (" ") 
            print ("Type 1 to buy a house for 1000$") 
            print ("Type 2 to buy a money machine for 100$")
            print ("Type 3 to buy a collecter")
            user_input = input ("Type 4 to go back to main menu")
            print (" ")
            if int(user_input) == 1 and money > 999:
                house = 1
                money = float(money) - (1000)
            if int(user_input) == 2 and money > 99:
                moneymachine = float(moneymachine) + (1)
                money = float(money) - (100)
            if int(user_input) == 3 and money > 99:
                collecter = 1
                money = float(money) - (100)
        print (" ")        
        print ("Type 1 to order")
        user_input = input ("Type 2 for main menu")
        print (" ")
        if int(user_input) == 1 and (money) > 1:
            Eat()
        elif int(user_input) == 2:
            menu()
        else:
            menu()
    except ValueError:
        Eat()
    

def work():
    global money
    global energy
    global salary
    gain = 1
    from random import randint
    work1 = (randint(1,20))
    hours = (randint(1,8))
    answer = float(work1) * float(hours)
    print (" ")
    print('Bob worked {0} hours and got {1} dollars per hour '.format(hours,work1))
    work2 = input('How much money did bob make')
    print (" ")
    if int(work2) == int(answer):
        if hours == 1:
            salary = float(salary) + (1)
            print ("You got a promotion!(1+ Salary)")    
        print (" ")
        print ("you gained {0} Dollars".format(salary))
        money = float(money) + float(salary)
        print('You now have {0} Dollars '.format(money))
        print("Type 1 to work again") 
        user_input = input ("Type 2 to go to main menu")
        print (" ")
        energy = float(energy) - float(gain)
        if int(user_input) == 1:
            work()
        if int(user_input) == 2:
            menu()
    else:
        print (" ")
        print ("You lost 1 Dollar")
        if money > 0:
            money = float(money) - float(gain)
            print('You now have {0} Dollars '.format(money))
            print("Type 1 to work again") 
            user_input = input ("Type 2 to go to main menu")
            print (" ")
            energy = float(energy) - (1)
            if int(user_input) == 1:
                work()
            if int(user_input) == 2:
                menu()
        else:
            print (" ")
            print('You now have {0} Dollars '.format(money))
            print("Type 1 to work again") 
            user_input = input ("Type 2 to go to main menu")
            print (" ")
            energy = float(energy) - (1)
            if int(user_input) == 1:
                work()
            if int(user_input) == 2:
                menu()


def items():
    global energy
    global money
    global hunger
    global thirst
    global foods
    global drinks
    global gun
    print (" ")
    print('You have a wallet (${0})  '.format(money))
    if int(gun) > 0:
        print('You have a gun')
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
    print (" ")
    menu()
def dead():
    input("gg dude you ded")
def home():
    global machine, moneymachine, collect, money, collecter, user_input
    if moneymachine == 1:
        machine = ("|$         |")
    if moneymachine == 2:
        machine = ("|$$        |")
    if moneymachine == 3:
        machine = ("|$$$       |")
    if moneymachine == 4:
        machine = ("|$$$$      |")
    if moneymachine == 5:
        machine = ("|$$h$$$     |")
        
    
    print ("")
    print ("   House")
    print (" ----------")
    print (machine)
    print ("|          |")
    print ("|          |")
    print ("|          |")
    print (" ----------")
    print ("You have {0}/5 money machines".format(moneymachine))
    if int(collecter) == 0:
        print ("You have {0}$ to collect".format(collect))
        user_input = input ("Type 1 to collect money")
    print ("")
    if int(user_input) == 1:
        money = float(money) + float(collect)
        collect = 0
  
    menu()
def menu():
    global wanted, house, collect, moneymachine
    global now
    global timer
    global hunger
    global thirst
    global money
    global gun
    global energy
    now = datetime.datetime.now()
    timer2 = ('{0}{1}'.format(now.hour, now.minute))
    if int(hunger) > (10):
        hunger = 10
    if int(thirst) > (10):
        thirst = 10
    if int(energy) > (10):
        energy = 10
    
    if (0) > int(hunger) or (0) > int(thirst):
        dead()
    if (wanted) > (9):
        if gun == 1:
            wanted = 9
            energy = float(energy) - (1)
            print (" ")
            print ("You shot the cops but you are not off their radar")
            print (" ")
        else:
            money = float(money) * (0.5)
            wanted = 0
            print (" ")
            print ("You got caught by the cops")
            print (" ")
    if (timer2) > (timer):
        thirst = float(thirst) - (1)
        hunger = float(hunger) - (1)
        timer = float(timer) + (1)
        collect = float(collect) + float(moneymachine) 
        timer = ('{0}{1}'.format(now.hour, now.minute))
        menu()
    print (" ")
    print ("Type 1 to Work")
    print ("Type 2 to go to Mcdonalds")
    print ("Type 3 to see your inventory")
    print ("Type 4 to save your progress")
    if house == 1:
        print ("Type 5 to go to your house")
    print('You have {0} / 10 hunger'.format(hunger))
    print('You have {0} / 10 thirst'.format(thirst))
    print('You have {0} / 10 energy'.format(energy))
    print('You have {0} / 10 wanted'.format(wanted))
    user_input = input('You have {0} dollars '.format(money))
    print (" ")
    if int(user_input) == 1:
        work()
    elif int(user_input) == 2 and (money) > 1:
        Eat()
    elif int(user_input) == 3:
        items()
    elif int(user_input) == 795535:
        money = float(money) + (1000)
        menu()
    elif int(user_input) == 4:
        with open('objs.pickle', 'wb') as f:  
            pickle.dump([money, hunger, thirst, energy, gun, wanted, timer, drinks, foods, salary, house, machine, moneymachine, collect, collecter], f)
    elif int(user_input) == 5 and house == 1:
        home()




            
    
    else:
        print (" ")
        print ("You need more money")
        print (" ")
        menu()
menu()


        





        

















