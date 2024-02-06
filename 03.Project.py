#Create a simple calculator program and prompts for 2
#operands and an operator, then calculates the result.
#Prompt for the first operand (either integer or floating point)
#Prompt for a operator, where:
#   + addtion
#   - subtraction
#   * multiplication
#   \ division
#If an invalid operator is entered, then display
#"Invalid Operator" (Do not display an invalid calculation)
#If a valid operator is entered, display the first number,
#the operand, the second number, an equals sign, and the result of the calculation

n1 = int(input("Enter first number: "))
op = input("Enter operator(+,-,*,/):").strip()
n2 = int(input("Enter second number: "))
if op == "+":
    print("Result:",(n1+n2))
elif op == "-":
    print("Result:",(n1-n2))
elif op == "*":
    print("Result:",(n1*n2))
elif op == "/":
    if n2 != 0:
        print("Result",float(n1/n2))
else:
    print("Invlid Operator")
