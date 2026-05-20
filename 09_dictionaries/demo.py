# Dictionaries

# empty Dictionary 
empty_dict = {}
print(empty_dict)
print(type(empty_dict))

empty_dict = dict()
print(empty_dict)
print(type(empty_dict))

# Dictionary with Numeric Data 
data = {1:10,2:20,3:30,4:40,5:50}
print(data)

# Dictionary with Text Data 
data = {"c1":"python","c2":"ai","c3":"cloud"}
print(data)

# Tuple with Mixed Data 
data = {1:10,2:20,3:30,"c1":"python","c2":"ai","avg":5.5,"passed":True}
print(data)

# Accessing Data In Dictionaries
data = {1:10,2:20,3:30,4:40,5:50}
print(data)

# first element 
# first_element = data[0] # KeyError: 0
first_element = data[1]
print(first_element)

# last element 
# last_element = data[-1] # KeyError: -1
last_element = data[5]
print(last_element)

# unknown_element = data[10]
# print(unknown_element) # KeyError: 10

# Access Individual Elements 
data = {1:10,2:20,3:30,4:40,5:50}
print(data)
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[5])

# Access Individual Elements -> 10k elements
data = {1:10,2:20,3:30,4:40,5:50,1000:10000}
print(data)
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[5])
print(data[1000])

# Access Individual Elements -> 10k elements
data = {1:10,2:20,3:30,4:40,5:50,1000:10000}
# print(dir(data)) # '__iter__
for num in data: # Only keys we got
    print(num)
    
for key in data: # Only keys we got
    print(key) 
    
for key in data: # Access Values, using key 
    print(data[key])
    
# Apply Operators -> Requirements: Multiply Each Number with 10
data = {1:10,2:20,3:30,4:40,5:50,1000:10000}
for key in data:
    print(key * 10)
    
# Apply Operators -> Requirements: Multiply Each Number with 10
data = {1:10,2:20,3:30,4:40,5:50,1000:10000}
for key in data:
    print(data[key] * 10)
    
# Apply Operators -> Requirements: Give Courses in Upper Case
data = {"c1":"python","c2":"ai","c3":"cloud"}
for course in data:
    print(data[course].upper())
    
# Apply Conditionals -> Requirements: Give Only Even Numbers
data = {1:10,2:20,3:35,4:40,5:55,1000:10000}
for key in data:
    if data[key] % 2 == 0:
        print(data[key])
        
# Duplicates Allowed - value duplicates allowed 
data = {1:10,2:20,3:30,4:40,5:50,6:20}
print(data)

# Duplicates Allowed - keys duplicates allowed, but latest will override previous key  
data = {1:10,2:20,1:30,4:40,1:50,6:20}
print(data)

# insertion order preserved
data = {1:10,2:20,3:30,4:40,5:50,1000:10000}
print(data)

# keys should be immutable objects
# data = {['ten']:10,['twenty']:20} # TypeError: unhashable type: 'list'
# print(data)

# keys should be immutable objects
data = {('ten'):10,('twenty'):20} # TypeError: unhashable type: 'list'
print(data)

# Immutability
data = {1:10,2:20,3:30,4:40,5:50,1000:10000}
print(data)
data[1] = 100 
print(data)

# Real World Dictionaries Looks like JSON Data 
# https://media.licdn.com/dms/image/v2/D4D12AQGwOUMYbhUu-A/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1682148646113?e=2147483647&v=beta&t=qeCSY5Ktzx2jkeq7suYaSBV_-OS_18P-yuabrIhNWcU
# https://www.anbowell.com/_astro/guide_to_json.DimYsN86.webp
# https://www.goanywhere.com/sites/default/files/styles/max_2600x2600/public/2022-08/example_json_file_0.png.webp?itok=nS3qt8dd

students = {"101":{},"102":{}}
print(type(students))

students = {
    "101": {
        "name": "Ravi",
        "email": "ravi2krishna@gmail.com",
        "courses": ["python","ai","cloud"],
        "courses_fee": (10000,20000,20000)
    },
    "102": {
        "name": "Mike",
        "email": "mike@microsoft.com",
        "courses": ["java","ai","devops"],
        "courses_fee": (10000,20000,20000)
    }
}
print(type(students))

# Get all Students Data 
print(students)

print("=" * 50)

# Get 101 Student Details
# student_id = 101
student_id = "101"
print(students[student_id])

print("=" * 50)
print(students["101"])

print("=" * 50)

# Get Courses Enrolled by Mike 
print(students["102"])
print(students["102"]["courses"])

# Get 2nd Course Enrolled by Mike 
print(students["102"]["courses"][1])

print("=" * 50)

# Check if mike is a google customer or not 
print(students["102"]["email"])
if students["102"]["email"].endswith("@gmail.com"):
    print(f"User {students["102"]['name']} is Google Customer")
else:
    print(f"User {students["102"]['name']} is Not Google Customer")


# Dictionary Operations 
print(dir(data))
