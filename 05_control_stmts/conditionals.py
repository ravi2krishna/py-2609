# Indentation 

print("Hello")
print("Python")
# print("Ravi")
#  print("Ravi") # IndentationError: unexpected indent
 
# Indentation defines the structure and hierarchy of "code blocks"

# if 
# if True: # IndentationError: expected an indented block after 'if' statement on line 11
# print("This")
# print("Is")
# print("The")
# print("Of")
# print("Code")
# print("To")
# print("Execute")

if True: # IndentationError: expected an indented block after 'if' statement on line 11
 print("This")
 print("Is")
 print("The")
 print("Of")
 print("Code")
 print("To")
 print("Execute")

# Inconsistent number of spaces 
# if True: # IndentationError: expected an indented block after 'if' statement on line 11
#    print("This")
#  print("Is")
#    print("The")
#     print("Of") 
#    print("Code")
#    print("To")
#    print("Execute")

# Consistent number of spaces    
if True: # IndentationError: expected an indented block after 'if' statement on line 11
   print("This")
   print("Is")
   print("The")
   print("Of")
   print("Code")
   print("To")
   print("Execute")
   
# Consistent number of spaces and Recommended Way is using 4 Spaces i.e Tab
if True: 
    print("This")
    print("Is")
    print("The")
    print("Of")
    print("Code")
    print("To")
    print("Execute")
    
# in if condition, if the condition is False 
if False: # Code is not analyzed because condition is statically evaluated as false
    print("This")
    print("Code")
    print("Will")
    print("Never")
    print("Execute")
    
if True:
    print("This")
    print("Is")
    
if True:
 print("Code")
 print("To")
 print("Execute")
 
# if condition use with dynamic condition
if 5 > 2:
    print("Yes 5 > 2 is correct")

if 5 < 2:
    print("Yes 5 < 2 is correct")
    
num = 10
if num > 0:
    print("Given Num is Positive")
if num < 0:
    print("Given Num is Negative")
    
num = -10
if num > 0:
    print("Given Num is Positive")
if num < 0:
    print("Given Num is Negative")

print("================")
    
# if-else 
num = 10
if num > 0:
    print("Given Num is Positive")
else:
    print("Given Num is Negative")

print("================")

# without input() data is Fixed 
name = "Ravi" # this is always fixed i.e Static 
print(name)

# input() - reads the input
name = input("Enter Your Name: ") # this is Dynamic 
print(name)
print("Welcome: "+name) # Concatenation 
print("Welcome: ",name) # Comma operator 
print("Welcome: {name}") # No Interpolation
print(f"Welcome: {name}") # Interpolation

# if else with dynamic nature 
num = input("Enter Number: ")
num = int(num)
if num > 0: # TypeError: '>' not supported between instances of 'str' and 'int'
    print(f"Given Num {num} is Positive")
else:
    print(f"Given Num {num} is Negative")
    
# Voting App Dynamic 
age = int(input("Enter Your Age: "))
# age = input("Enter Your Age: ")
# age = int(age)
if age >= 18:
    print("You Can Vote")
else:
    print(f"You Cannot Vote as you are still {age} years only")
    
# Conditional Expression
# value_if_true if condition else value_if_false 
age = int(input("Enter Your Age: "))
status = "You Can Vote" if age >= 18 else "You Cannot Vote"
print(status)

# elif ladder 
marks = int(input("Enter Marks: "))
if marks >= 35:
    print("PASSED")
else:
    print("FAILED")

# Check for Grades 
marks = int(input("Enter Marks: "))
if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
elif marks >= 60:
    print("C Grade")
elif marks >= 50:
    print("D Grade")
elif marks >= 35:
    print("E Grade")
else:
    print("FAILED")

# match case 
error_code = int(input("Enter Error Code You See: "))
match error_code:
    case 200:
        print("Success - OK")
    case 401:
        print("Unauthorized")
    case 404:
        print("Not Found")
    case _:
        print("Unknown Error")