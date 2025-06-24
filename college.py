college=(
    ("swetha",("data structures","python","linux")),
    ("divya",("maths","science","physics")),
    ("aishwarya",("architect","maths","statistics"))
    )

while True:
       print("\n COLLEGE STUDENT DETAILS")
       print("1.View all students")
       print("2.View  a student's subjects")
       print("3.Exit")
       print("------------------------------")
       
       choice = input("enter your choice(1-3):")
       
       if choice == '1':
          print("Students:")
          for student in college:
            print(f" - {student[0]}")
            
       elif choice == '2':
           stud=input("enter a student name:")
           c=len(college)
           e=0
           for i in range(c):
               d=college[i][0]
               
               if stud==d:
                   print(f"given student subjects is:{college[i]}")   
                   print("---------------")
                   break
               else:
                   e+=1
                   
           if e==c :
               print("student not found")        
               
       elif choice =='3':
           print("exiting .....")
           break
       else:
           print("invalid choice")        