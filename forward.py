import getpass
from datetime import date, datetime
import datetime


class Student:
    def __init__(self,first_name,last_name,email,course,password,dob,gender,student_id,contact):
        self.first_name = first_name
        self.last_name  = last_name
        self.email = email
        self.course = course
        self.password = password
        self.dob = dob
        self.gender = gender
        self.student_id = student_id
        self.contact = contact

    def sign_up():
        while True:
            #first_name = input("Enter your first name: ")
            try:
                first_name = input("Enter your first name: ")
                first_name1 = first_name.isalpha()
                if first_name1 == True:
        
                    #pass
                    print(first_name)
                    break

                else:
                    print("Please try again")
            except ValueError:
                print("Enter valid name")

            # this is for last name
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

            # this is for dob

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

        while True: 
            try:
                month = int(input("\n Enter your birth month: "))
                if 1 <= month <= 12:
                    break
                else:
                    print("Invalid entry. Enter month number")
            except ValueError:
                print("Invalid Input -- Numbers Only")   

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
            
                     
                    

            
                


        print(f"Your first name is {first_name}, \n Your last name is {last_name}, \nYour email is{email}")       
            
            
        #last_name  = input("What is your last name: ")


    def log_in():
        pass

    def course(self,innovation_school,innovation_studio,start_up_funding,software_development,data_engineering,innovation_partnership):
        #if
        pass
        return
    
    def pay_fees():
        return
    
#student = Student()
Student.sign_up()
