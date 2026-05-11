# Simulate Authentication Functionality Bank Logins / ATM Withdraws / Password Based Logins

correct_pin = 2345

attempts = 3 

print(correct_pin)
# print(len(correct_pin)) TypeError: object of type 'int' has no len()
# pin_str = str(correct_pin)
# print(len(pin_str)) # 4

while attempts > 0:
    print(f"You Have {attempts} Attempts Left")
    
    user_pin = int(input("Enter PIN: "))
    
    if (len(str(user_pin))) != 4:
        print("Transaction Failed")
        attempts -= 1
        continue
    
    if user_pin == correct_pin:
        print("Transaction Success")
        break 
    else:
        print("Transaction Failed")
        attempts -= 1

else:
    print("Maximum Attempts Reached, Try After 24 Hours ")
    