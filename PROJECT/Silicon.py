import getpass
from datetime import date, datetime
import datetime
import csv
import pandas as pd

class Admission:
    def signup():
        print("\n SILICON SIGN UP PAGE")
        # # FIRST NAME SETUP
        while True:
            #first_name = input("Enter your first name: ")
            try:
                first_name = input(" \n Enter your first name: ")
                first_name1 = first_name
                first_name1 = first_name.isalpha()
                if first_name1 == True:
        
                    #pass
                    print(first_name)
                    break

                else:
                    print("Please try again")
            except ValueError:
                print("Enter valid name")

        # # LAST NAME ENTRY
        while True:
            try:
                last_name = input("\n Enter your last name: ")
                last_name1 = last_name.isalpha()
                if last_name1 == True:
                
                    print(last_name)
                    break
                    #pass
                else:
                    print("Please try again")
            except ValueError:
                print("Enter valid name")

        # # DOB SETUP (YEAR)
        while True:
            try:
                user_year = int(input("\n Enter your year of birth: "))

                date_now = datetime.date.today()
                year_now = date_now.year
                
                age = year_now - user_year

                if 18 <= age <= 30:
                    print("You qualify for this program")
                    break
                else: 
                    print("Sorry, you do not qualify for this program")
                    return
            except ValueError:
                print("Invalid ")
        
        # # DOB SETUP (MONTH)
        while True: 
            try:
                month = int(input("\n Enter your birth month: "))
                if 1 <= month <= 12:
                    break
                else:
                    print("Invalid entry. Enter month number")
            except ValueError:
                print("Invalid Input -- Numbers Only")   

        # # DOB SETUP (DAY)
        while True:
            try:
                day = int(input("\n Enter your day of birth: "))
                if 1 <= day < 31:
                    break
                else:
                    print("Invalid Day Entry")
            except ValueError:
                print("Invalid Input -- Numbers Only")

        dob = (user_year , month , day)

        # #EMAIL SETUP
        while True:
            try:
                email= input("\n Enter your e-mail: ")
                condition = "@"
                if condition in email:
                    print(email)
                    break
                else:
                    print("Please enter a valid email address")
            except ValueError:
                print("Invalid Input")

        # # PASSWORD CREATION   
        while True:
            try:
                password1 = getpass.getpass("\n Create a password: ")
                password1_valid = any(chr.isdigit() for chr in password1)
                if password1_valid == True:
                    print("Strong")
                    break

                else:
                    password1
                    print("Weak Password: Include Numbers")
            except ValueError:
                print("Invalid Password")
        
        # # PASSWORD CONFIRMATION
        while True:  
            try:              
                    password2 = getpass.getpass("\n Confirm your password: ")
                    password2_valid = any(chr.isdigit() for chr in password2)
                    if password2_valid == True:
                        print("Strong")
                    
                    if password1 == password2:
                        print("\n Password Confirmed")
                        break
                    else:
                        print("Passwords do not match")
                        
            except ValueError:
                print("Invalid Input")

        # # STUDENT SELECTS COURSE
        while True:
            print("\n \n Courses Available \n 1. Data Engineering \n 2. Software Engineering \n 3. Innovation Studio \n 4. Innovation School \n 5. Startup Funding ")
            
            try: 
                course = int(input("\n Select the course -- Choose a number: "))
                if course == 1:
                    course = "Data Engineering"
                    break
                elif course == 2:
                    course = "Software Engineering"
                    break
                elif course == 3:
                    course = "Innovation Studio"
                    break
                elif course == 4:
                    course = "Innovation School"
                    break
                elif course == 5:
                    course = "Startup Funding"
                    break

                else:
                    print("Enter a numbe between 1 and 5")
                print(course)

            except ValueError:
                print("Invalid Input")
            
        # STUDENT CONTACT
        while True:
            try:
                contact = int(input("\n Enter your contact no.: "))
                contact_string = str(contact)
                if len(contact_string) == 9:
                    break
                else:
                    print("Invalid Entry")
            except ValueError:
                print("Invalid")
            
            # GENDER INFORMATION
        while True:
            try:
                gender = input("\n Select your gender: \n Enter 'M' if Male or 'F' if Female? ")
                gender = gender.upper()
                if gender == "M":
                    gender = "Male"
                    break
                elif gender == "F":
                    gender = "Female"
                    break
                else:
                    print("Please enter M or F")
                
            except ValueError:
                print("Invalid Entry")

        with open('Database.csv', "a") as file:
            data   = first_name,last_name,dob,email,gender,password2,course,contact 
            writer= csv.writer(file)

            writer.writerow(data)
        
        file_path = 'Database.csv'
        #read csv

        df = pd.read_csv(file_path)


    
# admit = Admission
# admit.signup()

class Student(Admission):
    def login():
        super(Student)
        while True:
            print("Welcome to Silicon \n Kindly Log In \n")
            try:
                entry_email = input("Email: ")
                entry_pass  = input("Password: ")
                file_path = 'Database.csv'
                df = pd.read_csv(file_path)
            
                saved_mail = df['EMAIL'].tolist()
                saved_pass = df['PASSWORD'].tolist()

                if entry_email in saved_mail and entry_pass in saved_pass:
                    Student.menu()
                    break
                else:
                    print("Unsuccessful Login Attempt. \n Try Again \n \n")
                    break
            except ValueError:
                print("Invalid Entry")
    def menu():
            try:
                print ("-- SILICON --\n 1. About Us 2. Resources 3. Fee Payment 4. Exit")  
                choice = int(input("Select menu "))
                
                if choice == 1:
                    print("\n This is about us")
                
                elif choice == 2:
                    print("1. Lecture Slides \n 2. Notes \n 3. Course Outline \n 4. Time Table\n 5. Kaggle \n 6. Git Hub")

                elif choice == 3:
                    print("Pay fees: Follow the prompts to pay fees")
                    Student.fee_menu()

                elif choice == 4:
                    return               

                else:
                    print("Enter a Valid Input")
            except ValueError:
                print("Invalid Input")

    def fee_menu():
        print("\n MENU \n 1. MOMO \n 2. CARD")
        while True:
            try:
                main_choice = input("Enter option (number only): ")
                main_choice = int(main_choice)
                if main_choice == 1:
                    Student.momo()
                    print("Invalid Input")
                    return main_choice
                else:
                    print("Invalid input. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    
    def momo():
        while True:
            try:
                momo_no = int(input("\n Enter Momo No.: "))
                momo1 = str(momo_no)
                if len(momo1) == 9:
                   break
                else:
                     print("Incorrect Number")            
            except ValueError:
                print("Invalid Input")

        while True:
                try:
                   amount = float(input("\n Enter amount you wish to pay: "))
                   if amount > 0:
                    break
                   else: print("Enter a value greater than 0")   
                except ValueError:
                    print("Invalid Input")
                  
        
        while True:
                try:
                    email = input("\n Email: ")
                    file_path = 'Database.csv'
                    df = pd.read_csv(file_path)
                
                    saved_mail = df['EMAIL'].tolist()

                    if email in saved_mail:
                            break
                    else:
                            print("Email does not match")
                            
                except ValueError:
                        print("Invalid Input")
        
        while True:
                try:
                    pin = int(input("\n Enter your pin to confirm payment: "))
                    pin1 = str(pin)
                    if len(pin1) == 4:
                        print("Payment Successful")
                        Student.menu()
                        break 
                    else:
                        print("Invalid Pin")                     
                except ValueError:
                     print("Invalid Input")
            

        
                                  
                   
                

    def card():
            #CARD NUMBER
            while True:
                
                try:
                    card_number = int(input("Enter your card number: "))
                    card_string = str(card_number)

                    if len(card_string) == 10:
                        break

                    else:
                        print("Please try again")
                except ValueError:
                    print("Enter valid number")

            #CVV

            while True:

                try:
                    cvv_number = int(input("Enter the CVV number behind your card: "))
                    cvv_string = str(cvv_number)
                   
                    if len(cvv_string) == 3:
                        break

                    else:
                        print("Please try again")
                except ValueError:
                    print("Enter valid CVV number")

            #PIN

            while True:

                try:
                    pin_number = int(input("Enter yor PIN number: "))
                    pin_string = str(pin_number)
                   
                    if len(pin_string) == 4:
                        break

                    else:
                        print("Please try again")
                        
                except ValueError:
                    print("Enter valid PIN number")
                    break

            
            #EMAIL
            while True:
                try:
                    email = input("Email: ")
                    file_path = 'Database.csv'
                    df = pd.read_csv(file_path)
                
                    saved_mail = df['EMAIL'].tolist()

                    if email in saved_mail:
                        print("Payment Successful")
                        break
                    else:
                        print("Email does not match")
                
                except ValueError:
                    print("Invalid Input")


print("\n Welcome to Silicon Inovation Accra School (SAIS)\n")
print("1. Sign Up  2. Log In")
while True:
    try:
        home_choice = int(input("\nSelect an option "))
        if home_choice == 1:
            Admission.signup()
            break
        elif home_choice == 2:
            Student.login()
            break

        else:
            print("Please select 1 or 2")
    except ValueError:
        print("Invalid Input")
#Admission.signup()
# Student.login()