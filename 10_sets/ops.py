# Sets Methods / Operations

# add(): add element to set 
data = {10,20,30,40,50}
print(data)
data.add(60)
print(data)

# update(): add multiple elements to set 
data = {10,20,30,40,50}
print(data)
data.update([60,70,60,80,90])
print(data)

# pop(): Removes random element
data = {1,20,30,40,0}
print(data)
data.pop()
print(data)

# remove(): Remove element by value 
data = {10,20,30,40,50}
print(data)
data.remove(30)
# data.remove(300) # KeyError: 300
print(data)

# discard(): Remove element by value 
data = {10,20,30,40,50}
print(data)
data.discard(30)
data.discard(300)
print(data)

# clear(): Empties set 
data = {10,20,30,40,50}
print(data)
data.clear()
print(data)

# copy(): Creates a copy
data = {10,20,30,40,50}
print(data)
backup = data.copy()
print(backup)

# Special Methods Specific to sets only (math related ops)
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

# union(): combine sets 
print(s1.union(s2))
print(s1 | s2)

# intersection(): get common elements from sets 
print(s1.intersection(s2))
print(s1 & s2)
print(s1)
print(s2)

# intersection_update(): get common elements from sets, updates calling sets 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.intersection_update(s2))
print(s1)
print(s2)

# difference(): Removes Common elements from the set and gives unique elements 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1-s2)
print(s2-s1)
print(s1)
print(s2)


# difference_update(): Removes Common elements from the set and gives unique elements, updates calling sets  
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference_update(s2))
print(s1)
print(s2)

# symmetric_difference(): Removes Common elements from the set and takes combined elements from both sets
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
print(s1)
print(s2)

# symmetric_difference_update(): Removes Common elements from the set and takes combined elements from both sets, updates calling sets  
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference_update(s2))
print(s1)
print(s2)

# issubset(): Checks if given set is a subset of another set 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}

print(s1.issubset(s2))
print(s3.issubset(s1))

# issuperset(): Checks if given set is a superset of another set 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}
print(s3.issuperset(s1))
print(s1.issuperset(s3))

# isdisjoint(): Check if sets have no common elements 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

