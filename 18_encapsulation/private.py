# Private Access 

class A:
    def __init__(self,a):
        self.__a = a # Private i.e __

obj = A(10)

# print(obj.a) # AttributeError: 'A' object has no attribute 'a'

print(obj._A__a) # “You shouldn’t, but you can if you insist”

# Real World Use Case 
class CreditCard:
    def __init__(self,card_number,card_cvv):
        self.__card_number = card_number # Private
        self.__card_cvv = card_cvv # Private