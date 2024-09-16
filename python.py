operator = input("enter an operater(+,-,*,/):")
a=float(input("enter the 1st number"))
b=float(input("enter the 1nd number"))

if operator=='+':
    result=a+b
    print(result)
elif operator=='-':
    result=a-b
    print(result)
elif operator=='*':
    result=a*b
    print(result)
elif operater=='/':
    if b!=0:
        result=a/b
        print(result)

