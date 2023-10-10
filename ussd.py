import getpass
from datetime import date
class service:
     
     def track(op):
          card_tracker.append(op)
          return op
     def cred(res):
          credit.append(res)
          return res
     def withdraw(wrd):
         if wrd > reminder:
              print ("Not enough balance left to  complete this transaction")
         debit.append(wrd)
         return wrd  
     def newBalance(neb):
         reminder.append(neb)
         return neb      

def main_menu():
    print("\n MENU \n 1. Make Deposit \n 2. Withdrawal \n 3. Transfer Money \n 4. Check Balance\n 5. Financial Statement")
    while True:
        try:
            main_choice = input("Enter option (number only): ")
            main_choice = int(main_choice)
            if 1 <= main_choice <= 5:
                return main_choice
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def menu():
    print("\n 1. Return to Main Menu \n 2. Exit")
    while True:
        try:
            choice_m = input("Enter option (number only): ")
            choice_m = int(choice_m)
            if choice_m == 1:
                 return choice_m
            elif choice_m == 2:
                return choice_m
            else:
                print("Invalid input. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
# def app(mek):
#     income = []
#     income.append(mek)
#     return mek

# Welcome to USSD app
print("\n WELCOME TO SILICON ACCRA INNOVATION SCH. USSD EXPENSE TRACKER SERVICE \n")
print("\n To proceed create a unique 4-digit passcode -- PLEASE DO NOT START WITH 0(ZERO)")

# Handle exceptions when user enters wrong input for unique code and allows a user create a password
while True:
    try:
        user_pin = getpass.getpass("Enter a 4-digit number(pin): ")
        user_pin = int(user_pin)
        if 1000 <= user_pin <= 9999:
            print("Thank You! Do not share this code with anyone.")
            break
        else:
            print("Invalid input. Please enter a 4-digit number.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# THIS IS THE MAIN BODY FOR THE PROGRAM
card_tracker = []
credit = []
debit = []
reminder = []
while True:
    choice = main_menu()

#this block of the code handles the deposit a user makes  
    if choice == 1:
        try:
            card = int(input("Enter 12-digit code on the scratch card: "))
            if 100000000000 <= card <= 999999999999:
                
                if card in card_tracker:
                     print ("\n Invalid! Card has already been used")
                else:
                    service.track(card)
                     
                    if 100000000000 <= card < 199999999999:
                        service.cred(100) 
                    elif 200000000000 <= card < 299999999999: 
                       service.cred(200) 
                    elif 300000000000 <= card < 399999999999: 
                       service.cred(300) 
                    elif 400000000000 <= card < 499999999999: 
                       service.cred(400)  
                    elif 500000000000 <= card < 599999999999: 
                       service.cred(500) 
                    elif 600000000000 <= card < 699999999999: 
                       service.cred(600) 
                    elif 700000000000 <= card < 799999999999: 
                       service.cred(700) 
                    elif 800000000000 <= card < 899999999999: 
                       service.cred(800) 
                    elif 900000000000 <= card < 999999999999: 
                       service.cred(900) 
                    sum_credit = sum(credit)
                    print("\n Thank You!! Deposit Successful.")          
                    print(f"Your balance is {sum_credit}") 
            else:
                print("Invalid Card")    
            return_choice = menu()
            if return_choice == 1:
                    choice
            elif return_choice == 2:
                    print("Exiting program. Goodbye!")
                    break
           
        except ValueError:
            print("Invalid Input")

        
#this block of code handles the withdrawal a user makes    
    elif choice == 2:
        try:
            wDraw = float(input("\n How much do you want to withdraw: "))
            service.withdraw(wDraw)
            print(debit)
            sum_expense = sum(debit)
            balance = sum_credit - debit[-1]
            service.newBalance(balance)
            print(f"Your balance is {balance}")
            print(reminder)
            
            
            # if balance > sum_credit:
            #     
            # else:
            #     pin = getpass.getpass("\n Enter your pin: ")
            #     pin = int(pin)
            #     if pin == user_pin:
            #         print("\n Withdrawal Successful ")
                    
            #         print(f"Your balance is {balance}")
            #     else: 
            #         print("Incorrect Pin")
            return_choice = menu()  
            if return_choice == 1:
                    choice
            elif return_choice == 2:
                print("Exiting program. Goodbye!")
                break              
            
                
        except ValueError:
                print("Invalid Input. -- for now.lol")
    # # Add handling for other menu choices (2, 3, 4, 5) here
    #project for beginners geek for geeks
    elif choice == 4:

        print(f"Your balance is {reminder[-1]}")
        return_choice = menu()  
        if return_choice == 1:
                    choice
        elif return_choice == 2:
                print("Exiting program. Goodbye!")
                break     

#this option prints out the financial statement        
    elif choice == 5:
        today = date.today()
        with open("./financialStatement.txt", "a") as file:
            file.write(f"\n Your Financial Statement \n You made an deposit of {sum_credit}, and made a withdrawal of {sum_expense}\n Your balance as of {today} is {balance} \n Thank You For Choosing Silicon USSD EXPENSE SERVICES!")
        file.close
        with open("./financialStatement.txt","r") as file:  
            print(file.read())
        file.close
        return_choice = menu()  
        if return_choice == 1:
                    choice
        elif return_choice == 2:
                print("Exiting program. Goodbye!")
                break     

# # for line in file:
# #     print(line)
# print(file.mode)
# file.write("I am making an input \n")

# #to save memory when you open a file make sure you close it. which should always come adn the end 
# file.close()