# Functional Programming 

# Without Functions 

# User One wants to calculate for below values
num1 = 10
num2 = 5

# Math Operations 
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 10)

# Another User wants to calculate for below values
num1 = 20
num2 = 5

# Math Operations 
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 10)

# Another User wants to calculate for below values
num1 = 200
num2 = 50

# Math Operations 
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 10)

# With Functions
def math_ops():
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)

# User One wants to calculate for below values
print("User 1")
num1 = 10
num2 = 5
math_ops()

print("User 2")
# Another User wants to calculate for below values
num1 = 20
num2 = 5
math_ops()

print("User 3")
# Another User wants to calculate for below values
num1 = 200
num2 = 50
math_ops()

print("=" * 20)

# math_ops(10,5) # TypeError: math_ops() takes 0 positional arguments but 2 were given
   

# Functions With Parameters 
def math_ops(num1, num2): # num1, num2 are Parameters
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)
    
# math_ops() # TypeError: math_ops() missing 2 required positional arguments: 'num1' and 'num2'
math_ops(10,5) # ("User 1")
math_ops(20,5) # ("User 2")
math_ops(200,50) # ("User 2")

print("=" * 50)

# Positional Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")
    
employee_info("Hyderabad","Ravi","ravi2krishna@gmail.com") # incorrect order 
employee_info("Ravi","ravi2krishna@gmail.com","Hyderabad") # correct order

print("=" * 50)

# Keyword Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")
    
employee_info("Hyderabad","Ravi","ravi2krishna@gmail.com") # incorrect - using positional approach
employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi2krishna@gmail.com") # using Keyword approach

print("=" * 50)

# Without Default Arguments
def employee_info(emp_name,emp_email,emp_location,org_name):
    print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")

employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi2krishna@gmail.com",org_name="IBM")
employee_info(emp_location="Bangalore",emp_name="Krishna",emp_email="krishna@gmail.com",org_name="IBM") 
employee_info(emp_location="Pune",emp_name="Sam",emp_email="sam@gmail.com",org_name="IBM") 

print("=" * 50)

# With Default Arguments
def employee_info(emp_name,emp_email,emp_location,org_name="TCS"):
    print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")

employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi2krishna@gmail.com")
employee_info(emp_location="Bangalore",emp_name="Krishna",emp_email="krishna@gmail.com") 
employee_info(emp_location="Pune",emp_name="Sam",emp_email="sam@gmail.com",org_name="IBM") 

print("=" * 50)

# Placement Requirement With Default Arguments
# def employee_info(emp_name,emp_email,emp_location,org_name="TCS",emp_mobile):
#     print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")

# Non-default argument follows default argument
# SyntaxError: parameter without a default follows parameter with a default

def employee_info(emp_name,emp_email,emp_location,emp_mobile,org_name="TCS"):
    print(f"Hi {emp_name} your email is {emp_email} with mobile number {emp_mobile} and working for {org_name} at location {emp_location}")
    
employee_info(emp_location="Bangalore",emp_name="Krishna",emp_email="krishna@gmail.com",emp_mobile=9999999999) 
employee_info(emp_location="Pune",emp_name="Sam",emp_email="sam@gmail.com",org_name="IBM",emp_mobile=8888888888) 

print("=" * 50)

# Without Arbitrary Positional Arguments
def add_numbers_one(n1):
    print(n1)
    
def add_numbers_two(n1,n2):
    print(n1+n2)
    
def add_numbers_three(n1,n2,n3):
    print(n1+n2+n3)
    
add_numbers_one(10)
add_numbers_two(10,20)
add_numbers_three(10,20,30)

# add_numbers_three(10,20,30,40,50,60,70,80,90,100)

print("=" * 50)

# With Arbitrary Positional Arguments
def add_numbers(*numbers):
    print(numbers) 

add_numbers(10)
add_numbers(10,20,30)
add_numbers(10,20,30,40,50,60,70,80,90,100)

def add_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num 
    print(f"Total Sum is {total}")

add_numbers(10)
add_numbers(10,20,30)
add_numbers(10,20,30,40,50,60,70,80,90,100)


def profile(*info):
    print(info)
    
profile("ravi","krishna")
profile("ravi","krishna",9989898989)
profile("ravi","krishna",9989898989,False)

# Real world use case w.r.t Ecommerce Applications Cart Functionality 
def cart_total_value(*products):
    total = 0
    for product in products:
        total += product 
    print(f"Total Cart Value is ₹ {total}")

cart_total_value(268.98,599,1178)

print("=" * 50)

# Arbitrary Keyword Arguments
def profile(**info):
    print(info)
    
profile(fname="Ravi")
profile(fname="Ravi",lname="Krishna")
profile(fname="Ravi",lname="Krishna",mobile=90909090)

print("=" * 50)

def profile(**info):
    for data in info:
        # print(data) # key
        print(info[data]) # value 

profile(fname="Ravi",lname="Krishna",mobile=90909090)

print("=" * 50)

# Real World Use Case -> jan=3000, feb=4500, mar=9000
# Real World Use Case -> jan=3000, feb=4500, mar=9000, apr=6000
# Real World Use Case -> jan=3000, feb=4500, mar=9000, apr=6000, may=3000
# Requirement: Calculate Total Transaction Amount and Number Of Transactions Made

def bank_transactions(**transactions):
    print(transactions)
    total_transactions_value = 0
    number_of_transactions = 0
    for transaction in transactions:
        # total_transactions_value += transaction # TypeError: unsupported operand type(s) for +=: 'int' and 'str'
        total_transactions_value += transactions[transaction]
        number_of_transactions += 1
    print(f"Total Transactions Amount is {total_transactions_value} for {number_of_transactions} Transactions")

    
bank_transactions(jan=3000, feb=4500, mar=9000)
bank_transactions(jan=3000, feb=4500, mar=9000, apr=6000, may=3000)

# pid_101=[name,desc,quantity], feb=4500, mar=9000

print("=" * 50)

# Without return 
def add(a,b):
    a + b
    
add(100,200)
print(add(100,200))

# With return 
def add(a,b):
   return a + b
    
add(100,200)
print(add(100,200))

# function composition
def sub(c,d,e): # add c & d then minus e --> c + d - e
    return add(c,d) - e

print(sub(3,4,5))

