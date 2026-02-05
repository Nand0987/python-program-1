# class Student :
#     s_name="nitish" #6byte
#     s_age=22 #4bytes
# f_student=Student() #object
# s_student=Student() #object
# t_student=Student() #object

# print(f_student.s_name)
# print(f_student.s_age)

# print(s_student.s_name)
# print(s_student.s_age)
# del s_student
# print(t_student.s_name)
# print(t_student.s_age)


# class Student :
#    def  __init__(self,s_name,s_age):
#     self.s_name=s_name
#     self.s_age=s_age

# f_student=Student("nitish",21)
# s_student=Student("suresh",22)
# t_student=Student("naresh",22)
# print(s_student.s_name)
# print(f_student.s_age)

class Student :
    def __init__(self,roll_no,name,marks): #constructor
        self.name=name
        self.marks=marks
        self.roll_no=roll_no
    def display_college(self): #TNRN
        print("kr mangalam university")
    def set_data(self,roll_no,name,marks): #TSRN
        self.roll_no=roll_no
        self.name=name
        self.marks=marks
    def get_marks(self): #TNRS
        return self.marks
    def calculate_grade(self,marks):
        
        
    

s1=Student(22,"rishav",23)
s1.display_college()

        
    







