def addition(a,b):
    return a+b
def substraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b 

input1 = float(input("Enter first number:"))
input2 = float(input("Enter second number:"))

print("Enter a choice \n1.Addition \n2.Substraction \n3.Multiplication \n4.Division")
choice = int(input())
if choice == 1:
    result=addition(input1,input2)
    print("Result is",result)
elif choice == 2:
    result=substraction(input1,input2)
    print("Result is",result)
elif choice == 3:
    result=multiplication(input1,input2)
    print("Result is",result)
elif choice == 4:
    result=division(input1,input2)
    print("Result is",result)
else:
    print("Please enter valid choice")        
















