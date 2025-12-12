#1st task
# for i in range(1,21):
#     print("2 *",i,"=",2*i)

#2nd task:
# a=int(input("Enter value of a: "))
# b=int(input("Enter value of b: "))

# for i in range(a+1,b):
#     print("The In between Values are: ",i)

#3RD TASK
# a=int(input("Enter value of a: "))
# b=int(input("Enter value of b: "))
# count=0
# odd=0

# for i in range(a,b+1):
#         if(i%2==0):
#             print("The Evens are: ",i)
#             count=count+1
#         elif(i!=0):
#              print("The Odds are: ",i)
#              odd=odd+1

# print("Total even no: ",count)
# print("Total odd no: ",odd)

#4th Task
# count=0
# a=int(input("Enter range a: "))
# b=int(input("Enter range b: "))


# print("The NUmbers are: ")
# for i in range(a,b):
#     if(i%3==0 and i%5==0):
#         print(i)
#         count=count+1
# print("Total Numbers that ae divided by both 3 and 5 is:",count)
    
#5t Task

a=int(input("Enter the range value a:"))
b=int(input("Enter the range value b:"))
# count=0
# print("The natural numbers are: ")
# for i in range(a,b):
#     print(i)
#     count=count+i
# print("Sum of Natural Numbers are: ",count)

for i in range(a,b):
    print()
    for j in range(a,b):
        
        print("   ",i,"*",j,"=",i*j,end="")