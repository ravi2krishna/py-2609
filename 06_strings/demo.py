# Strings 

# Single Line Strings
s1 = "hello" # Recommended
print(s1)
print(type(s1))

s2 = 'hello' # Recommended
print(s2)
print(type(s2))

s3 = '''hello''' # Not Recommended
print(s3)
print(type(s3))

s4 = """hello""" # Not Recommended
print(s4)
print(type(s4))

# Multi Line Strings
# SyntaxError: unterminated string literal (detected at line 21)
# define_python = 'Python is a high-level, general-purpose programming language. 
#         It emphasizes code readability, simplicity, and ease-of-writing 
#         with the use of significant indentation, "plain English" naming, 
#         an extensive ("batteries-included") standard library, and garbage collection.'
# print(define_python)

define_python = '''Python is a high-level, general-purpose programming language. 
        It emphasizes code readability, simplicity, and ease-of-writing 
        with the use of significant indentation, "plain English" naming, 
        an extensive ("batteries-included") standard library, and garbage collection.'''
print(define_python)

define_python = """Python is a high-level, general-purpose programming language. 
        It emphasizes code readability, simplicity, and ease-of-writing 
        with the use of significant indentation, "plain English" naming, 
        an extensive ("batteries-included") standard library, and garbage collection."""
print(define_python)

# When you use single quote in a string, enclose them in double quotes 
question = "how are you ?"
# answer = 'i'm fine' # SyntaxError: unterminated string literal (detected at line 42)
answer = "i'm fine"
print(answer)

# When you use double quote in a string, enclose them in single quotes 
question = "how are you ?"
# answer = "i"m fine" # SyntaxError: unterminated string literal (detected at line 42)
answer = 'i"m fine'
print(answer)

# Need both single quote and double quote in a string
question = "how are you ?"
# answer = 'i"m fine i'm fine' # SyntaxError: unterminated string literal (detected at line 54)
# answer = "i"m fine i'm fine" # SyntaxError: unterminated string literal (detected at line 55)
answer = ''' i"m fine i'm fine '''
answer = """ i"m fine i'm fine """
print(answer)

# Accessing Strings
text = "python"
print(text)

# Accessing Characters using index
# Positive Indexing
print(text[0])
print(text[1])

# Negative Indexing
print(text[-1])
print(text[-2])

# print(text[10]) # IndexError: string index out of range

# print all characters 
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

print("===========")

# print all characters 
text = "python is language"

for character in text:
    print(character)

print(dir(text))
print("===========")

text = 12345 # TypeError: 'int' object is not iterable
# for character in text:
#     print(character) 
print(dir(text))

print("===========")

text = "12345" # TypeError: 'int' object is not iterable
for character in text:
    print(character) 
    
print("Length Of String: ",len(text))
print("===========")

prices_products = [1000,1500,2000,2500,3000,3500,4000,4500,5000,100000]
print(dir(prices_products))
print("Count Of Products: ",len(prices_products))

print("===========")

# Slicing 
text = "python"
print(text)
# print(text[]) # Expected index or slice expression
print(text[:])
print(text[::])
print(text[0:3:1]) # pyt
print(text[0:3:]) # pyt
print(text[1:3:]) # yt
print(text[0:5:2]) # pto

        #     0   1 2  3  4  5
        #     p   y t  h  o  n
        #     -6 -5 -4 -3 -2 -1   

print(text[-4:-1:1]) # tho
print(text[-4:-1:-1]) # empty 
print(text[-4:-6:-1]) # ty

# String Concatenation
s1 = "good "
s2 = "morning"
print(s1 + s2)

# Formatted String Literals (f-strings)
age = 30 
# print("My age is "+age) # TypeError: can only concatenate str (not "int") to str
print(f"My age is {age}")

# String Repetition 
laugh = "Haha"
print(laugh)

hard_laugh = laugh * 20
print(hard_laugh)

# String Immutability 
greet = "hello"
print(greet)
# Requirement is Print Hello 
print(greet[0])
# greet[0] = 'H' # TypeError: 'str' object does not support item assignment
print(greet[0])

print("=" * 10)

# Example Of Mutable Datatype i.e List 
greet = ['h','i']
print(greet[0])
greet[0] = 'H'
print(greet[0])

print("=" * 10)

greet = "hello"
print(greet)
print(type(greet))
print(dir(greet))

# capitalize() - Return a copy of the string with its first character capitalized and the rest lowercased.
greet = "hello"
result = greet.capitalize()
print(greet)
print(result)