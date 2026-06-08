# File & Directory Management Using Python

# Syntax - 1
# file = open("file_path","mode")
# file = open("file.txt","r") # FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'
# print(file)

file_data = open("14_file_manage/file.txt","r") 
print(file_data)

print(file_data.closed) # False --> Still Open
file_data.close() # Flush and close the IO object
print(file_data.closed) # True --> Now Closed

# Syntax - 2 (Recommended)
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data)
print(file_data.closed) # True --> File implicitly closed

# Reading Data From File
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.read())
    
# Reading Data From File with Character Wise 
with open("14_file_manage/file.txt","r") as file_data:
    # print(file_data.read())
    for character in file_data.read():
        print(character)
        
# Reading Data From File with Word Wise 
with open("14_file_manage/file.txt","r") as file_data:
    for word in file_data.read().split():
        print(word)
        
# Reading Data From File with Line Wise 
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.readline())

# Reading Data From File with Line Wise 
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.readlines())
    
# Reading Data From File with Multiple Lines 
with open("14_file_manage/file.txt","r") as file_data:
    for line in file_data.readlines():
        print(line.strip())
        

# Earlier we manually created file and manually written data to file 

# Now Use Python To Create File and Write Data
with open("14_file_manage/write.txt","w") as file_data: 
    file_data.write("Hello From Python")
    
# Now Use Python To Update Data In File
with open("14_file_manage/write.txt","w") as file_data: 
    file_data.write("Hello From Ravi ")
    
# Now Use Python To Append Data In File
with open("14_file_manage/write.txt","a") as file_data: 
    file_data.write("Hello From Python")
    
# Folder / Directory Management 
# directory_name = "14_file_manage/students_data"
# os.mkdir(directory_name) # NameError: name 'os' is not defined. Did you forget to import 'os'?

# Folder / Directory Management 
import os
directory_name = "14_file_manage/students_data"
# os.mkdir(directory_name) 
# os.rmdir(directory_name)

# Folder / Directory Management 
import os
directory_name = "14_file_manage/students_data"

if not os.path.exists(directory_name):
    os.mkdir(directory_name)
os.rmdir(directory_name)