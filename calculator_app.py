def add(a, b):
    return(a + b)

def substract(a, b):
    return( a - b)

def multiply(a, b):
    return(a * b)

def divide(a, b):
    if b == 0:
        return "❌, Can't divide from Zero"
    return(a / b)

print("Smart Calculator!")


while True: 

    
    print("-- menu --")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    calculation = input("What calculation you want to perform")

    if calculation == "5":
        print("Thanks for using smart calculator")
        break

    if calculation not in ["1", "2", "3", "4"]:
        print("❌, invalid choice try again")
        continue

    
    num1 = float(input("Enter your first number!"))
    num2 = float(input("Enter your second number!"))

    
    if calculation == "1":
        print("Result:",add(num1, num2))
    
    elif calculation == "2":
        print("Result:", substract(num1, num2))

    elif calculation == "3":
        print("Result:", multiply(num1,num2))

    elif calculation == "4":
        print("Result:", divide(num1, num2))

    else:
        print("❌, Invalid opreation")
    