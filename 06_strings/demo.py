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