# Data Types 

# Numeric Types 

data = 10
print(type(data))

data = -10
print(type(data))

data = 10.5
print(type(data))

data = -10.5
print(type(data))

# complex number -> a + ib 
# data = 3 + i5 # Error
# print(type(data))

# complex number -> a + bj 
data = 3 + 5j # No Error
print(type(data))

data = True
print(type(data))

data = False 
print(type(data))

data = None 
print(type(data))

data = "python"
print(type(data))

# Complex Data Types 

# List
data = [10,20,30,40,50]
print(type(data))

# Tuple
data = (10,20,30,40,50)
print(type(data))

# Set
data = {10,20,30,40,50}
print(type(data))

# Frozenset
data = frozenset({10,20,30,40,50})
print(type(data))

# Dictionary 
data = {"course":"python","time":7,"duration":90}
print(type(data))
print(data)

# Custom Data Type For Student 
class Student:
    student_id = 101
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    student_contact = 9999999999
    student_gpa = 9.3
    student_enrolled_courses = ["Python","DevOps","AI"]
    
data = Student() # Object Creation Of Class 
print(type(data))
print(data) # Prints Object Reference 
print(data.student_name)

print("==============")

# Type Conversion / Implicit Conversion [Automatic]
n1 = 10  # int
n2 = 5.5 # float 
sum = n1 + n2 # float 
print(sum)
print(type(sum))

# Type Casting / Explicit Conversion [Manual]
price = 1128.85 # float 
print(price)
print(type(price))
# round_off_price = data_type(variable_name)
round_off_price = int(price)
print(round_off_price)
print(type(round_off_price))

# Some User in a web site was filling some form (text boxes) --> Behind the scenes these are strings
rating = "4" # input in web site
print(type(rating))
# if rating >= 4: # TypeError: '>=' not supported between instances of 'str' and 'int'
rating = int(rating)
if rating >= 4:
    print("Positive Feedback")
else:
    print("Negative Feedback")

    
    