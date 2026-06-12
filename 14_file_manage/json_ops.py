# Working With JSON Files / Data 

import json 

student = {
    "id":"101",
    "name": "Ravi",
    "email": "ravi2krishna@gmail.com",
    "courses": ["python","ai","cloud"],
    "gpa":9.5
}

print(type(student))
print(student)

# Write Data To JSON File 
with open("14_file_manage/student.json","w") as file_data:
    json.dump(student,file_data)
    
    
# Write Data To JSON File With Indentation
with open("14_file_manage/student.json","w") as file_data:
    json.dump(student,file_data,indent=4)

print("=" * 50)
    
# Read Data From JSON File
with open("14_file_manage/student.json","r") as file_data:
    data = json.load(file_data)
    print(data)
    print(type(data))
    
print("=" * 50)

# Requirement: Get Student Name & Number Of Courses he joined from student.json file
with open("14_file_manage/student.json","r") as file_data:
    data = json.load(file_data)
    print(data)
print("Student Name: ",data['name'])
print("Student Joined Courses: ",data['courses'])
print("Total Courses Enrolled: ",len(data['courses']))

print("=" * 50)

# Requirement: Check If Student Passed Or Not, based on GPA above 7 from student.json 
with open("14_file_manage/student.json","r") as file_data:
    data = json.load(file_data)
    print(data)
    
if data['gpa'] >= 7:
    print("Student Passed")
else:
    print("Student Failed")

print("=" * 50)
    
# File Based -> dump() & load()

# Object Based -> dumps() & loads()

student = {
    "id":"101",
    "name": "Ravi",
    "email": "ravi2krishna@gmail.com",
    "courses": ["python","ai","cloud"],
    "gpa":9.5
}

print(type(student))
print(student)

print("=" * 50)

# dumps(): Convert a native Python dictionary into a formatted JSON string.
json_data = json.dumps(student)
print(type(json_data))
print(json_data)

print("=" * 50)

# loads(): Convert a text-based JSON string back into an interactive Python dictionary.
string_data = '{"id": "101", "name": "Ravi", "email": "ravi2krishna@gmail.com", "courses": ["python", "ai", "cloud"], "gpa": 9.5}'
print(type(string_data))
print(string_data)

python_dict = json.loads(string_data)
print(type(python_dict))
print(python_dict)

# Assume i'm a full stack developer 
# Requirement: We have an API, when requested we are getting JSON Data 
# https://dummyjson.com/
# https://dummyjson.com/users

import requests # First Install Module(pip install requests), then you can use it 
url = 'https://dummyjson.com/users'
response = requests.get(url)
print("HTTP Status Code: ",response.status_code)

print(response)
print(response.text)

print(type(response.text))

data_fetched = response.text
api_data_dict = json.loads(data_fetched)
print(type(api_data_dict))

# Requirements: Find Number Of Users in the platform 
all_users = api_data_dict['users']
print(all_users)
print("Number Of Users in the platform: ",len(all_users))

print("=" * 50)

# Requirements: Fetch all the usernames Of Users in the platform 
for user in all_users:
    # print(user)
    # print("=" * 20)
    print(user['id'],user['username'],user['age'])

print("=" * 50)
  
# Requirements: Fetch all the usernames Of "Young Users" in the platform i.e aged below 30
print("=" * 50)
print("Young Users List In Platform")
print("=" * 50)
for user in all_users:
    if user['age'] < 30:
        print(user['id'],user['username'],user['age'])