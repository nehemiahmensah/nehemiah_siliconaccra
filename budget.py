#build a budget tracker that allows users to input income and expenses, 
#then calculates the balance, using loops and conditions for financial calculations

print("\n WELCOME TO YOUR BUDGET TRACKER")

#TAKE INCOME FROM USER
income = int(input("\n How much is your salary? "))

#TAKE DETAILS OF OVERTIME
overtime = input("\n Do you work overtime: yes/no? ")
overtime = overtime.lower()

if overtime == "yes":
    phour = int(input("\n How much are you paid per hour(for overtime)? "))
    hours_worked = int(input("\n How many hours did you work overtime? "))
else:
    phour = 0
    hours_worked = 0

overtime_income = phour * hours_worked

#TAKE DETAILS OF SIDE JOB
side_job = input("\n Do you work a side job: yes/no? ")
side_job = side_job.lower()

if side_job == "yes":
    side_job_pay = int(input("\n How much do you earn from your side job? "))
else: side_job_pay = 0

#TAKE INPUT FOR ANY OTHER INCOME NOT SPECIFIED
other_income = input("\n Do you have any other source of income apart from the ones specified above: yes/no? ")
other_income = other_income.lower()

if other_income == "yes":
    amt_other_income = int(input("\n How much do you earn that has not been specified above: "))
else: amt_other_income = 0

if side_job_pay >= 0 and overtime_income >= 0 and income >= 0 and amt_other_income >= 0:
    total_income = income + overtime_income + side_job_pay + amt_other_income
    print(f"\n Your total income is ${total_income}\n")
else: print("No value to compute")

print("*" * 40)
 
 #TAKE EXPENSES FROM USER
print("\n EXPENSES ")
utility    = int(input("\n How much do you spend on utilities? "))
food       = int(input("\n How much do you spend on food? "))
transport  = int(input("\n How much do you spend on transport? "))

rent = input("\n Do you pay rent monthly: yes/no? ")
rent = rent.lower()

if rent == "yes":
    rent_pay = int(input("\n How much rent do you pay in a month? "))
else: rent_pay = 0

loan = input("\n Are you on a monthly loan repayment plan: yes/no? ")
loan = loan.lower()

if loan == "yes":
    loan_pay = int(input("\n How much loan repayment do you make? "))
else: loan_pay = 0

extra_expenses = input("\n Do you have miscellaneous expenditure and any other expenses not specified: yes/no? ")
extra_expenses = extra_expenses.lower()

if extra_expenses == "yes":
    miscellaneous = int(input("\n Kindly enter sum of miscellaneous expenditure and any other expenses not specified "))
else: miscellaneous = 0

if utility >= 0 and food >= 0 and transport >= 0 and rent_pay >= 0 and loan_pay >= 0 and miscellaneous >= 0:
    expenses = utility + food + transport + rent_pay + loan_pay + miscellaneous
    print(f"\n Your total expense is ${expenses}")
else: print("No value to compute")

print("*" * 40)

balance = total_income - expenses

print(f"""\n Your total income is ${total_income}
            Your total expenses is ${expenses}
        \n\n\n Your balance is ${balance}
      """)

#health care expenses, insurance expenses, miscellanous.