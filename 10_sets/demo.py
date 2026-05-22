# Sets 

# empty set 
empty_set = {}
print(empty_set)
print(type(empty_set))

empty_set = set()
print(empty_set)
print(type(empty_set))

# Set with Numeric Data 
data = {10,20,30,40,50}
print(type(data))

data = [10,20,30,40,50]
print(type(data))
print(data) # List is Ordered Collection

data = {10,20,30,40,50}
print(type(data))
print(data) # Set is unordered Collection

# Set with Text Data 
data = {"python","ai","cloud"}
print(data)

# Set with Mixed Data 
data = {10,20,30,"python","ai",5.5,True}
print(data)

# Accessing Data In Lists
data = {10,20,30,40,50}
print(data)

# first element 
# first_element = data[0] # TypeError: 'set' object is not subscriptable
# print(first_element)

# last element 
# last_element = data[-1]
# print(last_element)

# Access Individual Elements -> 10k elements
data = {10,20,30,40,50,10000}
print(data)
# print(dir(data)) # '__iter__'
for num in data:
    print(num)
    
# Apply Operators -> Requirements: Multiply Each Number with 10
data = {10,20,30,40,50,10000}
for num in data:
    print(num * 10)

# Apply Operators -> Requirements: Give Courses in Upper Case
data = {"python","ai","cloud"}
for course in data:
    print(course.upper())
    
# Apply Conditionals -> Requirements: Give Only Even Numbers
data = {10,20,35,40,55}
for num in data:
    if num % 2 == 0:
        print(num)
        
# Duplicates Allowed 
# Insertion Order Is Not Preserved 
data = {10,20,35,20,40,55,20} 
print(data)

# Set Operations 
print(dir(data))


# frozenset 
data = {10,20,30,40,50}
print(type(data))
print(data)

data = frozenset({10,20,30,40,50})
print(type(data))
print(data)

print(dir(data))