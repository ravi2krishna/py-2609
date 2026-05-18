# tuples 

# empty tuple 
empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

empty_tuple = tuple()
print(empty_tuple)
print(type(empty_tuple))

# Tuple with Numeric Data 
data = (10,20,30,40,50)
print(data)

# Tuple with Text Data 
data = ("python","ai","cloud")
print(data)

# Tuple with Mixed Data 
data = (10,20,30,"python","ai",5.5,True)
print(data)

# Accessing Data In Lists
data = (10,20,30,40,50)
print(data)

# first element 
first_element = data[0]
print(first_element)

# last element 
last_element = data[-1]
print(last_element)

# unknown_element = data[10]
# print(unknown_element) # IndexError: tuple index out of range

# Slicing In Lists same as strings 
data = (10,20,30,40,50)
print(data)
print(data[1:3:1]) # 20,30
print(data[0:5:2]) # 10,30,50

# Access Individual Elements 
data = (10,20,30,40,50)
print(data)
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])

# Access Individual Elements -> 10k elements
data = (10,20,30,40,50,10000)
print(data)
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])
# print(data[9999])

# Access Individual Elements -> 10k elements
data = (10,20,30,40,50,10000)
# print(dir(data)) # '__iter__
for num in data:
    print(num)
    
# Apply Operators -> Requirements: Multiply Each Number with 10
data = (10,20,30,40,50,10000)
for num in data:
    print(num * 10)
    
# Apply Operators -> Requirements: Give Courses in Upper Case
data = ("python","ai","cloud")
for course in data:
    print(course.upper())
    
# Apply Conditionals -> Requirements: Give Only Even Numbers
data = (10,20,35,40,55)
for num in data:
    if num % 2 == 0:
        print(num)
        
# Duplicates Allowed 
data = (10,20,35,20,40,55,20)
print(data)

# Insertion Order Is Preserved 
data = (10,20,35,20,40,55,20)
print(data)

# Tuple Operations 
print(dir(data))