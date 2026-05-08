# Looping Structures / Statements (Iteration Statements)

# while loop

# while True: # this forms an infinite loop 
#     print("Repeat...........")
# To terminate above use control + c 

while False:
    print("Repeat...........")
    
# Counters 
count = 1
while count <= 5:
    print("Count is: ",count)
    count += 1
    
# Use while loop when we don't know number of Iterations/Repetitions in advance

# You Found a Lost Phone, Trying To Break Password 
# Tell me at which attempt, the phone will be unlocked ?

actual_pin = "2345"
user_given_pin = ""

while user_given_pin != actual_pin:
    user_given_pin = input("Enter PIN: ")
print("Phone Unlocked")

# For Loop 
prices_products = [1000,1500,2000,2500,100000]

# Some Offer is running -> Provide a discount of 250 on each product 
# In lists we have index, which starts from zero and keeps going on 
print(prices_products)
print(prices_products[0])
print(prices_products[1])
print(prices_products[2])
print(prices_products[3])
print(prices_products[4])
# .
# .
# print(prices_products[499])
print("Prices After Discount")
print(prices_products[0] - 250)
print(prices_products[1] - 250)
print(prices_products[2] - 250)
print(prices_products[3] - 250)
print(prices_products[4] - 250)

# Say we have 10000 Products 
# print(prices_products[9999] - 250)

# for loop -> 10000 products 
prices_products = [1000,1500,2000,2500,3000,3500,4000,4500,5000,100000]
print("Prices Before Discount")
for price in prices_products:
    print(price)
    
print("Prices After Discount")
for price in prices_products:
    print(price - 250)