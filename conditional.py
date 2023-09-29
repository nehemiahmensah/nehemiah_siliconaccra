#exam_result take in an input from the student convert it to a float check the grade the student had ....if the student enters 70.5 use the python function to run the number to the whole (round)
name  = (input("Hi what is your name? ")) 
score = float(input(" \n Please enter your score "))
score = round(score)

if score <= 39:
    print(f"\n Hi {name} , GRADE F")
elif score <= 49:
    print(f" \n Hi {name} , GRADE E")
elif score <=59:
    print(f" \n Hi {name} ,  GRADE D")
elif score <=69:
    print(f" \n Hi {name} , GRADE C")
elif score <=79:
    print(f" \n Hi {name} , GRADE B")

else: print(f" \n Hi {name} , GRADE A")
   




