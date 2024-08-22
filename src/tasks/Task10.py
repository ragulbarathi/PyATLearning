""" Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24"""

n = int(input("Factorial of a number,Enter n:-"))
fact = 1
if n == 0 or n == 1:
    print(f"factorial of {n} is {fact}")
else:
    for i in range(1, n + 1):
        fact = fact * i
print(f"factorial of {n} is {fact}")
