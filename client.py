# Client Needs Math Package 

# from  mathpackage import msg 
# print(msg) # ImportError: cannot import name 'msg' from 'mathpackage' 

from  mathpackage import add
# print(msg) # NameError: name 'msg' is not defined
print(add.msg)
print("Sum Of Numbers: ",add.add_fun(100,200))