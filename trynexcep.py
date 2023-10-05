class Division:

    def divide_me(self, num, denom):
        return num/denom
    
division = Division()
print(division.divide_me(4, 2))

class Converter:

    def divide(self, num, denom):
        #the try is where u put the code that is prone to error
        try: 
            result = num / denom
        
        #in the exvept block u write a code that will handle the error
        except ZeroDivisionError:
        #except (ZeroDivisionError, TypeError) as e:
        #print(f"Cant do this - {e}")
            print("Cant do this")
        except SyntaxError:
            print("Syntax error")
        #else block to return what should happen if you dont get any exception
        else:
            print(f"Your result is - {result}")
        #finally will run if there is an exception or not
        finally:
            print("THis is the last statement")

converter = Converter()
converter.divide(12, 0)

#u can create a class exception that is inheriting from the parent class exception

#bad code
userNumber = input("Enter your number ")
userNumber = float(userNumber)
result = userNumber + 2

#good code

userNumber = input("Enter your number ")
try: 
    userNumber = float(userNumber)
except Exception:
    print("Invalid Number")
else:
    result = userNumber + 2
    print(result)
finally:
    print("Thank You")
