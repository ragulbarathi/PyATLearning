"""
Task #3
-(i) Explain the difference between the = operator and the == operator in Python.

- (ii)What does the ** operator do in Python, and how is it used?

- (iii)What does the ^ operator do in Python, and in what context is it commonly used?
"""

"""(i) -->Here '=' is the assignment operator which assigns value from right to left.Example: - a=6 here 6
is assigned to variable a,whereas '==' is a boolean operator, it compares the two values and returns true 
or false"""
a = 2
print(a)
b = 2
print(a == b)
b = b + 1
print(a == b)
"""(ii)-->Here '**' is the power operator ie.x**y means x base^ pow y"""
c = a ** b
print(c)
"""(iii)-->Here '^' is xor operator which is form of an logical operator-bitwise operator,it is generally used for 
xor encryption"""
print(a ^ b)
print(True ^ True)
print(True ^ False)
print(False ^ True)
print(False ^ False)
"""can be used to swap two integers"""
# First integer
a = 10
# Second integer
b = 27

print("Before Swapping:")
print("a =", a)
print("b =", b)

# swapping integers using XOR
a = a ^ b
b = a ^ b
a = a ^ b

print("After Swapping:")
print("a =", a)
print("b =", b)
