# String Methods 

# Simulate Gmail Functionality 
#                   RaVI2KRiShNa -> ravi2krishna@gmail.com 

email = input("Enter Email ID: ")
print("Original Email Given: "+email)
# lower(): Converts the string to lowercase 
transformed_email = email.lower()
print("Transformed Email: "+transformed_email)

# strip(): Removes spaces from both ends
# lstrip(): Removes spaces from the left side (start) only
# rstrip(): Removes spaces from the right side (end) only
transformed_email = transformed_email.strip()
print("Transformed Email: "+transformed_email)

# add domain @gmail.com using concatenation 
domain = "@gmail.com"
transformed_email = transformed_email + domain
print("Final Transformed Email: "+transformed_email)

# Simulate PAN Functionality 
# https://www.pan.utiitsl.com/
pan = input("Enter PAN ID: ")
print("Original PAN: "+pan) # @amopl9912w

# isalnum() method returns True if all characters in a string are alphanumeric (letters or numbers) otherwise False
valid_pan = pan.isalnum()
print(f"Given PAN {pan} is {valid_pan}")

if pan.isalnum() and len(pan) == 10:
    print("Original PAN: "+pan)
    # upper() method returns a new string where all lowercase characters are converted to uppercase
    print("Transformed PAN: "+pan.upper())
else:
    print(f"Given PAN {pan} is INVALID")
    
    
# Simulate Phone ISD Scenario 
# https://us1.discourse-cdn.com/flex016/uploads/weweb/original/2X/d/dbe25afb4aeb05640347e2f7c1b7ae532ebb28f2.png
# https://www.businessbloomer.com/wp-content/uploads/2014/11/woocommerce-add-coupon-automatically-to-cart-if-product.png

# startswith() used to check if a string starts with a specific substring
# endswith() used to check if a string ends with a specific substring

contact_number = input("Enter Contact Number Starting With ISD CODE: ")
# contact_number = contact_number.startswith("+91")
print(f"India Number {contact_number}")

if contact_number.startswith("+91"):
    print("Calling India - Charged In Rupees")
elif contact_number.startswith("+33"):
    print("Calling France - Charged In Euros")
elif contact_number.startswith("+1"):
    print("Calling USA - Charged In Dollars")
else:
    print("Invalid Number - Only India, France & USA Supported")
    
# Simulate Email Synchronization 
# endwith() method returns True if the string ends with the specified value, otherwise False.
source_email = input("Enter Source Email ID: ")
destination_email = input("Enter Destination Email ID: ") 

if source_email.endswith("@gmail.com") and destination_email.endswith("@gmail.com"):
    print("Email Backup Process Started")
else:
    print("Email Backup Process Failed - Source & Destination Didn't Match")
    
# Simulate Data Operations Work: CSV Data from a file and perform some operations 
# https://www.datablist.com/learn_images/csv/google_sheet_csv.png
# https://www.slashgear.com/img/gallery/csv-files-explained-what-they-are-and-how-to-open-them/what-are-csv-files-1699455969.jpg
# Name,Email,Age,City,Job_Role
# emp_data = "John,john@apple.com,30,Hyderabad,Developer"
# Requirement: Display Employee Name & Job Role

emp_data = "John,john@apple.com,30,Hyderabad,Developer"
emp_name = emp_data[0]
print("Employee Name: ",emp_name)

emp_name = emp_data[0:4]
print("Employee Name: ",emp_name)

# Records we updated in future, name was corrected
emp_data = "Michael,john@apple.com,30,Hyderabad,Developer"

emp_name = emp_data[0:4]
print("Employee Name: ",emp_name)

# Using Above Approach we have hard coded logic, which is not good 
# split() method in Python is the primary tool for breaking a string into a list of substrings\
emp_data = "Michael,john@apple.com,30,Hyderabad,Developer"
data_splitted = emp_data.split()
print(data_splitted)

emp_data = "Michael john@apple.com 30 Hyderabad Developer"
data_splitted = emp_data.split()
print(data_splitted)

emp_data = "Michael,john@apple.com,30,Hyderabad,Developer"
emp_data = "john,john@apple.com,30,Hyderabad,Developer"
emp_data = "bignameeeeeeeeeeeeeeee,john@apple.com,30,Hyderabad,Developer"
emp_data = "john,john@apple.com,30,Hyderabad,Developer"
data_splitted = emp_data.split(",")
print(data_splitted)

print("Employee Name: ",data_splitted[0])
print("Employee Role: ",data_splitted[-1])

# Simulate Amazon Order Email / SMS / OTP Confirmation Template 
order_template = "Hello, Your Order with order_id has been shipped"
order_ids = "AMAZON-ID-1010029202,AMAZON-ID-8090029202,AMAZON-ID-9090029202,AMAZON-ID-7080029202"

# "Hello, Your Order with AMAZON-ID-1010029202 has been shipped"
order_ids_extracted = order_ids.split(",")
print(order_ids_extracted)
# print(dir(order_ids_extracted))
for order_id in order_ids_extracted:
    # replace() method is used to swap out a specific substring for a new one within a string
    # replace(old,new)
    send_email = order_template.replace("order_id",order_id)
    print(send_email)
    
