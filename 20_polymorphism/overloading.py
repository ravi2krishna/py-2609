# Method Overloading Traditional - Fails 

class MathOps:
    
    def add(self,a,b):
        return a + b 
    
    def add(self,a,b,c):
        return a + b + c
    
obj = MathOps()

# print(obj.add(1,2)) # TypeError: MathOps.add() missing 1 required positional argument: 'c'
print(obj.add(1,2,3))

print("=" * 50)    

class MathOps:
    
    def add(self,*args):
        return sum(args) 

obj = MathOps()

print(obj.add(1,2))
print(obj.add(1,2,3))
print(obj.add(1,2,3,4))
print(obj.add(1,2,3,4,5))