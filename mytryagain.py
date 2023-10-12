#SOLID S--- single responsibility  eg. using one method / class to solve one problem
# O - open for extension close to modification - dont modify the code a lot
# listov 

# def validation(val):
#     if val.isnumeric() == True:
#         return val + 10
#     else: print("Not valid")

# entry = input("Enter the number: ")
# entry2 = validation(entry)

# print(entry2)

# guf = input("Enter number ")
# guf = guf.isnumeric()
# # print(type(guf))

# if guf.isnumeric() == True:
#     print("You did it")


contact = int(input("Enter the contact"))
contacta = str(contact)
print(len(contacta))

#print(len(contact))

if len(contacta) == 10:
    print("successful")