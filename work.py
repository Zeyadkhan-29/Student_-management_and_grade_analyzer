student1_info = {
    "name":"zeyad",
    "age":19,
    "regNo":10,
    "class":"AIML",
    "section":"A",
    "year": "Second",
}

student2_info = {
    "name":"pavin",
    "age":19,
    "regNo":11,
    "class":"AIML",
    "section":"A",
    "year": "Second",
}

student3_info = {
    "name":"sachin",
    "age":19,
    "regNo":12,
    "class":"AIML",
    "section":"A",
    "year": "Second",
}
#print(student1_info)
# print(student2_info)
# print(student3_info)

# student1_info["age"]=20
# student1_info["section"]="B"
# student1_info.update({"college":"SRM"})
# student1_info.pop("year")
# print(student1_info.get("name"))
# print(student1_info.get("age"))
# print(student1_info.get("regNo"))
# print(student1_info.get("class"))
# print(student1_info.get("section"))
# print(student1_info.get("year"))
# print(student1_info)


student_info=[{
    "name":"zeyad",
    "age":19,
    "regNo":10,
    "class":"AIML",
    "section":"A",
    "year": "Second",
},{
    "name":"pavin",
    "age":19,
    "regNo":11,
    "class":"AIML",
    "section":"A",
    "year": "Second",
},{
    "name":"sachin",
    "age":19,
    "regNo":12,
    "class":"AIML",
    "section":"A",
    "year": "Second",
}]
student_info.pop(1)
student_info.append({"name": "rahul","age":20,"regNo":13,"class":"AIML","section":"A","year":"second"})
student_info.append({"name": "pavin","age":19,"regNo":11,"class":"AIML","section":"A","year":"second"})
student_info[0]["marks"]={
    "python":90,
    "math":90,
    "physics":88,
    "english":85
}
student_info[1]["marks"]={
    "python":90,
    "math":66,
    "physics":79,
    "english":87
}
student_info[2]["marks"]={
    "python":89,
    "math":69,
    "physics":70,
    "english":95
}
student_info[3]["marks"]={
    "python":84,
    "math":70,
    "physics":98,
    "english":75
}


# regNo=int(input("enter the reg number = "))
# found = False
# for student in student_info:
#     if(student["regNo"]==regNo):
#         print(f"{regNo} is duplicate")

#         found = True
#         break
# if found==False:
#     print(f"{regNo} not a dublicate regno")




# mark=int(input("enter the marks = "))
# if(mark<0 or mark>100):
#     print("invalid marks")
# else:
#     print(f"valid mark is  = {mark}")


# if(student_info==[]):
#     print("no student available")


# print("===== Student Details =====")
# for key,value in student_info[0].items():
#     print(f"{key} : {value}")
# print("---------------------------")


# regNo=int(input("enter the reg number = "))

# found = False

# for student in student_info:
#     if(student["regNo"]==regNo):
#         print(f"{regNo} student found name -> {student["name"]}")
#         found=True
#         break

# if not found:
#     print("student not found")


# print("==== Student Management System =====")
# print("1. Add Student")
# print("2. Remove Student")
# print("3. Update Student")
# print("4. Display Students")
# print("5. Search Student")
# print("6. Grade Analysis")
# print("7. Exit")

# while True:
#     choice=int(input("enter the variable choice = "))
#     if(choice==1):
#         print("-> Add Student")
#     elif(choice==2):
#         print("-> Remove Student")
#     elif(choice==3):
#         print("-> Update Student")
#     elif(choice==4):
#         print("-> Display Student")
#     elif(choice==5):
#         print("-> Search Student")
#     elif(choice==6):
#         print("-> Grade Analysis")
#     elif(choice==7):
#         exit()
#     else:
#         print("incorrect choise")
#     print(f"you choose = {choice}")



# for subject in student_info[0]["marks"].keys():
#     lowest=float("inf")
#     lowest_student=""
#     for student in student_info:
#         sub_marks= student["marks"][subject]
#         if(sub_marks<lowest):
#             lowest=sub_marks
#             lowest_student=student["name"]

#     print(f"{subject}->lowest got {lowest_student}->{lowest}")


# for subject in student_info[0]["marks"].keys():
#     highest=0
#     highest_student=""
#     for student in student_info:
#         sub_marsk=student["marks"][subject]

#         if(highest<sub_marsk):
#             highest=sub_marsk
#             highest_student=student["name"]

#     print(f"{subject}->highest got {highest_student} ->{highest}")


# passed=0
# failed=0
# for student in student_info:
#     total=0
#     for marks in student["marks"].values():
#         total+=marks

#     if(total>=150):
#         passed+=1
#     else:
#         failed+=1

# print(f"passed = {passed}")
# print(f"failed = {failed}")



# highest=0
# lowest=float("inf")

# highest_student=""
# lowest_student=""

# for student in student_info:
#     total=0
#     for mark in student["marks"].values():
#         total+=mark
#     if(highest<total):
#         highest=total
#         highest_student=student["name"]

#     if(total<lowest):
#         lowest=total
#         lowest_student=student["name"]

# print(f"{highest_student} -> got highest marks = {highest}")
# print(f"{lowest_student} -> got lowest marks = {lowest}")



# class_total=0
# total_student=0
# for student in student_info:
#     for mark in student["marks"].values():
#         class_total+=mark
#     total_student+=1

# avg = class_total/total_student
# print(f"the avg is = {avg}")
# print(f"total class marks is = {class_total}")
# print(f"total class student in = {total_student}")
    




# for subject in student_info[0]["marks"].keys():

#     highest=0
#     highest_student=""

#     for student in student_info:

#         marks=student["marks"][subject]

#         if(highest<marks):
#             highest=marks
#             highest_student=student["name"]
#     print(subject,"-> highest = ",highest,"->",highest_student)

# for subject in student_info[0]["marks"].keys():

#     lowest = float("inf")
#     lowest_student=""

#     for student in student_info:
#         mark=student["marks"][subject]

#         if(lowest>mark):
#             lowest=mark
#             lowest_student=student["name"]

#     print(subject,"-> lowest = ",lowest,"->",lowest_student)












# for subject in student_info[0]["marks"].keys():
#     total=0
#     student_num=0

#     for student in student_info:
#         total+=student["marks"][subject]
#         student_num+=1

#     avg=total/student_num
#     print(subject,"-> avg is = ",avg)
    

    







# classtotal=0
# students_num=0
# for student in student_info:
#     total=0
#     for mark in student["marks"].values():
#         total+=mark
#     students_num+=1
#     classtotal+=total
# class_avg=classtotal/students_num
# print(students_num)
# print(classtotal)
# print(class_avg)


# for student in student_info:
#     total=0
#     subject=0
#     for marks in student["marks"].values():
#         total+=marks
#         subject+=1
#     avg=total/subject
#     if (90<=avg<=100):
#         grade = "A+"
#     elif (80<=avg<90):
#         grade = "A"
#     elif (70<=avg<80):
#         grade = "B"
#     elif (60<=avg<70):
#         grade = "C"
#     elif (50<=avg<60):
#         grade = "D"
#     else:
#         grade = "F"


#     if(avg>=50):
#         result = "PASS"
#     else:
#         result = "FAIL"
#     print(student["name"],"->",avg,"->",grade,"->",result)



# highest=0
# lowest=float("inf")

# highest_student=""
# lowest_student=""

# for student in student_info:
#     total=0
#     for mark in student["marks"].values():
#         total+=mark

#     if(total>highest):
#         highest=total
#         highest_student=student["name"]

#     if(total<lowest):
#         lowest=total
#         lowest_student=student["name"]

# print(highest_student,"->highest is = ",highest)
# print(lowest_student,"->lowest is = ",lowest)

    

















# for student in student_info:
#     total = 0
#     for marks in student["marks"].values():
#         total+=marks
#     print(student["name"],"-> total marks is = ",total)






#print(student_info[0]["marks"].values())
# zeyads_total= 0
# for mark in student_info[0]["marks"].values():
#     zeyads_total+=mark
# print(f"total marks of zeyad is = {zeyads_total}")


# pavins_total=0
# for mark in student_info[1]["marks"].values():
#     pavins_total+=mark
# print(f"total marks of pavin is = {pavins_total}")


# sachins_total=0
# for mark in student_info[2]["marks"].values():
#     sachins_total+=mark
# print(f"total marks of sachin is = {sachins_total}")


# rahuls_total=0
# for mark in student_info[3]["marks"].values():
#     rahuls_total+=mark
# print(f"total marks of rahul is = {rahuls_total}")










# enter_reg=int(input("enter the reg number = "))
# found=False
# for i in student_info:
#     if i["regNo"]==enter_reg:
#         print("student found")

#         _name=input("enter the name = ")
#         i["name"]=_name
#         print("updated name")
#         _age=int(input("enter the age = "))
#         i["age"]=_age
#         print("updated age")
#         _section=input("enter the section = ")
#         i["section"]=_section
#         print("section updated")
#         _class=input("enter the class = ")
#         i["class"]=_class
#         print("class updated")
#         _year=input("enter the year = ")
#         i["year"]=_year
#         print("year updated")

#         for j in i:
#             print(j,":",i[j])

#         found=True
#         break

# if found==False:
#     print("no student exist with this reg number")




# enter_reg=int(input("enter the reg number = "))

# found = False
# for i in range(len(student_info)):
#     if(student_info[i]["regNo"]==enter_reg):
#         student_info.pop(i)
#         print("the student is passed out from this college")

#         found=True
#         break
# if (found==False):
#     print("no student exist with this reg number")






        

    
