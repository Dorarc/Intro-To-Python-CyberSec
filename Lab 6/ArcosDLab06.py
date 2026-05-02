'''
Name: Dorian Arcos 
Class: CSEC 1436
Date: Feb 24, 2026
Purpose: Lab 05 Assignment - Write a program that asks the user for the height of the initial drop (in ft), the bounce coefficient, and the stop
threshold (in inches). It then prints a table with the bounce number, the height of the ball in feet, the height of the
ball in inches, and the total distance covered by the fall in feet after each bounce. Your program should check to see
if the input is within bounds and makes experimental sense or else, that experiment terminates. The program
should allow additional experiments, until the user decides to quit

English Language Design:
Start loop for program
Ask user for inputs
If invalid, print invalid message and restart.
If valid, begin calculations
Calculation: 
    Start with drop height
    Start heigh multiple by bounce coefficient to get next bounce height
        repeat with each new bounce height until bounce height is less than stop threshold
    To find distance starting height plus height of bounce height time 2 ( up and down)
        This is new current distance
        Repeat with each new bounce height, adding to new current distance until bounce height is less than stop threshold 
Print number of bounces, height of each bounce, and total distance covered in a table format until bounce height is less than stop threshold
Print the final number of bounces and the total distance covered
Ask user if they would like to restart the program
    If no, end program with ending message
    If yes, restart program

Testing Values:
    Test program with valid inputs:
        Valid numbers used for testing:
            500, .5, 3
            675, .75, 2.4
            723.5, .25, 0.5
            432, .56, 2.75
    Test program with invalid inputs:
        Invalid number used for testing:
            -100, .5, 2
            100, -0.5, 1
            100, .5, -1
            1001, .5, 1
            100, 1.5, 1
            100, .5, 4

Pseudo Code:
Restart variable and start print message
While loop for program
    While restart is yes:
        User float inputs for
            Drop height in feet
            Bounce coefficient (how much bounce)
            When the ball is no longer considered bouncing (stop threshold in inches)
        Test validity with if statement
            height < 1 or height > 1000, bounce < 0.1 or bounce > 0.99, stop_threshold < 0.01, stop_threshold > 3
        If invalid, print invalid message and restart while loop with continue statement
        If valid, store values as floats, start else statement
            bounce of 0
            total height ==initial drop height
            current height == initial drop height
        Print table header: bounce number | current height in feet | current height in inches | total distance covered in feet
            Start while loop for new bounce height and total distance covered
                while (current_height * number of bounces * 12) >= stop_threshold
            Bounces is increased by 1 each time loop runs
            Current height updates each loop 
                current height by bounce coefficient
            Total distance ball travels updates each loop
                Total distance + new bounce height * 2 (up and down) 
            Print bounce number, current height in feet, current height in inches, and total distance covered in feet in as a new row with formatting for spacing and alignment
            repeat while loop until when bounce height <= stop threshold
    Print bounce stopped message
        include number of total bounces and total distance traveled in feet
    Ask user if they would like to repeat program (yes/no).lower()
        If yes, restart while loop
        if no, print goodbye message end program after pause
'''
import time
restart = 'yes'
print(f'How Many Bounces Will It Last?')

while restart == 'yes':
    
    print()

    height = float(input(f"Between 1 and 1000 feet, how high are you dropping the ball from?: "))
    bounce = float(input(f"Between 0.1 and 0.99, how bouncy is the ball?: "))
    stop_threshold = float(input(f"Between 0.1 and 3 inches, when is the ball no longer considered bouncing?: "))

    if height < 1 or height > 1000 or bounce < 0.1 or bounce > 0.99 or stop_threshold < 0.01 or stop_threshold > 3:
        print()
        print(f'Your inputs fall outside the requested values')
        print("-" * 40)
        print(f'Make sure your height is between 1-1000 feet, the bounciness is between 0.1-0.99,\nand when the ball is no longer considered bouncing is between 0.1-3 inches.')
        print()
        continue
    else:
       bounces = 0
       total_distance = height
       current_height = height 

       print(f'| Bounce Number | Current Height (ft) | Current Height (in) | Current Distance (ft) |')
       
       while (current_height * bounce * 12) >= stop_threshold:
            
            bounces = bounces + 1
            new_bounce = current_height * bounce
            total_distance = total_distance + (new_bounce * 2)

            print(f'{bounces:^15} {new_bounce:^21.4f} {new_bounce * 12:^21.4f} {total_distance:^24.4f}')

            current_height = current_height * bounce
        
    print(f'The ball has stopped bouncing!')
    print(f'The ball bounce {bounces} times!')
    print(f'The ball bounced about {round(total_distance,4)} feet!')

    restart = input('Would you like to bounce the ball again? (yes/no): ').lower()
    print()

print(f'Goodbye!')
time.sleep(1.5)