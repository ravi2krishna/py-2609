# Working With CSV Files 

import csv

# Reading Data From CSV File 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        print(row)
        
print("=" * 50)

# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from Hyderabad 
# After Reading CSV File, we git List Format Data 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row[-1])
        if row[-1] == "Hyderabad":
            print(row)
            
print("=" * 50)

# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from tcs 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row[1])
        if row[1].endswith("@tcs.com"):
            print(row)
            
print("=" * 50)

# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from tcs and Hyderabad
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row[1])
        if row[1].endswith("@tcs.com") and row[-1] == "Hyderabad":
            print(row)
            
print("=" * 50)

# NOW DATA SETS ARE CHANGED
# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from Hyderabad 
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row[-1])
        if row[-1] == "Hyderabad":
            print(row)
            
print("=" * 50)

# Using DictReader For Dynamic Nature i.e CHANGING DATA SETS 
# NOW DATA SETS ARE CHANGED
# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from Hyderabad 
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        print(row) # Data is In Dictionary Format
        # {'name': 'Hari', 'mobile': '9889032187', 'address': 'Jaipur', 'email': 'hari193@outlook.com'}
        
        # Earlier Data Was in List Format when we used reader()
        # ['Naveen', 'naveen409@tcs.com', '9806720153', 'Hyderabad']
            
print("=" * 50)


# Using DictReader For Dynamic Nature i.e CHANGING DATA SETS 
# NOW DATA SETS ARE CHANGED
# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from Hyderabad 
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        # print(row) # Data is In Dictionary Format
        if row['address'] == "Hyderabad":
            print(row)
            
print("=" * 50)


# Using DictReader For Dynamic Nature i.e CHANGING DATA SETS 
# NOW DATA SETS ARE CHANGED
# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from Hyderabad 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        # print(row) # Data is In Dictionary Format
        if row['address'] == "Hyderabad":
            print(row)
            
print("=" * 50)

# Create and Write Data To CSV File
with open("14_file_manage/emp.csv","w") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(['name', 'email', 'mobile', 'address'])
    csv_writer.writerows([['Ravi', 'ravi186@tcs.com', '9876055200', 'Bangalore'],
                        ['Ramu', 'ramu661@tcs.com', '9833214959', 'Bangalore'],
                        ['Deepak', 'deepak641@tcs.com', '9369382025', 'Chennai']])
    
    
# Create and Write Data To CSV File
fieldnames = ['name', 'email', 'mobile', 'address']
with open("14_file_manage/new.csv","w") as file_data:
    # csv_writer = csv.DictWriter(file_data) # TypeError: DictWriter.__init__() missing 1 required positional argument: 'fieldnames'
    csv_writer = csv.DictWriter(file_data,fieldnames=fieldnames)
    # Write the column header row
    csv_writer.writeheader()
    csv_writer.writerow({'name': 'Naveen', 'email': 'naveen409@tcs.com', 'mobile': '9806720153', 'address': 'Hyderabad'})
    csv_writer.writerows([
                        {'name': 'Ravi', 'email': 'ravi896@yahoo.com', 'mobile': '9113675924', 'address': 'Hyderabad'},
                        {'name': 'Sunil', 'email': 'sunil205@yahoo.com', 'mobile': '9507396790', 'address': 'Hyderabad'},
                        {'name': 'Vijay', 'email': 'vijay234@yahoo.com', 'mobile': '9540482452', 'address': 'Hyderabad'}
                        ])