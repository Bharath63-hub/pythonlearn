#mark=int(input("Enter mark:"))
#avg=mark/2

#if(mark/2>=70):
 #   print("avg is ",avg,"passed")
#else:
 #   print("Average",avg,"is low Retry")


#a=int(input("Enter a value:"))
#if(a%5==0 and a%3==0):
 #   print("Divide by 3 and 5")
#else:
 #   print("Not divided by 3 and 5")
#if(a<=35):
    #print("poor student")
#elif(a>35 and a<=70):
 #   print("average student")
#else:
 #   print("good student")

print("Simple Calculator")
a=float(input("Enter a value:"))
c=input()
b=float(input("Enter b value:"))


if(c=="+"):
    print("Addition: ",a+b)
elif(c=="-"):
    print("subtracted value:",a-b)
elif(c=="*"):
    print("Multiplied value:",a*b)
elif(c=="/"):
    print("Division:",a/b)
elif(c=="%"):
    print("Reminder after division:",a%b)
else:
    print("invalid operation")
