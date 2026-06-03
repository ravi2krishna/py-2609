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

# return - make sure it's the last part of statement to be executed
def add(a,b):
    print("Calculation Started")
    return a + b
    print("Calculation Completed") # Code is structurally unreachable

print(add(10,20))

a = 50
a = 60
a = 70 
print(a)

# multiple return statements, first return will be considered
def math_ops(num1,num2):
    return num1 + num2
    return num1 - num2
    return num1 * num2

print(math_ops(2,3))

# multiple returns are present, and used with conditionals, you can control the flow 
def math_ops(num1,num2,operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    else:
        return "Invalid Operator"
    
print(math_ops(20,10,"+"))
print(math_ops(20,10,"-"))
print(math_ops(20,10,"*"))
print(math_ops(20,10,"/"))
    
# Local Scope
def add():
    la = 10 # local variable - declared "inside the function" 
    lb = 20 # local variable - declared "inside the function" 
    print(la)
    print(lb)
    
add()

# print(la) # NameError: name 'la' is not defined. Did you mean: 'a'?
# print(lb)


# Parameters we are passing to the functions, are also local variables  
def add(la,lb): # local variable  are la and lb
    print(la)
    print(lb)

add(40,50)
# print(la) # NameError: name 'la' is not defined. Did you mean: 'a'?

# Global Scope
ga = 100
def add(la,lb): # local variable  are la and lb
    print(la)
    print(lb)
    print(ga) # global variable, accessed within function 
    
add(80,90)
print(ga)

# name conflicts
ga = 500
def add(la,lb,ga): # local variable  are la and lb
    print(la)
    print(lb)
    print(ga) # global variable, accessed within function 
    
add(10,20,30)


ga = 500
def add(la,lb,ga): # local variable  are la and lb
    print(la)
    print(lb)
    print(ga) # global variable, accessed within function 
    print(globals()['ga'])
    
add(40,50,60)

# global variables outside the function
count = 0
print(count)
count += 1
print(count)

# global variables inside the function
count = 0
print(count)
def increment():
    global count
    count += 1 # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
    return count 

print(increment()) 

# without lambda i.e regular functions
def add(a,b):
    return a + b 
print(add(200,300))

# with lambda functions
# lambda arguments:expression
lambda a,b:a+b # one liner function 
print((lambda a,b:a+b)(10,20))

# without lambda
def is_even_num(num):
    if num % 2 == 0:
        return True
    else:
        return False 
    
print(is_even_num(11))
print(is_even_num(10))

# with lambda
# lambda arguments:expression
lambda num:num % 2 == 0
print((lambda num:num % 2 == 0)(10))
print((lambda num:num % 2 == 0)(15))
print((lambda num:num % 2 == 0)(12))

# without lambda
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")
employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi2krishna@gmail.com")

# with lambda
# lambda arguments:expression
# lambda emp_name,emp_email,emp_location:print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")
print((lambda emp_name,emp_email,emp_location:print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}"))(emp_location="Pune",emp_name="Krishna",emp_email="ravi2krishna@gmail.com"))

# Without Higher Order Functions - map()
# Write a script/program to take a list of numbers and return the square of list of numbers
# [1,2,3,4,5]   ==>     [1,4,9,16,25]
def square_list(numbers):
    squared_list = []
    for num in numbers:
        squared_list.append(num * num)
    return squared_list

print(square_list([1,2,3,4,5]))


# With Higher Order Functions - map()
# Write a script/program to take a list of numbers and return the square of list of numbers
# [1,2,3,4,5]   ==>     [1,4,9,16,25]
# map(function, iterable)
map((lambda num:num*num), [1,2,3,4,5])
print(map((lambda num:num*num), [1,2,3,4,5]))
print(list(map((lambda num:num*num), [1,2,3,4,5]))) # one line function 

# Real World Use Case Of Working with Lambda & Higher Order Functions 
products = [
    {"name": "Laptop", "price": 80000, "discount": 10},
    {"name": "Phone", "price": 50000, "discount": 5},
    {"name": "Headphones", "price": 2000, "discount": 15},
    {"name": "Charger", "price": 1500, "discount": 0},
    {"name": "Camera", "price": 30000, "discount": 20},

    {"name": "Tablet", "price": 25000, "discount": 10},
    {"name": "Monitor", "price": 12000, "discount": 8},
    {"name": "Keyboard", "price": 2000, "discount": 5},
    {"name": "Mouse", "price": 1000, "discount": 0},
    {"name": "Printer", "price": 15000, "discount": 12},

    {"name": "Smartwatch", "price": 7000, "discount": 18},
    {"name": "Speaker", "price": 3500, "discount": 10},
    {"name": "PowerBank", "price": 1800, "discount": 7},
    {"name": "Router", "price": 2500, "discount": 5},
    {"name": "HardDisk", "price": 6000, "discount": 15},

    {"name": "SSD", "price": 5500, "discount": 20},
    {"name": "Webcam", "price": 2200, "discount": 10},
    {"name": "Microphone", "price": 3000, "discount": 12},
    {"name": "Projector", "price": 40000, "discount": 25},
    {"name": "Drone", "price": 75000, "discount": 30},

    {"name": "TV", "price": 45000, "discount": 18},
    {"name": "GamingConsole", "price": 38000, "discount": 15},
    {"name": "VRHeadset", "price": 20000, "discount": 22},
    {"name": "GraphicsCard", "price": 65000, "discount": 10},
    {"name": "Motherboard", "price": 12000, "discount": 8}
]

# find me prices after discounts  i.e Imperative Style What To Do 

prices_after_discounts = []
for product in products:
    print(product)
    price = product['price']
    print(price)
    discount = product['discount']
    print(discount)

    price_after_discount = price - (price * discount / 100)
    print(price_after_discount)
    prices_after_discounts.append(price_after_discount)
    
print("Prices After Discount: ",prices_after_discounts)

print("=" * 50)

# find me prices after discounts  i.e Declarative Style How To Do 
print(list(map((lambda product:product['price'] - product['price'] * product['discount']/100), products))) # one line function 

print("=" * 50)

# Without filter() 
# Write a script/program to take a list of numbers and return the even list of numbers 
# [1,2,3,4,5,6,7,8,9,10]    ==>     [2,4,6,8,10]

def even_list(numbers):
    evened_list = []
    for num in numbers:
        if num % 2 == 0:
            evened_list.append(num)
    return evened_list

print(even_list([1,2,3,4,5,6,7,8,9,10]))

# With filter() 
# Write a script/program to take a list of numbers and return the even list of numbers 
# [1,2,3,4,5,6,7,8,9,10]    ==>     [2,4,6,8,10]
# filter(function, iterable)
filter((lambda num:num%2 == 0), [1,2,3,4,5,6,7,8,9,10])
print(filter((lambda num:num%2 == 0), [1,2,3,4,5,6,7,8,9,10]))
print(list(filter((lambda num:num%2 == 0), [1,2,3,4,5,6,7,8,9,10]))) # one line function 

print("=" * 50)

# Real World Use Case Of Working with Lambda & Higher Order Functions 
products = [
    {"name": "Laptop", "price": 80000, "discount": 10},
    {"name": "Phone", "price": 50000, "discount": 5},
    {"name": "Headphones", "price": 2000, "discount": 15},
    {"name": "Charger", "price": 1500, "discount": 0},
    {"name": "Camera", "price": 30000, "discount": 20},

    {"name": "Tablet", "price": 25000, "discount": 10},
    {"name": "Monitor", "price": 12000, "discount": 8},
    {"name": "Keyboard", "price": 2000, "discount": 5},
    {"name": "Mouse", "price": 1000, "discount": 0},
    {"name": "Printer", "price": 15000, "discount": 12},

    {"name": "Smartwatch", "price": 7000, "discount": 18},
    {"name": "Speaker", "price": 3500, "discount": 10},
    {"name": "PowerBank", "price": 1800, "discount": 7},
    {"name": "Router", "price": 2500, "discount": 5},
    {"name": "HardDisk", "price": 6000, "discount": 15},

    {"name": "SSD", "price": 5500, "discount": 20},
    {"name": "Webcam", "price": 2200, "discount": 10},
    {"name": "Microphone", "price": 3000, "discount": 12},
    {"name": "Projector", "price": 40000, "discount": 25},
    {"name": "Drone", "price": 75000, "discount": 30},

    {"name": "TV", "price": 45000, "discount": 18},
    {"name": "GamingConsole", "price": 38000, "discount": 15},
    {"name": "VRHeadset", "price": 20000, "discount": 22},
    {"name": "GraphicsCard", "price": 65000, "discount": 10},
    {"name": "Motherboard", "price": 12000, "discount": 8}
]

# Find the Premium Products i.e product with price above 25000
# Without filter()
premium_products = []

for product in products:
    price = product['price']
    if price > 25000:
       premium_products.append(product)
       
print("All Products: ",products) 
print("Premium Products: ",premium_products)

print("=" * 50)

print(premium_products[0]['name'], premium_products[0]['price'])

print("=" * 50)

# Find the Premium Products i.e product with price above 25000
# With filter()
# filter(function, iterable)
# print(list(filter((lambda num:num%2 == 0), [1,2,3,4,5,6,7,8,9,10]))) # one line function 
print(list(filter((lambda product: product['price'] > 25000), products))) # one line function 
premium_products = list(filter((lambda product: product['price'] > 25000), products))
print(premium_products)

print("=" * 50)

for product in premium_products:
    print(product['name'], product['price'])
    
# Real World Data Looks and Comes like this in the form of a "file" (csv & xls files) 
# https://e.nodegoat.net/CMS/upload/guide-import_person_spreadsheet_excel.png