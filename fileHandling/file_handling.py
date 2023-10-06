# file = open("./resources/movies.txt", "a")
# print(file.name)
# #print(file.read())

# # for line in file:
# #     print(line)
# print(file.mode)
# file.write("I am making an input \n")

# #to save memory when you open a file make sure you close it. which should always come adn the end 
# file.close()

# with open("./resources/movies.txt", "r") as file:
#     print(file.name)


#     # using an example of file not found with file handling
# ref = input("Enter 1 to choose file path")
# try:
#    if ref.isnumeric() == True:
#         pass
#    with open("./resources/movies.txt", "r") as file:
#        print(file.read())
# except FileNotFoundError:
#         print("File not found")

with open("./resources/movies.csv", "r") as file:
    print(file.name)
    print(file.read())
    
