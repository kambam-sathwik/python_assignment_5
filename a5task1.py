
student_marks={'Alice':81,'Bob':82,'Steve':83,'Nancy':84}

s_name=input("Enter the student name:")

if s_name in student_marks:
    print(f"{s_name}'s marks:{student_marks[s_name]}")
else:
    print("Student Name Not Found")