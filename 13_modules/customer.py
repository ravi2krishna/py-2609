# Like we used math module and got sqrt & pi 

# Now a new customer / user wants to use our mathprofile module 

# from module import specific_functionality

from mathprofile import maintainer

print("Maintainer is: "+maintainer)
# print("Institute is: "+institute) # NameError: name 'institute' is not defined

print("=" * 50)

from mathprofile import maintainer,institute,add 
print("Maintainer is: "+maintainer)
print("Institute is: "+institute)
print("Adding Numbers: ",add(10,20))
# print("Profile: ",profile()) # NameError: name 'profile' is not defined. Did you forget to import 'profile'?

print("=" * 50)

# import everything
import mathprofile 
print("Maintainer is: "+mathprofile.maintainer)
print("Institute is: "+mathprofile.institute)
print("Adding Numbers: ",mathprofile.add(10,20))
print("Profile: ",mathprofile.profile())
print("Multiplying Numbers: ",mathprofile.mul(10,20))



