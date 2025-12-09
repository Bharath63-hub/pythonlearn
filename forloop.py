#1st task
# for i in range(1,21):
#     print("2 *",i,"=",2*i)

#2nd task:
# a=int(input("Enter value of a: "))
# b=int(input("Enter value of b: "))

# for i in range(a+1,b):
#     print("The In between Values are: ",i)

#3RD TASK
a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
count=0
odd=0

for i in range(a,b+1):
        if(i%2==0):
            print("The Evens are: ",i)
            count=count+1
        elif(i!=0):
             print("The Odds are: ",i)
             odd=odd+1

print("Total even no: ",count)
print("Total odd no: ",odd)