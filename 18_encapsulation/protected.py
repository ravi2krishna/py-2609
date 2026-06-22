# Private Access With Sub Classes

class A:
    def __init__(self,a):
        self._a = a # Protected i.e _

obj = A(10)

# print(obj.a) # AttributeError: 'A' object has no attribute 'a'

class B(A):
    def showA(self):
        a = A(10)
        print(a._a) 
        
obj = B(20)
obj.showA()