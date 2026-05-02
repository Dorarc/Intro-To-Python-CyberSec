'''
Name: Dorian Arcos 
Class: CSEC 1436
Date: Jan 27, 2026
Purpose: Lab 02 Assignment - Create a script that walks a user though 
    calculating the parameter, area, and volume of a cuboid.
 
English Language Steps:
1) Inform use of what we will be calculating the Parameter, Surface, and Volume of a cuboid.
2) Ask the user for the length of the cuboid.
3) Ask the user for the width of cuboid.
4) Ask the user for the height of the cuboid.
5) Print the provided inputs.
6) Compute the Parameter, area, and volume.
7) Round answers to the third decimal place.
9) Output the computed rounded totals for the user to see.

Pseudo Code:
Variables:
    length = ask for the length in inches between 1-99
    width = ask for the width in inches between 1-99
    height = ask for the height in inches between 1-99
    parameter = calculated parameter
    area = calculated area
    volume = calculated volume
    pshort = rounded calculated parameter
    ashort = rounded calculated area
    vshort = rounded calculated volume
print asking the user for the measurements between 1-99 inches.
store measurements in variables
print the provided measurements back to the user
store calculations for the wanted values in variables
store the calculated values in rounding variables
print the rounding variables 

print(f"Let's calculate the Parameter, Surface Area, and Volume of a Cuboid together! ")
#
# These are the variables uses to store the user provided length, height, and width.
length = float(input("What is the Length of the Cuboid? Provide a measurement between 1-99 inches: "))
height = float(input("What is the Height of the Cuboid? Provide a measurement between 1-99 inches: "))
width = float(input("What is the Width of the Cuboid? Provide a measurement between 1-99 inches: "))
print()
#
# These were used for confirmation test of provided inputs to ensure they print properly and the type is float.
# print(length, type(length))
# print(height, type(height))
# print(width, type(width))
#
# This repeats the length, height, and width provided back to the user.
print(f"The Length of the Cuboid is: {length} inches. "
      f"\nThe Height of the cuboid is: {height} inches. "
      f"\nThe Width of the Cuboid is: {width} inches. ")
print()
#
# These are the variables used to calculate the parameter, area, and volume.
parameter = 4 * (length + width + height)
area = 2 * (length*width + length*height + width*height)
volume = length * width * height
#
# These were used to test that the computed outputs are correct and still providing a float value.
print(parameter, type(parameter))
print(area, type(area))
print(volume, type(volume))
#
# These variables are used to round to the 3rd decimal place.
pshort = round(parameter, 3)
ashort = round(area, 3)
vshort = round(volume, 3)
#
# These are used to test the rounding works properly and is still providing a float value.
# print(pshort, type(pshort))
# print(ashort, type(ashort))
# print(vshort, type(vshort))
#
# These lines are used to output the parameter, area, and volume calculated. 
print(f"The Parameter of the Cuboid is: {pshort} inches. ")
print(f"The Surface Area of the Cuboid is: {ashort} square inches. ")
print(f"The Total Volume of the Cuboid is: {vshort} cubic inches. ")'''

# temp indicator 
'''
Name: Dorian Arcos
Class: CSEC 1436
Purpose: generate a simple problem statment


english language process:
(look at notes)
Testing:
(notes)
Psuedo Code
(notes)
'''

'''

daytime = int(input (f'please a temp reading as an integer between 50 and 120 degrees f (ex:70):'))

print(f'day temp is: {daytime}')
if (daytime >=50) and (daytime <= 60):
    print(f'it is a cold day today')
else:
    if daytime >= 61 and daytime <=70:
        print(f'it is a nice day')

    else:
        if daytime >= 71 and daytime <=80:
            print(f'it is a warm day')
        else:
            if daytime >=81 and daytime <=90:
                print(f'it is hot')
            else:
                if daytime >=91 and daytime <=100:
                    print(f'it is teaxas hot')
                else:
                    print(f'the temp you entered {daytime} cannot be processed.')
# using elif with processing incorrect range first
if daytime < 50 or daytime > 100:
    print(f"the temp you entered {daytime} cant be processed") 
if daytime >=50 and daytime <= 60:
    print(f'it is a cold day today')
elif daytime >= 61 and daytime <=70:
    print(f'it is a nice day')
elif daytime >= 71 and daytime <=80:
    print(f'it is a warm day')
elif daytime >=81 and daytime <=90:
    print(f'it is hot')
elif daytime >=91 and daytime <=100:
    print(f'it is texas hot')

#read up on switch statements 

if daytime < 50 or daytime > 100:
    print(f"the temp you entered {daytime} cant be processed") 
else:
    if daytime >=50 and daytime <= 60:
        print(f'it is a cold day today')
    elif daytime >= 61 and daytime <=70:
        print(f'it is a nice day')
    elif daytime >= 71 and daytime <=80:
        print(f'it is a warm day')
    elif daytime >=81 and daytime <=90:
        print(f'it is hot')
    elif daytime >=91 and daytime <=100:
        print(f'it is texas hot')

'''

#test single line if statement "if expression"
a = 5
b = 10

c = (7 if a < b else 10)
print(f"value of c {c}")

a = 5
b = 10

c = (7 if a > b else 10)
print(f"value of c {c}")

