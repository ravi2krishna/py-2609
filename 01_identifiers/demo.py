# This is Comment - Python Ignores this line 
# This is Comment - Python Ignores this line  # SyntaxError: invalid syntax

print()
print(10)
print(10.5)
print(-10)

# print(a) # NameError: name 'a' is not defined
# print(ten) # NameError: name 'ten' is not defined. Did you mean: 'len'?

print('a')
print("b")
print("ten")

# Identifiers
# today # "today" is not defined
today = "wednesday"
print(today)

# 2day = "wednesday" # SyntaxError
# print(2day)

day2moro = "thursday"
print(day2moro)

# $2moro = "thursday" # SyntaxError
# print($2moro)

_2moro = "thursday" 
print(_2moro)

# Improper Way Of Naming Identifiers
x = "Ravi"
y = 25
z = 9.5

# Proper Way Of Naming Identifiers
student_name = "Ravi"
student_age = 25
student_gpa = 9.5

# Static Data / Fixed Data 
math_pi = 3.14159265359 # Not Recommended
print(math_pi)

MATH_PI = 3.14159265359 # Recommended
print(MATH_PI)

student_aadhar_id = 123456789012 # Not Recommended
print(student_aadhar_id)

STUDENT_AADHAR_ID = 123456789012 # Recommended
print(STUDENT_AADHAR_ID)