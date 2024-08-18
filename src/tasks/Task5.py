"""### Task #5
- Create a program that takes two numbers as input and prints whether the first number is greater than,
 less than, or equal to the second number."""

a = float(input('Enter num1-'))
b = float(input('Enter num2-'))
result = "Greater than" if a > b else ("less than" if a < b else "equal to")
print(f"num1 is {result} num2")
