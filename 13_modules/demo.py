# Inbuilt Modules 

# 1st Syntax 
# print(math.sqrt(25)) # NameError: name 'math' is not defined. Did you forget to import 'math'?
import math
print(math.sqrt(25))
print(math.pi)

print("=" * 20)

# 2nd Syntax 
# from module import specific_functionality
from math import sqrt
print(sqrt(25))
# print(pi) # NameError: name 'pi' is not defined

print("=" * 20)
from math import sqrt,pi 
print(sqrt(25))
print(pi)

# Python Inbuilt Modules - https://docs.python.org/3/py-modindex.html

