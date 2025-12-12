#1st Task for list
# list=[ ] is considered as lists.

# a=[]
# sum=0

# c=int(input("Enter the range value: "))
# print("Enter the Values: ")

# for i in range(c):
#     b=int(input())
#     a.append(b)
#     # print(sum)
# print("The sum is: ")
# for i in a:
#     sum=sum+i

# print(sum)
# avg=sum/c
# print("The avg is: ",avg)




# i=int(input("Enter from range: "))
# c=int(input("enter range value: "))

# for i in range(1,6):
#     b=input()
#     a.append(b)
#     i=i+1
#     b=i
#print("values of a list",a,end="")


a=["raj","1","kumar","yukesh"]
b=int(input("Select index: "))
c=input("Enter value: ")

print()
def fun():
        
        print("inserting different value in given index position: ",b)
        a.insert(b,c)
        print(a)
        return list()
def list():
        print()
        print("index and values passed in the list.")
        a[b]=c
        print(a)
        return li1()

def li1():
        print()
        print("Removing an index: ",b)
        a.pop(b)
        print(a)
        

def li2():
        print()
        b=["Extended"]
        print("Extending or Merging  with different list....")
        a.extend(b)
        print(a)
        print()
        return fun()

li2()


# list(b,c)
# c="/media/raj/OS/shell-learn"
# def fun():
#     cd c
#     chmod 775 createfunc.sh
#     ./createfunc.sh    
# fun()