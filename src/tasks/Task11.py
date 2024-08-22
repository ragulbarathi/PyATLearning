"""Fibonacci Series"""

"""With for Loop"""

n = 10

# Initializing the first two terms
a = 0
b = 1

# Displaying the Fibonacci sequence
print("Fibonacci Sequence:")
for _ in range(n):
    print(a, end=" ")
    temp = a + b
    a = b
    b = temp
