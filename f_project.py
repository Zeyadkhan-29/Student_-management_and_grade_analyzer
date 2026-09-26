student_info = [
    {
        "name": "zeyad",
        "age": 19,
        "regNo": 10,
        "class": "AIML",
        "section": "A",
        "year": "Second",
        "marks": {
            "python": 90,
            "math": 85,
            "physics": 95,
            "english": 87
        }
    },
    {
        "name": "rahasya",
        "age": 20,
        "regNo": 13,
        "class": "AIML",
        "section": "A",
        "year": "second",
        "marks": {
            "python": 90,
            "math": 66,
            "physics": 79,
            "english": 87
        }
    },
    {
        "name": "sachin",
        "age": 19,
        "regNo": 12,
        "class": "AIML",
        "section": "A",
        "year": "Second",
        "marks": {
            "python": 89,
            "math": 69,
            "physics": 70,
            "english": 95
        }
    },
    {
        "name": "pavin",
        "age": 19,
        "regNo": 11,
        "class": "AIML",
        "section": "A",
        "year": "second",
        "marks": {
            "python": 84,
            "math": 70,
            "physics": 98,
            "english": 75
        }
    }
]
print("===== Student Management System =====")
print("1. Add Student")
print("2. Remove Student")
print("3. Update Student")
print("4. Display Students")
print("5. Search Student")
print("6. Grade Analysis")
print("7. Exit")


while True:
    user_choice=int(input("enter your choice = "))
    if(user_choice==1):
        print("Add Student")
        student_info.append({"name": input("Name: "), "age": int(input("Age: ")), "regNo": int(input("Reg No: ")), "class": input("Class: "), "section": input("Section: "), "year": input("Year: "), "marks": {}})


    elif(user_choice==2):
        print("Remove Student")
        reg_no=int(input("enter the reg number = "))
        found=False
        for student in student_info:
            if(student["regNo"]==reg_no):
                student_info.remove(student)
            found=True
            break
        if found==False:
            print(f"{reg_no} not exist")


    elif user_choice == 3:
        print("Update Student")
        reg_no = int(input("Enter the current reg number: "))
        found = False
        for student in student_info:
            if student["regNo"] == reg_no:
                print("Student found")
                student["name"] = input("Enter new name: ")
                student["age"] = int(input("Enter new age: "))
                student["regNo"] = int(input("Enter new reg number: "))
                student["section"] = input("Enter new section: ")
                student["class"] = input("Enter new class: ")
                student["year"] = input("Enter new year: ")
                student["marks"]["python"] = int(input("Enter Python mark: "))
                student["marks"]["math"] = int(input("Enter Math mark: "))
                student["marks"]["physics"] = int(input("Enter Physics mark: "))
                student["marks"]["english"] = int(input("Enter English mark: "))
                found = True
                print("Student updated successfully")
                break
        if not found:
            print("No student exists with this regNo")

            
    elif user_choice == 4:
        print("===== Display Students =====")
        for student in student_info:
            print("\n===== Student Details =====")
            for key, value in student.items():
                if key != "marks":
                    print(f"{key} : {value}")
            print("----- Marks -----")
            for subject, mark in student["marks"].items():
                print(f"{subject} : {mark}")
            print("---------------------------")



    elif(user_choice==5):
        print("Search Student")
        reg_no=int(input("enter reg no = "))
        found=False
        for student in student_info:
            if(student["regNo"]==reg_no):
                print(student)
            found=True
            break
        if(found==False):
            print("student not found")


    elif(user_choice==6):
        print("Grade Analysis")
        for student in student_info:
            total=0
            for mark in student["marks"].values():
                total+=mark
            avg=total/len(student["marks"])
            if(90<avg<=100):
                grade = "A+"
            elif(80<avg<=90):
                grade = "A"
            elif(70<avg<=80):
                grade = "B"
            elif(60<avg<=70):
                grade = "C"
            elif(50<avg<=60):
                grade = "D"
            else:
                grade = "F"

            if avg>=50:
                result = "PASS"
            else:
                result = "FAIL"

            print(f"{student["name"]} -> total marks = {total} -> avg = {avg} -> final result = {result} -> grade = {grade}")

            highest=0
            lowest=float("inf")
            highest_student=""
            lowest_student=""
            for student in student_info:
                total=0
                for mark in student["marks"].values():
                    total+=mark

                if(highest<total):
                    highest=total
                    highest_student=student["name"]
                if(lowest>total):
                    lowest=total
                    lowest_student=student["name"]
        print("===== Comparision who's marks is highest and lowest in the class =====")
        print(f"{highest_student} -> highest = {highest}")
        print(f"{lowest_student} -> lowest = {lowest}")

        class_total=0
        total_student=0
        for studnet in student_info:
            for mark in student["marks"].values():
                class_total+=mark
            total_student+=1
        avg=class_total/total_student
        print("===== Class total and avg =====")
        print(f"class total = {class_total} -> avg = {avg}")

        passed=0
        failed=0
        for student in student_info:
            total=0
            for mark in student["marks"].values():
                total+=mark
            avg=total/len(student["marks"])
            if(avg>=50):
                passed+=1
            else:
                failed+=1
        print("===== Number of Passed and Failed Student =====")
        print(f"total pass student = {passed}")
        print(f"total fail student = {failed}")

        print("===== Avg of individual subjects =====")
        for subject in student_info[0]["marks"].keys():
            total=0
            for student in student_info:
                total+=student["marks"][subject]
            avg=total/len(student_info)
            print(f"{subject} -> avg = {avg}")

        print("===== Highest & Lowest Marks in Each Subject =====")
        for subject in student_info[0]["marks"].keys():
            highest=0
            highest_student=""
            lowest=float("inf")
            lowest_student=""
            for student in student_info:
                mark=student["marks"][subject]
                if(highest<mark):
                    highest=mark
                    highest_student=student["name"]
                if(lowest>mark):
                    lowest=mark
                    lowest_student=studnet["name"]
            print(f"{highest_student}-> highest mark = {highest} -> subject ->{subject}")
            print(f"{lowest_student}-> lowest mark = {lowest} -> subject ->{subject}")

    elif(user_choice==7):
        exit()
    else:
        print("not a correct choice")