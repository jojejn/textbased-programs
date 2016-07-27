print("welcome to a calculator")
i = 0
# i made all the operations in functions just to make it easier
def add():
    result = str(num1+num2)
    print("the result is: " + result)
def sub():
    result =str(num1-num2)
    print("the answer is: "+result)
def multi():
    result = str(num1*num2)
    print("the answer is: "+result)
def divide():
    result = str(num1/num2)
    print("the answer is: "+result)
for x in range(0,100):
    print("enter the operation")
    oper = input()
    print("first number:")
    num1 = float(input())
    print("second number:")
    num2 = float(input())
                 
    
    if oper == "+":
       add()

    if oper == "-":
     sub()    

    if oper == "*":
        multi()

    if oper == "/":
        divide()
