"""# Home Can you create a Program I will give you number(userinput and print table)
f"{}" String format concept
User input - num int -> 10, 100, -1, 2, 3.14 -> input
9x1 = 9
9x2 = 18... till 10"""
print("Printing Math table")
print("Provide a number")
i = float(input())
j = 1
while j <= 10:
    table = f"{i}*{j}={i * j}"
    j = j + 1
    print(table)
