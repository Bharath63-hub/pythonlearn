# class lap:

    
#     def __init__(self):
#         self.name=input("Select Brand: ")
        
#     def brand(self):
        
        
#         if(self.name=="HP"):
#             print("Enter Your Requirements:")
#             self.p=input("Processor:")
#             self.ram=input("RAM:")
#             self.st=input("Storage:")
#             self.price=int(input("Buget fixed:"))
#             self.order={"Processor":self.p,"RAM":self.ram,"Storage":self.st,"Budget Price":self.price}
#             def hp():
#                 print()
#                 print("Conguralations Your order for HP is placed.")
#                 print()
#                 print("Thanks for choosing",self.name)
#                 print()
#                 print("Your Specification are:")
#                 for key,value in self.order.items():
                    
#                     print(f"{key}:{value}")
#             hp()
            
#         elif(self.name=="Lenovo"):
#             print("Enter Your Requirements:")
#             self.p=input("Processor:")
#             self.ram=input("RAM:")
#             self.st=input("Storage:")
#             self.price=int(input("Buget fixed:"))
#             self.order={"Processor":self.p,"RAM":self.ram,"Storage":self.st,"Budget Price":self.price}
#             def Lenovo():
#                 print()
#                 print("Your order for Lenovo is placed.")
#                 print()
#                 print("Thanks for choosing",self.name)
#                 print()
#                 print("Your specifications are:")
#                 for key,value in self.order.items():
#                     print(f"{key}:{value}")
#             Lenovo()
#         elif(self.name=="Dell"):
#             print("Enter Your Requirements:")
#             self.p=input("Processor:")
#             self.ram=input("RAM:")
#             self.st=input("Storage:")
#             self.price=int(input("Buget fixed:"))
#             self.order={"Processor":self.p,"RAM":self.ram,"Storage":self.st,"Budget Price":self.price}
#             def Dell():
#                 print()
#                 print("Conguralations Your order for Dell is placed.")
#                 print()
#                 print("Thanks for choosing",self.name)
#                 print()
#                 print("Your specifications are:")
                
#                 for key,value in self.order.items():
#                     print(f"{key}:{value}")
#             Dell()     
#         else:
#             def nobrand():
#                 print()
#                 print("Sorry! selected brand isn't available.")
#             nobrand()





# brand=lap()
# brand.brand()

#classes and objeusing parameters
# class teach:

#     def __init__(self,name,reg):
#         self.name=name
#         self.reg=reg
#     def dis(self):
#         print("teacher name:",self.name)
#         print("teachers reg.no:",self.reg)
# t1=teach("Raj",1)
# t2=teach("Bharath",2)

# t1.dis()
# t2.dis()

#task2
class calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    print("Choose the operation:")
    print("1.Add 2.Sub 3.Mul 4.Div")
    def operation(self):
        choose=int(input("select operation: "))
        match choose:
            case 1:
                def add():
                    print("The Answer is:",self.a+self.b)
                add()
            case 2:
                def sub():
                    print("The Answer is:",self.a-self.b)
                sub()
            case 3:
                def mul():
                    print("The Answer is:",self.a*self.b)
                mul()
            case 4:
                def div():

                    print("The Answer is:",self.a/self.b)
                div()
            case _:
                print("Invalid Operation.")
val=calc(int(input("Enter a value:")),int(input("Enter b value:")))
val.operation()

                
