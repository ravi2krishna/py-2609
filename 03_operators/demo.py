# Operators 

# Arithmetic Operators 
num1 = 10
num2 = 5

print("Sum Of Numbers: ", num1 + num2)
print("Difference Of Numbers: ", num1 - num2)
print("Product Of Numbers: ", num1 * num2)
print("Division Of Numbers: ", num1 / num2)
print("Modulus Of Numbers: ", num1 % num2)

print("Floor Division: ",num1 // num2 )
print("Normal Division: ", 3/2) # 1.5
print("Floor Division: ", 3//2) # 1
print("Exponentiation: ", 3 ** 2) # 3 ^ 2

print("========================")

# Compound Assignment Operators 
num = 10
num = num + 5 # long form
print(num) 

num = 10
num += 5 # short form
print(num) 


# Increment & Decrement increase or decrease a variable's value by one
# Increment & Decrement are used in Loops in our future sessions 
count = 0
print(count)
# count++ # SyntaxError: invalid syntax
count += 1 
print(count)

count = 10
print(count)
# count-- # SyntaxError: invalid syntax
count -= 1 
print(count)

print("========================")

# Comparison Operators
num1 = 3
num2 = 2

print(num1 == num2)
print(num1 > num2)
print(num1 != num2)

print("========================")

# Logical Operators 
num1 = 4
num2 = 3
num3 = 2
num4 = 1

print(num1 > num2 and num3 < num4) # T and F -> F
print(num1 > num2 and num3 > num4) # T and T -> T

print(num1 > num2 or num3 < num4) # T or F -> T
print(num1 < num2 or num3 < num4) # F or F -> F 

print(num1 < num2) # F
print(not num1 < num2) # F -> T

print("========================")

# Membership Operators 
data = "python is interpreted language"
find_word = "java"
status = find_word in data
print(status)

data = "python is interpreted language"
find_word = "python"
status = find_word in data
print(status)

# List Data Type -> Complex Data Type To Store Multiple Values, represented using []
employee_ids = ["101","102","103","104","105","1000"] 
find_emp_id = "108"
status = find_emp_id in employee_ids
print("Employee Found: ",status)

find_emp_id = "105"
status = find_emp_id in employee_ids
print("Employee Found: ",status)

find_emp_id = "108"
status = find_emp_id not in employee_ids
print("Employee Not Found: ",status)

print("========================")

# Identity Operators 
n1 = 10
n2 = 10
n3 = 5

print(n1 is n2)
print(id(n1))
print(id(n2))
print(id(n3))

print(n1 is n3)

print("========================")

# Bitwise Operators 
n1 = 5 # 0000000000000101
n2 = 3 # 0000000000000011
       # 0000000000000111 (|)
       # 0000000000000001 (&)

print(n1 & n2) # 1
print(n1 | n2) # 7

