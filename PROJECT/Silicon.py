import getpass
from datetime import date, datetime
import datetime
import csv
import pandas as pd

# CLASS  AND METHODS SETUP
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

        # # FIRST NAME SETUP
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

        #CONFIRM TO CREATE AN AUTO INCREMENT FOR ID            
        # while True:
        #     try:
        #         confirm = int(input("\n Are you sure you want to submit these details? \n Choose \n 1. Confirm \n 2. Exit"))
        #         if confirm == 1:
                
        #         elif confirm == 2:
        #             return
        #         else:
        #             print("Please enter 1 or 2")
        #     except ValueError:
        #         print("Invalid Entry")
            
        #/Users/siaccrainnovationsch/Documents/Nii/version_control/PROJECT/Database.csv 
        #/Users/siaccrainnovationsch/Documents/Nii/version_control/PROJECT/Silicon.py       
        #write to file
        with open('Database.csv', "a") as file:
            data   = first_name,last_name,dob,email,gender,password2,course,contact 
            writer= csv.writer(file)

            writer.writerow(data)
        
        file_path = 'Database.csv'
        #read csv

        df = pd.read_csv(file_path)
        print(df)

        # print(f"""{first_name}
        #         {last_name}
        #            {dob}
        #             {course}
        #             {contact}
        #                 {email}
        #         {gender}

        #     """)       

#asdfa@adsada
    def log_in():
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
                    print("Successful")
                    break
                else:
                    print("Unsuccessful Login Attempt. \n Try Again \n \n")
                    break
            except ValueError:
                print("Invalid Entry")



    def course(self,innovation_school,innovation_studio,start_up_funding,software_development,data_engineering,innovation_partnership):
        #if
        pass
        return
    
    def pay_fees():
        return
    
#student = Student()
print("Choose an option: 1. Sign Up   2. Log In")
choice1 = int(input("Enter your option here: "))
if choice1 == 1:
    Student.sign_up()
elif choice1 == 2:
    Student.log_in()
else:
    print("Please choose 1 or 2")
# with open('Database.csv', "r") as file:
#     #print(file.read())
#     for line in file:
#         print(line)
#     # reader = csv.reader(file)
#     # for record in reader:
#     #     FIRST_NAME, LAST_NAME, DOB, EMAIL, GENDER, PASSWORD, COURSE, CONTACT = record
#     #     print(f"{EMAIL,PASSWORD}")
#     # print(reader.read())