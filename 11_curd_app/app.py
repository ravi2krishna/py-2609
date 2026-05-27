# Student Management System

# Menu Based System -> In Future if you learn full stack, replace menus with UI Elements like Buttons 

# System Setup -> READ Only (Tuple)
SYSTEM_INFO = ("Digital Tech","Student Management System","v1")

# Admin Info -> READ Only (Tuple)
ADMIN_INFO = ("9999999999","admin@digital.com")

# Display System Info 
print("=" * 50)
print(f"        Welcome To {SYSTEM_INFO[0]}")
print(f"        Software {SYSTEM_INFO[1]} - {SYSTEM_INFO[2]}")
print("=" * 50)

# Core Functionalities (CRUD)
# Add Student -> ID, Name, Scores, Skills
# Represent Above Student Details in Dictionary 

students = {}
# students = {
#     "101": {
#         "name": "Ravi",
#         "scores": [90,80,90,90],
#         "skills": {"python","ai","devops"}
#     },
#     "102": {
#         "name": "Krishna",
#         "scores": [70,80,80,90],
#         "skills": {"java","sql","html"}
#     },
# }

# Build Menu Based System for different (CRUD) operations 
while True:
    print("Choose An Option: ")
    print("1 - Create student")
    print("2 - Update student")
    print("3 - Delete student")
    print("4 - Read students")
    print("5 - Exit Application")
    
    choice = input("Enter Your Choice (1-5): ")
    
    if choice == "1":
        # Create / Add Student 
        print("=" * 30)
        print("     Adding Student")
        print("=" * 30)
        
        student_id = input("Enter ID: ")
        if student_id in students:
            print("OOPS! Student ID Already Exists")
        else:
            name = input("Enter Name: ").title()
            scores = []
            while True:
                score_input = input("Enter Score or Type done: ")
                if score_input == "done":
                    break 
                if score_input.isdigit():
                    score_input = int(score_input)
                    if 0 <= score_input <= 100:
                        scores.append(score_input)
                    else:
                        print("Invalid Score, Score should be (0-100)")
                else:
                    print("Invalid Score, Only Digits Allowed")
                    

            skills = set()
            while True:
                skill_input = input("Enter Skill or Type done: ")
                if skill_input == "done":
                    break
                else:
                    skills.add(skill_input) 
                    
            print(students) # Before Adding 
            print("=========== Student Added ===========")
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            print(students) # After Adding i.e for confirmation
            
            
        
    elif choice == "2":
        # Update Student 
        print("=" * 30)
        print("     Updating Student")
        print("=" * 30)
        
        student_id = input("Enter ID: ")
        if student_id in students:
            new_name = input("Enter Name: ").title()
            students[student_id]['name'] = new_name
            print("=" * 30)
            print("Student Updated")
            print("=" * 30)
        else:
            print("=" * 50)
            print("OOPS! Student ID Doesn't Exists")
            print("=" * 50)
        print(students) # After Updating i.e for confirmation
        
    elif choice == "3":
        # Delete Student 
        print("=" * 30)
        print("     Deleting Student")
        print("=" * 30)
        
        student_id = input("Enter ID: ")
        if student_id in students:
            students.pop(student_id)
            print("=" * 30)
            print("Student Deleted")
            print("=" * 30)
        else:
            print("=" * 50)
            print("OOPS! Student ID Doesn't Exists")
            print("=" * 50)
        print(students) # After Deleting i.e for confirmation
        
    elif choice == "4":
        # Read Students 
        print("=" * 30)
        print("     Reading Student")
        print("=" * 30)
        
        student_id = input("Enter ID: ")
        
        if student_id in students:
            
                # Fetch specific student data
                data = students[student_id]
        
                # {'101': {'name': 'Ravi', 'scores': [90], 'skills': {'python'}}}
                # for sid,data in students.items():
                #     # sid = 101
                #     # data = {'name': 'Ravi', 'scores': [90], 'skills': {'python'}}
                
                # id is already fetched i.e sid 
                # fetch name, scores, skills etc 
                name = data['name']
                scores = data['scores'] # All Scores
                skills = data['skills'] # All Skills 
                
                # Average Score 
                total_score = 0 # 90 + 80
                count_scores = 0
                
                for score in scores:
                    total_score += score
                    count_scores += 1
                
                avg_score = total_score / count_scores
                
                # Highest Score
                high_score = scores[0] # 90
                
                for score in scores:
                    if score > high_score:
                        high_score = score
                        
                # Lowest Score
                low_score = scores[0] # 90
                
                for score in scores:
                    if score < low_score:
                        low_score = score
                
                
                # Skills Count 
                skill_count = 0
                for skill in skills:
                    skill_count += 1
                
                # Displaying Student Information
                print("=" * 30)
                print("     Student Information")
                print("=" * 30)
                print(f"ID: {student_id}")
                print(f"Name: {name}")
                print(f"All Scores: {scores}")
                print(f"Average Score: {avg_score}")
                print(f"Highest Score: {high_score}")
                print(f"Lowest Score: {low_score}")
                print(f"All Skills: {skills}")
                print(f"Skills Count: {skill_count}")
                print("=" * 30)
        
        else:
            print("=" * 50)
            print("OOPS! Student ID Doesn't Exist")
            print("=" * 50)
            
        
    elif choice == "5":
        # Exit Application
        print("=" * 50)
        print("     Exiting Application")
        print("=" * 50)
        print(f"        Admin Contact Number {ADMIN_INFO[0]}")
        print(f"        Admin Email ID  {ADMIN_INFO[1]}")
        break
        
    else:
        # Invalid Choice
        print("=" * 50)
        print("     Invalid Option, Only Use (1-5)")
        print("=" * 50)
        
    
    
    
