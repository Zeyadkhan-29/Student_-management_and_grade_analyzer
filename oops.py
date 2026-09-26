class student:
    def __init__(self,name,subject):
        self.name=name  #self.name ->is me name same rheta hai kue ki ye name ki memorie hai 
        self.subject=subject

    def get_cgpa(self):
        return self.subject

stud1=student("zeayd","math")
stud2=student("aly","english")
stud3=student("waqas","math")
stud4=student("wassam","science")


print(f"{stud1.name} have subject {stud1.get_cgpa()}")

