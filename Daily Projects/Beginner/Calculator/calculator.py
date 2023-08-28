# Simple python programming that makes a calculator

# Day Goal: Learn about function with outputs
import os
import art
 
def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

operations = {
    '+': addition,
    '-': subtraction,
    '\\': division,
    '*': multiplication,
}


new_calculation = True
while new_calculation:
    clear()
    print("Welcome to the calculator!")
    print(art.logo)

    num1 = float(input("Enter the first number: "))
    ans = 'prev'
    while ans == 'prev':        
        oper = input("Enter which operation you want :-\n+\n-\n*\n\\\nEnter operator: ")

        function = operations[oper]

        num2 = float(input("Enter the second number: "))

        result = function(num1, num2)

        print(f"{num1} {oper} {num2} = {result}")

        ans = input(f"Do you want to continue calculating with the previous result ({result}) or start a new calculation or do you want to exit ('prev' or 'new' or 'exit'): ")
        num1 = result
        print()
        if ans == 'exit':
            new_calculation = False

print("Exiting the calculator.")
        

# Alternatively instead of creating two loops (one for new calculation and another for the previous calculation), we could also just put the entire process inside a function
# and then just call that function for a new calculation, i.e, using recursion. Thereby avoiding the outer while loop.