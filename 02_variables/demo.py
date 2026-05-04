# Variables

# Assign Data (Store Data)
student_name = "Ravi" # String
student_age = 25 # int
student_gpa = 9.5
student_passed = True 
STUDENT_AADHAR = None # Absence Of Value

# Retrieve Data (Get Data)
print(student_name)
print(student_age)
print(student_gpa)
print(student_passed)
print(STUDENT_AADHAR)

# Concatenation: Joining Strings Using + Operator
print("======== Student Info ========")
# print("Student Name: Krishna") # Static
print("Student Name: " + student_name)
# print("Student Age: " + student_age) # TypeError: can only concatenate str (not "int") to str
print("Student Age: ", student_age) # Using , Operator 
print("Student GPA: ", student_gpa)
print("Did Student Pass: ", student_passed)
print("Student AADHAR ID: ", STUDENT_AADHAR)
print("======== Student Info ========")

# type(): Used to tell Data Type 
type(student_name)
print(type(student_name))
print(type(student_age))
print(type(student_gpa))
print(type(student_passed))
print(type(STUDENT_AADHAR))

print("====================")

# id(): Used to Get Memory Address 
id(student_name)
print(id(student_name))
print(id(student_age))
print(id(student_gpa))
print(id(student_passed))
print(id(STUDENT_AADHAR))

print("====================")

# Memory Model In Python 
value_x = 10
print(id(value_x))

value_y = 100
print(id(value_y))

value_z = 10
print(id(value_z))
