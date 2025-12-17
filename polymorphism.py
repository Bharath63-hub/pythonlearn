# class ani():
#     def sound(self):
#         print("Animal makes a Sound.")

# class dog(ani):
#     def sound(self):
#         print("Dogs bark")
#     # pass

# class bird(ani):
#     def sound(self):
#         print("Brids sings")
#     # pass


# Dog=dog()
# Dog.sound()
# Bird=bird()
# Bird.sound()


#2nd task

# class shape():
#     def area(self):
#         return 0
# class rec(shape):
#     def area(self,l,b):
#         print("area of rectangle is:",l*b)

# area=rec()
# area.area(6,4)

#3rd task

# class person():
#     def __init__(self,name):
#         self.name=name
# class stu(person):
#     def __init__(self,name,grade):
#         super().__init__(name)
#         self.grade=grade
#     def dis(self):
#         #super().__init__(grade)
#         print("The",self.name,"and grade is",self.grade)
# student=stu("Raj","A")
# #per=person("Raj")
# student.dis()

#4th task

# class vehi():
#     def start(self):
#         print("Vehicle Started.")
# class car(vehi):
#     def start(self):
#         print("Car started.")
# mode=car()
# by=vehi()
# by.start()
# mode.start()

#5th task

class emp():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class manager(emp):
    def __init__(self,name,salary,dep):
        self.dep=dep
        super().__init__(name,salary)
    def depart(self):
        print("Name is",self.name,"income is",self.salary,"Department is",self.dep)
man=manager("Raj",25000,"computer")

man.depart()