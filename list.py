#1st Task for list
# list=[ ] is considered as lists.

a=[]
sum=0

c=int(input("Enter the range value: "))
print("Enter the Values: ")

for i in range(c):
    b=int(input())
    a.append(b)
    # print(sum)
print("The sum is: ")
for i in a:
    sum=sum+i

print(sum)
avg=sum/c
print("The avg is: ",avg)