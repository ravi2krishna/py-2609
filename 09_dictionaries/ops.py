# Dictionary Methods / Operations

data = {"a":"apple","b":"banana"}
print(type(data))

# update(): adds / updates item in dictionary 
print(data)
data.update({"c":"cherry"}) # if key is not present, then add the item 
print(data)

data.update({"a":"apricot"}) # # if key is not present, then update the item 
print(data)

# pop(): removes an item by key 
data = {"a":"apple","b":"banana"}
print(data)
data.pop("a")
print(data)

# popitem(): removes last item
data = {"a":"apple","b":"banana"}
print(data)
data.popitem()
print(data)

# clear(): Empties the dictionary
data = {"a":"apple","b":"banana"}
print(data)
data.clear()
print(data)


# get(): used to get value for key 
data = {"a":"apple","b":"banana"}
print(data)
print(data.get("a"))
print(data["a"])
# print(data["c"]) # KeyError: 'c'
print(data.get("c")) # None -> No error when key is not present

# keys(): Used to get keys 
data = {"a":"apple","b":"banana"}
print(data)
data.keys()
print(data.keys())
for key in data.keys():
    print(key)
    
# values(): Used to get values
data = {"a":"apple","b":"banana"}
print(data)
data.values()     
print(data.values())
for value in data.values():
    print(value)

# items(): Used to get both keys and values
data = {"a":"apple","b":"banana"}
print(data)
data.items()
print(data.items())
for item in data.items():
    print(item)
    

# setdefault(): returns a value of key, if the key is already present
# if key doesn't exist, then adds the item and returns the value
data = {"a":"apple","b":"banana"}
print(data)
data.setdefault("b","blueberry")
print(data.setdefault("b","blueberry"))

data = {"a":"apple","b":"banana"}
print(data)
print(data.setdefault("c","cherry"))
print(data)

# copy(): Creates a copy
data = {"a":"apple","b":"banana"}
print(data)
backup = data.copy()
print(backup)