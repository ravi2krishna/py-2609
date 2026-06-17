# OOP - Object Oriented Programming 

# Class - Blue Print 
class Student:
    
    # Student Has Something - Characteristics / Properties (VARIABLES)
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Student Does Something - Behaviors / Actions (METHODS)
    def student_studies():
        print("Student is studying python")
    

# To use this class, object is required
student_object = Student()
    
print("Student Name: ",student_object.student_name)
print("Student Email: ",student_object.student_email)

# student_object.student_studies() # TypeError: Student.student_studies() takes 0 positional arguments but 1 was given

print("=" * 50)

# Class - Blue Print 
class Student:
    
    # Student Has Something - Characteristics / Properties (VARIABLES)
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Student Does Something - Behaviors / Actions (METHODS)
    # self is object reference 
    def student_studies(self):
        print("Student is studying python")
    

# To use this class, object is required
student_object = Student()
    
print("Student Name: ",student_object.student_name)
print("Student Email: ",student_object.student_email)

student_object.student_studies()

print("=" * 50)

# Class - Blue Print 
class Student:
    
    # Student Has Something - Characteristics / Properties (VARIABLES)
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Student Does Something - Behaviors / Actions (METHODS)
    # self is object reference 
    def student_studies(self):
        print("Student is studying python")
        print("Student Name: ",student_object.student_name)
        print("Student Name: ",self.student_email) # Recommended 
    
# To use this class, object is required
student_object = Student()
student_object.student_studies()

print("=" * 50)

# Class - Blue Print 
class Student:
    
    # Student Has Something - Characteristics / Properties (VARIABLES)
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Student Does Something - Behaviors / Actions (METHODS)
    # self is object reference 
    def student_studies(self):
        print("Student is studying python")
        print("Student Name: ",self.student_name)
        print("Student Name: ",self.student_email) # Recommended 
    
# To use this class, object is required
student_object = Student()
student_object.student_studies()

print("=" * 50)

# Working with multiple objects 
class Student:
    
    # Student Has Something - Characteristics / Properties (VARIABLES)
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Student Does Something - Behaviors / Actions (METHODS)
    # self is object reference 
    def student_studies(self):
        print("Student is studying python")
        print("Student Name: ",self.student_name)
        print("Student Name: ",self.student_email) # Recommended 
    
# To use this class, object is required
student_ravi = Student()
student_ravi.student_studies()

student_john = Student()
student_john.student_studies()

student_mike = Student()
student_mike.student_studies()

print("=" * 50)


# Working with multiple objects using Constructors 
class Student:
    
    # Student Has Something - Characteristics / Properties (VARIABLES)
    # student_name = "Ravi"
    # student_email = "ravi2krishna@gmail.com"
    
    # Constructor
    def __init__(self,student_name,student_email):
        self.student_name = student_name
        self.student_email = student_email
        
    
    # Student Does Something - Behaviors / Actions (METHODS)
    # self is object reference 
    def student_studies(self):
        print("Student is studying python")
        print("Student Name: ",self.student_name)
        print("Student Name: ",self.student_email) # Recommended 
    
# To use this class, object is required
student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.student_studies()

student_john = Student("john","john@gmail.com")
student_john.student_studies()

student_mike = Student("mike","mike@gamil.com")
student_mike.student_studies()

print("=" * 50)


# Working with Instance Members
class Student:
    
    # Student Has Something - Characteristics / Properties (VARIABLES)
    # student_name = "Ravi"
    # student_email = "ravi2krishna@gmail.com"
    
    # Constructor
    def __init__(self,student_name,student_email):
        # Instance Variables self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Student Does Something - Behaviors / Actions (METHODS)
    # self is object reference 
    # Below is Instance Method
    def student_studies(self):
        print("Student is studying python")
        print("Student Name: ",self.student_name)
        print("Student Name: ",self.student_email) # Recommended 
    
# To use this class, object is required
student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.student_studies()

student_john = Student("john","john@gmail.com")
student_john.student_studies()

student_mike = Student("mike","mike@gamil.com")
student_mike.student_studies()

print("=" * 50)


# Working with Class Members
class Student:
    
    # Class Variables - Shared by all objects
    institute_name = "Digital Institute"
    
    # Constructor
    def __init__(self,student_name,student_email):
        # Instance Variables self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Student Does Something - Behaviors / Actions (METHODS)
    # self is object reference 
    # Below is Instance Method
    def student_studies(self):
        print("Student is studying python")
        print("Institute Is: ",Student.institute_name) # Recommended
        print("Institute Is: ",self.institute_name) # Not Recommended
        print("Student Name: ",self.student_name)
        print("Student Email: ",self.student_email) # Recommended 
        
    # Class Method 
    @classmethod
    def change_institute_name(cls,new_name):
        cls.institute_name = new_name
        # print("Student Name: ",self.student_name) # Accessing instance data inside a class method gives error 
    
    
# To use this class, object is required
student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.student_studies()

student_john = Student("john","john@gmail.com")
student_john.student_studies()

student_mike = Student("mike","mike@gamil.com")
student_mike.student_studies()

print("=" * 50)

# Class Method Call
Student.change_institute_name("New Institute")

student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.student_studies()

student_john = Student("john","john@gmail.com")
student_john.student_studies()

student_mike = Student("mike","mike@gamil.com")
student_mike.student_studies()

print("=" * 50)

# Working with Static Method 
class Student:
    
    # Class Variables - Shared by all objects
    institute_name = "Digital Institute"
    
    # Constructor
    def __init__(self,student_name,student_email):
        # Instance Variables self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Student Does Something - Behaviors / Actions (METHODS)
    # self is object reference 
    # Below is Instance Method
    def student_studies(self):
        print("Student is studying python")
        print("Institute Is: ",Student.institute_name) # Recommended
        print("Institute Is: ",self.institute_name) # Not Recommended
        print("Student Name: ",self.student_name)
        print("Student Email: ",self.student_email) # Recommended 
        
    # Class Method 
    @classmethod
    def change_institute_name(cls,new_name):
        cls.institute_name = new_name
        # print("Student Name: ",self.student_name) # Accessing instance data inside a class method gives error 
    
    # Static Method
    @staticmethod
    def something():
        print ("I Do Something that is not associated with Classes & Objects")
        
    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email
    
    
# To use this class, object is required
student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.student_studies()

student_john = Student("john","john@gmail.com")
student_john.student_studies()

student_mike = Student("mike","mike@gamil.com")
student_mike.student_studies()

print("=" * 50)

# Class Method Call
Student.change_institute_name("New Institute")

student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.student_studies()

student_john = Student("john","john@gmail.com")
student_john.student_studies()

student_mike = Student("mike","mike@gamil.com")
student_mike.student_studies()

# Call Static Method
Student.something()

print(Student.validate_email("ravi.com"))
print(Student.validate_email("ravi@com"))
print(Student.validate_email("ravi@gmail.com"))

print("=" * 50)