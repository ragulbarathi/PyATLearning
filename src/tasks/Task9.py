"""Write a program that prints numbers from 1 to 100. # Loop For However, for multiples of 3,
 print "Fizz" instead of the number, and for multiples of 5, print "Buzz."
For numbers that are multiples of both 3 and 5, print "FizzBuzz."""

print('FizzBuzz Test->Prints Fizz for multiples of 3 , Buzz for multiples of 5 and FizzBuzz for multiples of 3 and 5')
n = 1
while n <= 100:
    print('Fizz') if n % 3 == 0 else (print('Buzz') if n % 5 == 0 else (print('FizzBuzz') if n % 15 == 0 else print(n)))
    n = n + 1
