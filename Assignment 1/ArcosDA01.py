'''
Name: Dorian Arcos 
Class: CSEC 1436
Date: 3/19/2026
Purpose: Assignment 01 - Write a program that determines the maximum time it takes to hack a combination lock using brute force - 
this is trying all possible combinations. 
A lock can have 3, 4, 5,or more rings which have to be twirled to open the lock. 
Each ring consist of a number from 0 to 9.


English Language Design:
1) Ask the user for the min number of rings. Must be >= 3 and < 10.
2) Validate if the provided number is >= 3 and < 10.
    If invalid, print error message and repeat question for min number of rings.
    If valid, move to max.
3) Ask the user for the max number of rings. must be >= min and <= 10.
4) Validate if provided number is >= min and <=10
    If invalid, print error message and repeat question for max number of rings.
    If valid, move next next steps.
5) Starting with min number of rings, ask for time it take to rotate the rings to enter the combination. Must be between > 0 seconds and <= 10 seconds.
6) Validate if provided number is between > 0 seconds and <= 10 seconds.
    If invalid, print error message and repeat question for time to rotate rings for combination.
    If valid, move to printing results.
7) Print the time it takes to break the lock in days, hours, minutes, and seconds. 
8) Save the result to the Text File ArcosDA01.txt.
9) Repeat with each number of rings until the max number of rings is completed.
10) Print end program message.

Testing:
    1)Test with invalid inputs for min and max number of rings.
        Should output error message and repeat question.
    2)Test with valid inputs for max number of rings.
        Should move to next question starting with min number of rings.
    3)Test with invalid inputs for time to rotate rings starting with min number..
        Should output error message and repeat question.
    4)Test with valid inputs for time to rotate rings.
        Should output time in days, hours, minutes, and seconds and save to text file.
    5)Should move to next number of rings and repeat until max number of rings is reached.
Testing Number:
    Invalid min inputs: 0,1,2,10,11
    Valid min inputs: 3,4,6
    Invalid max inputs: Any number smaller than the provided min number, 11, 12
    Valid max inputs: number >= min number, 10
    Invalid time inputs: -2, -1, 0, 11, 12
    Valid time inputs: 2, 3, 10
Test Case Numbers:
    min:3
    Max:5
    Time:2
        3 rings: 0 days, 0 hours, 33 minutes, 20 seconds
        4 rings: 0 days, 5hours, 33 minutes, 20 seconds
        5 rings: 2days, 7 hours, 33 minutes, 20 seconds
    min:4
    max:6
    time:3
        4 rings: 0 days, 8 hours, 20 minutes, 0 seconds
        5 rings: 3 days, 11 hours, 20 minutes, 0 seconds
        6 rings: 34 days, 17 hours, 20 minutes, 0 seconds
    min:6
    max:6
    time:10
        6 rings: 115 days, 17 hours, 46 minutes, 40 seconds

Pseudo Code:
print start message
min = int input for min number of rings
    while loop for min number of rings
    while min is < 3 or >= 10
    Test validity of min input
        Must be >= 3 and < 10
        if invalid
            Print error message 
            min = int input for min number of rings
            while loop repeats
        if valid
            End while loop and move to max number loop
max = int input for max number of rings
    While loop for max number of rings
    While max is < min or > 10
    Test validity of max input
        must be >= min and <=10
        If invalid 
            Print error message
            max = int input for max number of rings
            while loop repeats
        If valid 
            End while loop and move to Seconds loops
    Create and Open ArcosDA01.txt in append mode
    For loop to calculate times for range min to max
        For ring in range min to max 
        time = float input for time is takes to rotate rings to enter combo
        While loop for first number of combinations
            While time is <=0 or >10
            Test validity of time input
                Must be >0 and <=10
                If invalid
                    print error message 
                    time = float input for time is takes to rotate rings to enter combo
                    Repeat while loop
                If valid
                    End while loop begin calculation for output 
        total_seconds =  (10 ** ring) * time
        days = total_seconds // 86400
        remaining = total_seconds % 86400
        hours = remaining // 3600
        remaining = remaining % 3600
        minutes = remaining // 60
        seconds = remaining % 60
        Print calculated days, hours, minutes, and seconds
        Write calculated times to ArcosDA01.txt file
        For Loop repeats until max number input number is calculated and times are saved to txt file.
    End for loop
    Save and Close ArcosDA01.txt file
Print end of program message
'''

print(f"Let's Get Cracking!")
print(f'Welcome to the Lock Cracking Time Calculator')
print(f"let's get started!")

rings-min = int(input(f'Greater than or equal to 3 and less than 10 rings, what is the minimum number of rings on your lock?: '))
while rings-min < 3 or rings-min >= 10:
    print(f'ERROR: Invalid input. Ensure your input is greater than or equal to 3 and less than 10 rings.')
    rings-min = int(input(f'Greater than or equal to 3 and less than 10 rings, what is the minimum number of rings on your lock?: '))
#print({min_rings})
rings-max = int(input(f'Greater than or equal to {rings-min} and less than or equal to 10 rings, what is the maximum number of rings on your lock?: '))
while rings-max < rings-min or rings-max > 10:
    print(f'ERROR: Invalid Input. Ensure your input is Greater than or equal to {rings-min} and less than or equal to 10 rings')
    rings-max = int(input(f'Greater than or equal to {rings-min} rings and less than or equal to 10 rings, what is the maximum number of rings on your lock?: '))
#print(max_rings)
ArcosDA01 = open('ArcosDA01.txt', 'a')
print(f'The minimum number of rings is {rings-min} and the maximum number of rings is {rings-max}.')
ArcosDA01.write((f'The minimum number of rings is {rings-min} and the maximum number of rings is {rings-max}.\n'))
for ring in range(rings-min, rings-max +1):
    time = float(input(f'Greater than 0 and up to 10, how many seconds does it take to set a lock with {ring} rings?: '))
    while time <= 0 or time > 10:
        print(f'ERROR: Invalid input. Ensure your input is greater than 0 and up to 10 seconds.')
        time = float(input(f'Greater than 0 and up to 10, how many seconds does it take to set a lock with {ring} rings?: '))
    #print(time)
    #the following are the calculations and conversions for the need times
    total_seconds = (10 ** ring) * time
    days = total_seconds // 86400
    remaining = total_seconds % 86400
    hours = remaining // 3600
    remaining = remaining % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    print(f'It will take at most {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds to crack a combination with {ring} rings.')
    ArcosDA01.write(f'It will take at most {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds to crack a combination with {ring} rings.\n')
ArcosDA01.close()
print(f'We cracked the locks! All Done! Goodbye!')



