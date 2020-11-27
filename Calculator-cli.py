import math

Uname = input("Enter Your Name:")

Num1 = float(input("Enter a Number:"))
Num2 = float(input("Enter another Number:"))

print("Choose: +, -, *, /")
ask = input("What you what to do:")


if ask=="+"or "add" or "ADD":
    print(str(Num1+Num2))

elif ask=="-" or "minus" or "substract":
    print(str(Num1-Num2))

elif ask=="*":
    print(str(Num1*Num2))

elif ask=="/":
    print(str(Num1/Num2))

else:
    print(Uname,"Entered",Num1,",",Num2,"Do you want to change")

# Ask_change = print(Uname,"Entered",Num1,",",Num2,"Do you want to change")
# change = input("If yes(Y)/No(N):")

# if change=="Y"or "y" or "yes" or "Yes":
#     print("Hello")