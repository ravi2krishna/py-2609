# Exception Handling 

# When No Errors -> Nothing To Handle

print("Program Execution Started")

num1 = 10
num2 = 5

print("Result: ", num1/num2)

print("Program Execution Completed")

print("=" * 50)

# print("Program Execution Started")

# num1 = 10
# num2 = "5"

# print("Result: ", num1/num2)

# print("Program Execution Completed")

# print("=" * 50)

print("Program Execution Started")

num1 = 10
num2 = "5"

try:
    print("Result: ", num1/num2)
except:
    print("WARNING! Don't Divide Numerics With Strings")

print("Program Execution Completed")

print("=" * 50)

print("Program Execution Started")

num1 = 10
num2 = 5

try:
    print("Result: ", num1/num2)
except:
    print("WARNING! Don't Divide Numerics With Strings")

print("Program Execution Completed")

print("=" * 50)


# print("Program Execution Started")

# num1 = 10
# num2 = 0

# print("Result: ", num1/num2) # ZeroDivisionError: division by zero
# print("Program Execution Completed")

# print("=" * 50)

print("Program Execution Started")

num1 = 10
num2 = 0

try:
    print("Result: ", num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS! Check this - https://en.wikipedia.org/wiki/Division_by_zero")
print("Program Execution Completed")

print("=" * 50)

print("Program Execution Started")

num1 = 10
num2 = 3

try:
    print("Result: ", num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS! Check this - https://en.wikipedia.org/wiki/Division_by_zero")
print("Program Execution Completed")

print("=" * 50)

# When we come across multiple errors 
print("Program Execution Started")

# data = [1,2,'three',0,4]
# data = [1,2,0,4]
data = [1,2,4]

for num in data:
    print(1/num)
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero

print("Program Execution Completed")

print("=" * 50)


# When we come across multiple errors 
print("Program Execution Started")

data = [1,2,'three',0,4]

for num in data:
    try:
        print(1/num)
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero
    except:
        print("OOPS!!! Something Went Wrong")

print("Program Execution Completed")

print("=" * 50)

# When we come across multiple errors 
print("Program Execution Started")

data = [1,2,'three',0,4]

for num in data:
    try:
        print(1/num)
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero
    except TypeError:
        print("OOPS!!! Don't Divide Numerics With Strings")
        
    except ZeroDivisionError: 
        print("OOPS!!! Check this - https://en.wikipedia.org/wiki/Division_by_zero")   

print("Program Execution Completed")

print("=" * 50)


# else When there is no error 
print("Program Execution Started")

num1 = 10
num2 = 0

try:
    print("Result: ", num1/num2) # Verify Loin Credentials 
except:
    print("OOPS! Check this - https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Was Successful") # Then Only Check OTP

print("Program Execution Completed")

print("=" * 50)

# finally - Run this code for sure  
print("Program Execution Started")

num1 = 10
num2 = 5

try:
    print("Result: ", num1/num2) # Verify Loin Credentials 
except:
    print("OOPS! Check this - https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Was Successful") # Then Only Check OTP
finally:
    print("Closing All Opened File Streams & Database Connections")

print("Program Execution Completed")

print("=" * 50)

# Custom Exceptions
class MyCustomError(Exception):
    pass 

age = int(input("Enter Age: "))
if age < 18:
    print("You Cannot Vote")
else:
    print("You Can Vote")
    

# Custom Exceptions
class UnderAgeError(Exception):
    pass 

age = int(input("Enter Age: "))
if age < 18:
    # print("You Cannot Vote")
    # raise TypeError
    # raise UnderAgeError # ZeroDivisionError: division by zero
    # raise UnderAgeError("Below 18 Cannot Vote") # UnderAgeError: Below 18 Cannot Vote
    print("You Cannot Vote")
else:
    print("You Can Vote")
    
# Handle Custom Exceptions
class UnderAgeError(Exception):
    pass 

age = int(input("Enter Age: "))
try:
    if age < 18:
        # print("You Cannot Vote")
        # raise TypeError
        # raise UnderAgeError # ZeroDivisionError: division by zero
        raise UnderAgeError("Below 18 Cannot Vote") # UnderAgeError: Below 18 Cannot Vote
except UnderAgeError:
    print("You are not 18 Yet")
else:
    print("You Can Vote")
finally:
    print("Closing Program")