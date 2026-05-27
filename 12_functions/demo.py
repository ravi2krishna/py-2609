# Functional Programming 

# Without Functions 

# User One wants to calculate for below values
num1 = 10
num2 = 5

# Math Operations 
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 10)

# Another User wants to calculate for below values
num1 = 20
num2 = 5

# Math Operations 
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 10)

# Another User wants to calculate for below values
num1 = 200
num2 = 50

# Math Operations 
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 10)

# With Functions
def math_ops():
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)

# User One wants to calculate for below values
print("User 1")
num1 = 10
num2 = 5
math_ops()

print("User 2")
# Another User wants to calculate for below values
num1 = 20
num2 = 5
math_ops()

print("User 3")
# Another User wants to calculate for below values
num1 = 200
num2 = 50
math_ops()

print("=" * 20)

# math_ops(10,5) # TypeError: math_ops() takes 0 positional arguments but 2 were given
   

# Functions With Parameters 
def math_ops(num1, num2): # num1, num2 are Parameters
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)
    
# math_ops() # TypeError: math_ops() missing 2 required positional arguments: 'num1' and 'num2'
math_ops(10,5) # ("User 1")
math_ops(20,5) # ("User 2")
math_ops(200,50) # ("User 2")