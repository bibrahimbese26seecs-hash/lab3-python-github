def Add(num1, num2):
    return num1 + num2

def Sub(num1, num2):
    return num1 - num2

def Multi(num1, num2):
    return num1 * num2

def Div(num1, num2):
    return num1 / num2
 
def IsEven(num):
    return num % 2 == 0

def Percent(num1, num2):
    return (num1 / num2) * 100

choice = ""
print()
while choice != "-1":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"The Result of addition of the numbers {num1} and {num2} is {Add(num1, num2)}")
    print(f"The Result of subtraction of the numbers {num1} and {num2} is {Sub(num1, num2)}")
    print(f"The Result of multiplication of the numbers {num1} and {num2} is {Multi(num1, num2)}")
    if num2 != 0:   #Check to see if the second number is 0
        print(f"The Result of division of the numbers {num1} and {num2} is {Div(num1, num2)}")
    else:
        print("The second number cannot be 0 for division!")
    choice = input("Do you want to find the percentage of the two numbers(Y/N): ")
    if (choice == "Y"):
        if num2 != 0:   #Check to see if the second number is 0
            print(f"{num1} is {Percent(num1, num2)} percent of {num2}")
        else:
            print("The second number cannot be 0!")
    choice = input("Do you want to find if a nuber is even or odd(Y/N): ")
    if choice == "Y":
        num = int(input("Enter a number: "))
        if IsEven(num):
            print(f"{int(num)} is Even")
        else:
            print(f"{int(num)} is Odd")
    choice = input("Enter -1 to exit the Calculator or press enter to continue: ")
    if choice == "-1":
        print("Exiting the calculator.")
