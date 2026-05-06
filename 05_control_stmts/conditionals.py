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