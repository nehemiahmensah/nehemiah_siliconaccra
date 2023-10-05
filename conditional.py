# #exam_result take in an input from the student convert it to a float check the grade the student had ....if the student enters 70.5 use the python function to run the number to the whole (round)
# name  = (input("Hi what is your name? ")) 
# score = float(input(" \n Please enter your score "))
# score = round(score)

# if score <= 39:
#     print(f"\n Hi {name} , GRADE F")
# elif score <= 49:
#     print(f" \n Hi {name} , GRADE E")
# elif score <=59:
#     print(f" \n Hi {name} ,  GRADE D")
# elif score <=69:
#     print(f" \n Hi {name} , GRADE C")
# elif score <=79:
#     print(f" \n Hi {name} , GRADE B")

# else: print(f" \n Hi {name} , GRADE A")
   
class students:
    '''Takes on the variables for the students data
    '''
    subject = ""
    marks = ""
    level = 200

    def __init__(self, name, subject, marks):
        self.name = name 
        self.subject = subject
        self.marks = int(marks)
        self.level = 200
    
    def display():
        return "shaaa"
    
me = students("nii","math",100)
print(me.display())





    
    # def getInfo(self):
    #     self.name = input("What is your name: ")
    #     self.subject = input("Enter the subject: ")
    #     self.marks = input("Enter the marks")
    #return
    
    # def outPut(self):
    #     print("Your name is ", self.name)
    #     print("Your subjects are ", self.subject)
    #     print("Your marks are ", self.marks)
    #     print("Your level is ", self.level)
    #   return

# score1 = students()
# print(score1)


