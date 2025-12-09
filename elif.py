# mark=int(input("Marks Acquired in 12th grade:"))
# #name=input()
# #add=input()
# #ph=int(input())

# if(mark>70):
   
    
#     print("Your Eligible for Admission.Please Provide Your Details asked below:")
#     name=input("Name:")
#     add=input("Location:")
#     ph=int(input("contact:"))
#     print("")
#     print("Verified:")
#     print("Name:",name)
#     print("Address:",add)
#     print("phone Numer:",ph)
#     print("Thanks for Uploading")

# else:
#     print("Better Luck Next Time.")

salary=int(input("Enter Your income:"))
age=int(input("Enter Your age:"))

if(salary>=20000 or age<=25):

    print("You are Eligible for loan")
    print("how much loan do you want?")
    loan=int(input())
    if(loan<=50000):
        print("Your Loan will be Sanctioned.")
    else:
        print("Sorry limit is upto 50000 only.")
else:
    print("Your not Eligible for Loan")
