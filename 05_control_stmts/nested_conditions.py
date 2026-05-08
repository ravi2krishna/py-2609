# Nested Conditionals 
# inner condition is only checked if the outer condition is true. 

if True:
    print("1")
if True:
    print("This is NOT Nested Condition")
   

if True: # Outer Condition 
    print("1")
    if True: # Inner Condition
        print("This is Nested Condition")
        if True: # Inner Condition
            print("This is Nested Condition")

if False: # Outer Condition 
    print("1")
    if True: # Inner Condition
        print("This is Nested Condition")
        
# Nested Conditional Use Case 
age = int(input("Enter Your Age: "))
if age >= 18:
    has_id = input("Do You Have ID (yes/no): ")
    if has_id == "yes":
        print("You Can Vote")
    else:
        print("You Cannot Vote Without ID Proof")
else:
    print("You Cannot Vote With Under Age")

# Real World Use Case 
# Net Banking Login -> User Authentication & -> OTP Authorization 
