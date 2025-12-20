a=float(input("a:"))
c=input()
b=float(input("b:"))
match c:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
    case "*%":
        print(a%b)
    case _:
        print("invalid operation")
    
