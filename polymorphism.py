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

class shape():
    def area(self):
        return 0
class rec(shape):
    def area(self,l,b):
        print("area of rectangle is:",l*b)

# a=shape()
# a.area()
area=rec()
area.area(6,4)
