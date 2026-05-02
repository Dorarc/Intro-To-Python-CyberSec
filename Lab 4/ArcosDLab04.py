"""
Name: Dorian Arcos 
Class: CSEC 1436
Date: Jan 210, 2026
Purpose: Lab 04 Assignment - Complete the Try It assignments in the Text book for chapter 3: Hopper Quote, Shift Cypher, Wage Calculator, List Basics, Creating a Tuple With User Input.
"""

'''
Hopper Quote: 
Write a program that prints the following text, including the quotation marks. Your program may not use single quotes (') anywhere in the code. The last line must be indented with a tab character.

    "To me programming is more than an important practical art.
    It is also a gigantic undertaking in the foundations of knowledge."
    	-- Grace Hopper

English Language Design:
print the given text in the same format provided.

Pseudo Code:
1 Print the first line of text using single quote to wrap text.
2 Print second line of text and use a newline character and a tab character to move Grace Hopper name to new line and tabbed over. 
this line is wrapped in single quote as well.

Difference:
The book use a separate lin for the name of the author and the second line of text. I have used a single line broken with a newline character.
'''
print(f'Start of Quote:')
print(f"Hopper Quote:")
print()
print(f'"To me programming is more than an important practical art.')
print(f'It is also a gigantic undertaking in the foundations of knowledge."\n\t-- Grace Hopper')

'''
Shift Cypher: 
During the Roman Empire, Julius Caesar (100–44 BCE) used a simple technique to encrypt private messages. Each letter of the message was replaced with the third next letter of the alphabet. Ex: If the message was CAT, the C became F, the A became D, and the T became W, resulting in the message FDW. This technique is known as a shift cipher because each letter is shifted by some amount. In Caesar's case, the amount was three, but other amounts (besides 0) would work too.

Write a program that prompts the user to input the following two values (example input in bold):

    Enter a 3-letter word: CAT
    Shift by how many letters? 3
The program should then shift each letter of the word by the desired amount. Based on the example above, the output would be:

    The secret message is: FDW

English Language Design:
Ask the user for a three letter word
Ask the user for the how many letters they would like to shift
Convert the entered word into an integer
Add three to the generated integers
Convert the integers back to letters
Provide the computed letters as the secret code for the user

Pseudo Code:
Request an input for a 3 letter word
Request an input for the amount of character to shift
Convert the first letter into an integer
Shift the number by adding the amount of shift provided
Convert the new integer back to a letter.
Repeat for letters 2 and 3.
Print the computed new letter for the user as their secret code.

Difference:
The primary difference between my method and that of the book is that I used many more lines of code.
As I am learning the code for the first time, 
I needed to break uo the workflow to ensure I had an understanding of what was the code is doing
and that I was correctly completing the given task.
'''
print()
print(f'Start of Cypher:')

#variables used to ask user for inputs
word = input(f'Provide a three letter word to encode: ')
shift = int(input(f'How many character would you like to shift for your code?: '))

#variables used to ask convert the letters of the word into code point
first_letter = ord(word[0])
second_letter = ord(word[1])
third_letter = ord(word[2])

#variables used to shift the code point by the given number of characters
first_shift = first_letter + shift
second_shift = second_letter + shift
third_shift = third_letter + shift

#print(first_letter, second_letter, third_letter)

#variables convert the code point to there corresponding letters
first_new = chr(first_shift)
second_new = chr(second_shift)
third_new = chr(third_shift)

#print(first_new, second_new, third_new)

#print the computed shifted letter as the secret code for the user.
print('You secret code is: ', first_new + second_new + third_new)


'''
Wage Calculator:
You just landed a part-time job and would like to calculate how much money you will earn. 
Write a program that inputs the time you start working, the time you stop working, and your hourly pay rate (example input in bold):

    Starting hour: 9
    Starting minute: 30
    Stopping hour: 11
    Stopping minute: 0
    Hourly rate: 15
Based on the user input, your program should calculate and display the following results:

    Worked 9:30 to 11:00
    Total hours: 1.5
    Payment: $22.50
For this exercise, you need to write code that (1) calculates the total payment and (2) formats the three output lines.
 Use f-strings and format specifiers to display two-digit minutes, one decimal place for hours, and two decimal places for payment. 
 The input code has been provided as a starting point.

English Language Design
Start with base code from book.
Inputs for starting time, stopping time, and wages.
Use input to convert start hour to minutes.
Use input to convert stop hour to minutes.
Calculate total of minutes of start time.
Calculate total of minutes of end time.
Calculate total time worked.
Calculate pay based on total time worked.

Pseudo Code:
Start with base code from book.
New variables
    start_hour_convert = 
    stop_hour_convert = 
    start_time = 
    stop_time = 
    total_hours = 
    pay = 
Inputs for starting time, stopping time, and wages.
Use input to convert start hour to minutes: hours * 60.
Use input to convert stop hour to minutes: hours * 60.
Calculate total of minutes of start time: start hours(converted) + start minutes.
Calculate total of minutes of end time: stop hours(converted) + stop minutes.
Calculate total time worked: total of stop time - total of start time.
Calculate pay based on total time worked: total hours worked * inputed rate.

Difference:
The primary difference between my method and that of the book is that I used many more lines of code to calculate the totals needed.
As I am learning the code for the first time, 
I needed to break uo the workflow to ensure I had an understanding of what was the code is doing
and that I was correctly completing the given task.
I also used different names for the variables.
'''
print()
print(f'Start of Wage Calculator:')

#variables given from textbook
start_hour = int(input("Starting hour: "))
start_min = int(input("Starting minute: "))
stop_hour = int(input("Stopping hour: "))
stop_min = int(input("Stopping minute: "))
rate = float(input("Hourly rate: "))
print()

#conversion calculation
start_hour_convert = start_hour * 60
stop_hour_convert = stop_hour * 60
start_time = start_hour_convert + start_min
stop_time = stop_hour_convert + stop_min
total_hours = (stop_time - start_time) / 60 
pay = total_hours * rate

#outputs
print(f'You worked {start_hour}:{start_min:02d} to {stop_hour}:{stop_min:02d}')
print(f'Your total hours worked were: {total_hours:.1f}')
print(f'Your payment for hours worked is: ${pay:.2f}')

'''
List Basics:
Write a program to complete the following:

Create a list with the following elements: 2, 23, 39, 6, -5.
Change the third element of the list (index 2) to 35.
Print the resulting list and the list's length.

English Language Design
Create list from the provided numbers.
Change the third number in the list to the number 35
Print out the new resulting list and its length

Pseudo Code:
Create a list from the provided numbers using a list object
Select the number in the list, 39, and change the number stored in that position
Print the resulting new list
Print the length of the list

Difference:
As this was a short activity that had very little code needed, the difference between my code and that of the book
is the variable name used for the list element
'''
print()
print(f"Start of List Basics")

# Create the list from the given elements

# Change the third element to 35

# Print the resultant list

# Print the length of the list


# Create the list from the given elements
list = [2, 23, 39, 6, -5]

# Change the third element to 35
list[2] = 35

# Print the resultant list
print(list)

# Print the length of the list
print(len(list))

'''
Creating A Tuple With User Input:
Write a program that reads in two strings and two integers from input and creates a tuple, my_data, with the four values.
Given input:
    x
    y
    15
    20
The output is:
    my_data: ('x', 'y', 15, 20)


English Language Design:
Ask users for inputs
Create a tuple from users inputs
Print tuple

Pseudo Code:
Variables used:
    first = first users input
    second = seconds users input
    third = third users input
    fourth = fourth users input as integer
    my_data = tuple variable as integer
Ask for input for each variable
Create a tuple from users inputs
Print the created tuple


Difference:
As this was a short activity that had very little code needed, the difference between my code and that of the book
is the variable name used for the list element
'''
print()
print(f'Start of Tuple:')

#input variables
first = input()
second = input()
third = int(input())
fourth = int(input())

#creation of tuple
my_data = (first, second, third, fourth)

#print tuple
print(f'my_data: {my_data}')
