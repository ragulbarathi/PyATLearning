"""Triangle Classifier:Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides, determine if the triangle is
 equilateral (all sides are equal), isosceles (exactly two sides are equal),
or scalene (no sides are equal). Use an if-else statement to classify the triangle."""
print('Triangle Classifier')
x1 = int(input('Enter length of side1 of triangle'))
x2 = int(input('Enter length of side2 of triangle'))
x3 = int(input('Enter length of side3 of triangle'))

if x1 == x2 == x3:
    print('Equilateral')
elif x1 == x2 or x1 == x3 or x2 == x3:
    print('Isosceles Triangle')
else:
    print('Scalene Triangle')
