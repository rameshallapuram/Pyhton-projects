#functions of operations
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def devide(n1,n2):
    return n1/n2

operations = {'+':add, '-':subtract, '*':multiply, '/':devide}

def calculator():

    num1 = float(input("Enter a number: "))
    print(num1)
    num2 = float(input("Enter a number: "))
    print(num2)

    for key in operations:
        print(key)

    continue_calculations = True

    while continue_calculations:
        operator_choice = input("enter an operator from the list above: ")
        result = (operations[operator_choice](num1,num2)) #calling function of operations
        print(result)
        continue_operations = input("Do you want to continue operations? 'yes','new' or 'no': ").lower()
        if continue_operations == "yes":
            num1 = result
            num2 = float(input("Enter a number: "))
        elif continue_operations == "new":
           calculator()
        else:
            continue_calculations = False

calculator()
        