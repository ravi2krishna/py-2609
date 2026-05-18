# List Methods / Operations 

# append(): Adds Elements To End Of List 
data = [10, 20, 30, 40, 50]
print(data)
data.append(60)
print(data)

# extend(): Adds Iterable To List 
data = [10, 20, 30, 40, 50]
print(data)
new_data = [60,70,80,90,100]
data.extend(new_data)
print(data)

# insert(): Add element on a specific position base on index
data = [10, 20, 40, 50]
print(data)
# data.append(30)
data.insert(2,30)
print(data)

# pop(): Removes an element by default last element 
# if index is provided, removes specific element
data = [10, 20, 30, 40, 50]
print(data)
data.pop()
print(data)

data = [10, 20, 30, 40, 50]
print(data)
data.pop(0)
print(data)

# remove(): Remove element based on value 
data = [10, 20, 30, 40, 50]
print(data)
data.remove(30)
print(data)

data = [10, 20, 30, 10, 40, 50, 10]
print(data)
data.remove(10)
print(data)

# Requirement: Remove all occurrences of 10
data = [10, 20, 30, 10, 40, 50, 10]
print(data)

while 10 in data:
    data.remove(10)
print(data)

# clear(): Remove all elements and empties list 
data = [10, 20, 30, 10, 40, 50, 10]
print(data)
data.clear()
print(data)

# index(): Used to get the index position of value
data = [10, 20, 30, 40, 50]
print(data)
data.index(30)
print(data.index(30))

# count(): Count the number of occurrences 
data = [10, 20, 30, 10, 40, 50, 10]
print(data)
data.count(10)
print(data.count(10))
print(len(data))

# reverse - Reveres the list 
data = [10, 20, 30, 40, 50]
print(data)
data.reverse()
print(data)

# sort(): sorts the list, default is ascending order 
data = [10, 20, 40, 30, 50]
print(data)
data.sort()
print(data)

data = [10, 20, 40, 30, 50]
print(data)
data.sort(reverse=True) # descending order 
print(data)

# copy(): Creates backup copy 
data = [10, 20, 40, 30, 50]
print(data)
backup_copy = data.copy()
print(backup_copy)

# PAN 
pan = ["ABCDE1234F","EFGHE1234F","XYZAC1234F"] # Original PAN ID's 
print(pan)
pan[0] = "LMNOP1234F"
print(pan)
