'''
Name: Dorian Arcos 
Class: CSEC 1436
Date: Jan 2, 2026
Purpose: Lab 03 Assignment - Create a script that calculate the time for the first byte of an email is received
    and the last byte after the byte of the email is received and output the answers in milliseconds.

English Language Design:
Ask the user for the distance  to city, the size of the email, and the generation speed of their network card ==> store as float
Convert the distance from mile to meter.
Calculate what 80% of speed of light in 1 meter per second is.
Convert seconds to millisecond.
Compute time of first byte arrival.
Compute time of last byte arrival after first is received.
Print time the first byte to arrives.
Print time for last byte to arrive after first.


Pseudo Code:
Variables used 
    User_Distance = number of miles to the cites the use is sending email stored as float type
    User_File_size = size of users email in megabytes float type
    User_Card_Speed = users generation speed of network card in megabytes per second stored as float type
    Light_Speed = calculate 80% of light speed
    Mile_To_Meter = Conversion of miles to meters
    Sec_To_Mill = Conversion os seconds to milliseconds
    First_Byte = holds calculation and conversion of the speed the first byte arrives in milliseconds.
    Last_Byte = holds calculation and conversion of the speed the last byte arrives after the first in milliseconds.
1) Ask the user for the distance they are sending the email in miles.
2) Ask the user for the size of the email they are sending in megabytes.
3) Ask the user the generation speed of their network card in megabytes per second.
4) Convert distance into meters ==> miles * 1609 meters = distance in meters.
5) Calculate 80% of speed of light in 1 meter per second ==> 80% * 300000000.
6) convert seconds to millisecond ==> 1 sec * 1000 milliseconds.
7) Compute time of first byte arrival.
8) compute time of last byte arrival.
9) print time first first byte to arrive.
10) print time for last byte to arrive after first.

Test numbers:
    Distance in miles, Size of email in megabytes, Generation speed of network card
    a) 250, 45, 325 
    b) 150, 50, 355
    c) 12, 35, 345
    d) 1, 55, 372
Expected Results:
    millisecond until email received, milliseconds until last byte received 
    a) 1.676, 138.4615
    b) 1.0056, 140.8451
    c) .0805, 144.9275
    d) .0067, 147.8495                    
'''
import math
# Tells the user what the app will do.
print(f"Let's find out how fast an email will travel to your friend's inbox \nand the amount of time it takes for the full message to be received!")
#
# Engages and prompts user to to start app
input(f"Hit enter on your keyboard to start!")
#
# Variable used to ask for and store distance in miles as a float type.
User_Distance = float(input(f"What is the distance, in miles, to the city you are sending your email to? "))
#print(User_Distance)
#
# Variable is used to ask for and store the size of the email in megabytes.
User_File_Size = float(input(f"What is the size of the email you are sending in megabytes? "))
#
# Variable is used to ask for and store generation speed of users network card in megabytes per seconds.
User_Card_Speed = float(input(f"What is the generation speed of your network card in megabytes per second? "))
#print(type(User_Distance),User_Distance,type(User_File_Size),User_File_Size,type(User_Card_Speed),User_Card_Speed).
#
# This converts the distance provided by the user from miles to meters.
Mile_To_Meter = User_Distance * 1609
#print(Mile_To_Meter)
#
# This calculates 80% of the speed of light in 1 second; output is in meters/second.
Light_Speed = float(.80 * 300000000)
#print(Light_Speed) 
#
# This is used to convert seconds to milliseconds.
Sec_To_Mill = float(1 * 1000)
#print(Sec_To_Mill)
#
# This Variable converts the file size to bytes.
Byte_Size = User_File_Size * 1024 * 1024
#
# This Variable converts the card speed to bytes to minutes.
Byte_Speed = User_Card_Speed * 1024 * 1024
#
# Arrival of first byte: Computes time it takes for first byte to travel between cities in second and then converts to millisecond. 
First_Byte = (Mile_To_Meter / Light_Speed) * Sec_To_Mill
#print(First_Byte)
#
# Arrival of Last byte: Computes the time it take for the last byte to arrive once the first arrived in seconds and then converts to milliseconds.
Last_Byte = Byte_Size / Byte_Speed * Sec_To_Mill
#print(Last_Byte)
#
# Text line to engage user and let them know the times were computed.
input(f"You Have Mail!\nLets see how long that took.\nHit enter on your keyboard to see the results.")
#
# Empty line for output formatting.
print()
#
# prints the output time of the first byte computation, rounds the output to the 4th decimal place, and displays this for the user.
print(f"The first byte of the email will take", round(First_Byte,4), f"milliseconds to arrive \nin your friends mail box.")
#
# Empty line for output formatting
print()
#
# prints the output time of the last byte arrival time computation, rounds the output to the 4th decimal place, and displays this for the user.
print(f"It will then take", round(Last_Byte,4), f"milliseconds after the first byte arrives \nfor the full email to arrive in their mail box. ")
#
# Empty line for output formatting. 
print()
print(f"That's fast!")
