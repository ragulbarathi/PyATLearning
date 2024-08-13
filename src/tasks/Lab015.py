"""Task #2
Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f{""}
"""
print("Program for >,-,num1 pow num2,*,+,/ ")
print("please enter two numbers")
num1 = float(input())
num2 = float(input())

Maximum = max(num1, num2)
Powerfunction = pow(num1, num2)
subtraction = num1 - num2
multiplication = num1 * num2
addition = num1 + num2
division = num1 / num2

print(f"Maximum of two numbers ={Maximum}", f"Power of num1 to num2 ={Powerfunction}",
      f"Subtraction of num1,num2={subtraction}", f"Multiplication of two num1*num2={multiplication}",
      f"addition num1+num2={addition}", f"division num1/num2={division}", sep="\n")
