# Tuple Methods / Operations

# index(): Used to get the index position of value
data = (10, 20, 30, 40, 50)
print(data)
data.index(30)
print(data.index(30))

# count(): Count the number of occurrences 
data = (10, 20, 30, 10, 40, 50, 10)
print(data)
data.count(10)
print(data.count(10))

# PAN 
pan = ("ABCDE1234F","EFGHE1234F","XYZAC1234F") # Original PAN ID's 
print(pan)
# pan[0] = "LMNOP1234F" # TypeError: 'tuple' object does not support item assignment
print(pan)