'''
Name: Dorian Arcos 
Class: CSEC 1436
Date: Jan 17, 2026
Purpose: Lab 05 Assignment - Write a python program that asks the user for the three sides of a triangle and
prints the validity of the triangle, and if valid, prints the details of the triangle as specified in the assignment instructions. 

English Language Design:
Ask the user for the length of the three sides of a triangle with sides being between 1.0 - 100.0.
    Store sides as a float and sort smallest to largest.
If user provides invalid measurements, a zeros or negative number, print invalid entry message and end program.
If valid measurements, print confirmation that given measurements are a valid lengths.
Confirm if triangle is valid using triangle inequality Theorem.
If triangle is invalid, print out invalid triangle message with given lengths and end program.
If triangle is valid, print out length of each side and the area.
If Triangle is valid, confirm the type of triangle and print out result: Equilateral, Isosceles, Scalene Right Scalene, or Right Isosceles and print Hypotenuse.
End with end of program message.

Testing Values:
    Valid numbers used for testing:
        10,10,10 area= 43.30 Equilateral
        7,10,5 area= 16.25 Scalene
        2,2,3 area= 1.98 Isosceles
        3,4,5 area= 6 Right Scalene
        1,1,1.41 area= .50 Right Isosceles
     

    Invalid number used for testing:
        79,10,15
        1,2,8
        5,5,12
        3,4,7
        0,4,5
        100,4,5
        -1,4,5


Pseudo Code: 
1)Ask use for length of side "a" of triangle with an allowed range of 1.0 - 100.0.
2)Ask for the length of side "b" of triangle with an allowed range of 1.0 - 100.0.
3)Ask use for length of side "c" of triangle with an allowed range of 1.0 - 100.0.
4)Verify entered lengths are valid or invalid.
    if then statement validating entries are >=1.00 and <=100.
        if false output 'invalid entry, program terminated' and end program.
        if true output 'lengths accepted' and continue program.
5)Sort entries from smallest to largest.
    Use the sorted command to sort the entires from smallest to largest.
6)Validate sides form a triangle.
    Use Inequality Theorem. 
        Smallest + Middle > Largest.
    If invalid, print triangle is invalid with the length of each side and terminate program.
    If valid: print triangle is valid with the length of three sides and the area.
7)determine type of triangle.
    if all sides are equal, print triangle is equilateral.
    if two sides are equal, print triangle is isosceles.
    if two sides are equal and the Pythagorean Theorem is true, print triangle is a right isosceles triangle.
    if no sides are equal, print triangle is scalene.
    if no sides are equal and the Pythagorean Theorem is true, print triangle is a right scalene triangle.
8)Print end of program message.
'''

import math


a = float(input(f'What is the length, between 1.00 - 100.00, of the first side of the triangle?: '))
b = float(input(f'What is the length, between 1.00 - 100.00, of the second side of the triangle?: '))
c = float(input(f'What is the length, between 1.00 - 100.00, of third side of the triangle?: '))
side_order = sorted([a,b,c])
a2 = side_order[0]
b2 = side_order[1]
c2 = side_order[2]
#print(a1,b1,c1)
#print(side_order)

side_check = f'Lengths Accepted!' if (a2 >= 1.00 and a2 <= 100) and (b2 >= 1.00 and b2 <= 100) and (c2 >= 1.00 and c2 <= 100) else exit(f'Invalid Entry, Program Terminated.')   
print(side_check)

triangle_check = f'This Is A Valid Triangle!' if (a2 + b2) > c2 else exit(f'Triangle Is Invalid, Program Terminated: {side_order}.')
print(triangle_check)

s = (a2 + b2 + c2) / 2
area = math.sqrt(s * (s - a2) * (s - b2) * (s - c2))
user_area = round(area, 2)
p_thag = a2**2 + b2**2 == c2**2
#print(round(area, 2))

print(f'The length of the sides of the triangle are: {side_order}\nThe Area of the triangle is: {user_area: .2f}')

if a2 == b2 and b2 == c2 and a2 == c2:
   print(f'This is an Equilateral Triangle. The hypotenuse is {c2}')
elif a2==b2 or a2==c2 or b2==c2:
    if a2**2 + b2**2 == round(c2**2):
        print(f'This is an isosceles right triangle. The hypotenuse is {c2}.')
    else:
       print(f'This is an isosceles triangle. The hypotenuse is {c2}')
elif a2!=b2  and b2!=c2 and a2!=c2:
    if a2**2 + b2**2 == c2**2:
        print(f'This is a scalene right triangle. The hypotenuse is {c2}.')
    else:
        print(f'This is a scalene triangle. The hypotenuse is {c2}')
print('Program Completed.')