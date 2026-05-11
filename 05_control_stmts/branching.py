# Branching Structures / Statements (Jump Statements)

for num in range(1,11,1):
    print(num)
    
print("============")

# break - helps you exit the loops  
for num in range(1,11,1):
    # stop the loop, when num is 5 
    if num == 5:
        break 
    print(num)

print("============")    

# continue - helps you skip the current iteration 
for num in range(1,11,1):
    # skip the 5th iteration
    if num == 5:
        continue 
    print(num)
    
# pass - acts as a placeholder, does nothing 
# Requirement - To Perform Some Operations in the Future 
# When Salary is above 25000, we want to do something 
# emp_salary = 15000

emp_salary = 15000
if emp_salary > 25000:
    pass # ___________
    
# Other Operations To Work On 
print("Working With Next Functionalities")

# After 6 Months 
# When Salary is above 25000, we want to do something 
# something is promoted to junior engineer 
emp_salary = 35000
if emp_salary > 25000:
    print("Trainee promoted to junior engineer")
    
# When working with OOP 
class Employee:
    pass 
    
class Manager:
    pass
    
class Developer: 
    pass