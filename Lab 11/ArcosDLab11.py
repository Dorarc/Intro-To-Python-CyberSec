'''
Name: Dorian Arcos 
Class: CSEC 1436
Date: April 7, 2026
Purpose: Lab 11 Assignment - Audit a text file that contains a list of words:
    Read a Text file of a list of words. Filter and sort into list for 5, 6, and 7 character lengths and in alphabetical order. Add each list to its own text file.
    Ask the user to for a letter they would like to search for in the list. Search through the list for all words that contain the letter 
    and print the number of results and a table of found words for each list.
    Then ask the user for another letter to search for as well as what position the letter should be in.
    Search through the list for all words that contain the letter in the specified position and print the number of results and a table of found words for each list.

English Language Design:
Stage 1:
Open file Words.txt
read word text file
add all word into a list called AllWordsList.
    each item in the list is a word without a newline character.
print the total number of words in the file.

Stage 2:
create alphabet variable
create empty list for 5, 6, and 7 character words
In the list AllWordsList:
    convert all words to lowercase.
    For loop to check for any words that do not contain alpha characters.
        Skip word if it contains non alpha characters.
    check the length of each word.
        append to appropriate list based on length.
            FiveCharList, SixCharList, SevenCharList.
    continues until all word are sorted into proper list.
Print the total number of words in each list.

Stage 3:
sort 5 character list in alphabetical order.
sort 6 character list in alphabetical order.
sort 7 character list in alphabetical order.

Stage 4:
Open text file for 5 characters in write mode.
write 5 character list to text file.
    one word per line.
Close 5 character text file.
Open text file for 6 characters in write mode.
write 6 character list to text file. 
    one word per line.
Close 6 character text file.
Open text file for 7 characters in write mode.
write 7character list to text file. 
    one word per line.
Close 7 character text file.

Stage 5:
Part 1:
ask the user for a letter they would like to use to find words that contain that letter from each of the different list.
    if not a valid alphabetical character, continue asking use until correct input is given.
    if valid begin search for Words containing letter.
Part 2:
search list for input audit letter in any position in Words.
Store matching Words in separate list for each Char List.
print the total number of matches in each list
    number of matches in 5 Char List:
    number of matches in 6 Char List:
    Number of matches in 7 Char List:
Display the Words from each list that contain audit letter in table format with only 5 words per line
    5 Char List Table
    6 Char List Table
    7 Char List Table

Stage 6: 
Part 1:
ask the user for a letter they would like to use to find Words that contain that letter from each of the different list.
    Ask for for the character
        if not a valid alphabetical character, continue asking use until correct input is given.
        if valid, move to next step.
    Ask user for a the position the character should be in.
        Confirm the position is between 1 and 7
            if not valid, continue asking use until correct input is given.
            if valid, move to next step.
Part 2:
search list for input audit letter at the specific input position in Words.
    if the position is greater than 5, skip 5 Character list and move to next list.
    if the position is greater than 6, skip 6 Character list and move to next list.
    if the position is greater than 7, skip 7 Character list and move to next list.
store matching words in a seperate list for each Char List.
print the total number of matches in each list
    number of matches in 5 Char List:
    number of matches in 6 Char List:
    Number of matches in 7 Char List:
Display the Words from each list that contain audit letter in table format with only 5 words per line
    5 Char List Table
    6 Char List Table
    7 Char List Table
If table is empty do not display the table


    


Testing:
Stage 1:
run code 
    does for loop work as expected?
        does list show words correctly?
    does code print total number of words?
Stage 2:
run code
    does loop properly convert to lowercase?
    does loop properly skip words that do not contain alpha characters?
    does code sort words based on length of word into appropriate list?
Stage 3:
    run code
    verify each list is properly sorted in alphabetical order.
Stage 4:
        does each required text file get generated?
        are words on separate line, lowercase, and in alphabetical order?
Stage 5:
Part 1:
Run code
    is input question asked?
    does invalid test examples cause loop to repeat?
    does valid test examples cause loop to end?
        Invalid test inputs:
            1, 2, 123, ab, abc, *
        Valid test inputs:
            a, b, c, z
Part 2:
Run code
    does the match count print for each list?
    does the table display with proper formatting?
    Test Letters:
    l, s
Stage 6:
Part 1:
Run code
    does input question ask for letter?
        does invalid test example cause loop to repeat?
        does valid test example casue loop to end?
            invalid test inputs:
                1, 2, 123, ad, abd, *
            valid test inputs:
                a, b, c, z
    does input question ask for position?
        does invalid test examples cause loop to repeat?
        does valid test examples cause loop to end?
            Invalid test inputs:
                0, 8, 9, ab, *, 12
            Valid test inputs:
                1, 5, 6, 7
Part 2:
Run code
    does match count print for each list?
    does skipped list print skip message?
    does table only display when matches are found?
    does table display with proper formatting?
    Test Letter and Position combinations:
        l at position 1
        s at position 5
        z at position 7
        a at position 6

Pseudo Code:
Stage 1
Starting program message
open Words.txt in read mode with encoding utf-8.
create an empty list called AllWordsList
Start loop to read each line in the file.
    for loop will read each line as a sting and remove the last character from the sting.
    loop will then append sting to the list AllWordsList.
For each Line in WordsTXT:
    slice sting to remove last character
    append to list AllWordsList
Once call lines in Words.txt are appended to list, close file.
Print (total number of words in AllWordsList)

Stage 2:
create variable for alphabet
create empty list for 5,6 and 7 character words
start loop to sort AllWordsList
    for loop will:
        convert list to lowercase.
        for loop compares each list item to alphabet variable
            if passes check
                continues to next step
            if fails check
                item is skipped and loop moved to next list item
        start else statement to check the length of each word.
            sort into appropriate list based on number of characters.
    for each Word in AllWordsList:
        convert Word to lowercase
        for characters in lowercase:
            if the character is not found in the alphabet variable:
                break to restart for alpha check loop
        else:
            check the length of word
                if word contains 5 characters 
                    append to FiveCharList
                elif word contains 6 characters
                        append to SixCharList
                elif word contains 7 characters
                        append to SevenCharList

Stage 3:
sort 5 character list in alphabetical order.
FiveCharList sort
sort 6 character list in alphabetical order.
SixCharList sort
sort 7 character list in alphabetical order.
SevenCharList sort

Stage 4:
open text file for 5 character words in write mode.
    open ArcosDFiveCharList.txt write in utf-8
for loop to write words to text file
    for each Word FiveCharList
        write to text file on new line
Close text file.
open text file for 6 character words in write mode.
    open ArcosDSixCharList.txt write in utf-8
for loop to write words to text file
    for each Word SixCharList
        write to text file on new line
Close text file
open text file for 7 character words in write mode.
    open ArcosDSevenCharList.txt write in utf-8
for loop to write words to text file
    for each Word SevenCharList
        write to text file on new line
Close text file.

Stage 5:
Part 1:
Ask the user for a single letter to audit the word list with a while loop
Loop will also validate the input is a valid letter in the alphabet stored in audit_letter variable.
    Valid variable = True
    while Valid is False 
        ask use for a single letter to audit the word lists
            if character is in alphabet variable
                Valid becomes True
    exit loop
            if input is invalid 
                Valid stays False
                    continue to ask the user for a valid letter
Part 2:
Create empty list for each Char List 
    Five_Char_Audit 
    Six_Char_Audit 
    Seven_Char_Audit
For loop to search for audited character
    for words in FiveCharList
        if audited letter is found
            append to Five_Char_Audit
Repeat For loop for each CharList
print number of words in Five_Char_Audit
    Repeat for each list
print table title with centering format
print separator line
print words in Five_Char_Audit in table format with 5 words per row
    using a counter set for 0
    for loop where words in list file
        print word from Char_Audit list
        after word increase counter
        once counter reaches 5
            start new line
            rest counter to 0         
            repeat printing words
    loop continues until all words printed in table format
Repeat loop for Six and Seven Audit list.

Stage 6:
Part 1:
Ask the user for a single letter to audit the word list files and the specific position letter should be with a while loop
first loop validates input letter is valid and then second loop request position is between 1 to 7.
    Valid variable = True
    while Valid is False
        ask the user for a single letter to audit the word lists to be stored in audit_letter_pos variable.
            if character is in alphabet variable
                Valid becomes True
    exit loop
            if input character is invalid
                Valid stays False
                    Continue to ask the use for a valid letter
    create numbers variable of '1234567'
    Valid variable = True
        while Valid is False
            ask the user for a specific position the character should be in in the words stored in audit_num_pos variable.
                if position number is in numbers variable
                    convert position number variable to an integer 
                    Valid becomes True
        exit loop
Part 2:
Create empty list for each Char list.
    Five_Char_Pos
    Six_Char_Pos
    Seven_Char_Pos
begin searching for matching words in words list
    for words in Five Character List
        check if position number variable is >5
            print skip error message
        else
            check if words in position number variable -1 equals  audit letter number variable
                append to Five Character Position empty list changing to >6 and >7 for respective Character Position list
Repeat For loop for each Character List
print number of words in Five Character Position list
    Repeat for each Character Position list
print table title with centering format
print separator line
print words in Five Character Position list in table format with 5 words per row
    using a counter set for 0
    for loop where words in list file
        print word from Character Position list
        after word increase counter
        once counter reaches 5
            start new line
            rest counter to 0         
            repeat printing words
    loop continues until all words printed in table format
Repeat loop for Six and Seven Character Position list.
print end message
'''
#stage 1:
print(f'Lets audit a text file with lines of different words')

WordsTXT =  open('Words.txt', 'r', encoding= 'utf-8')
AllWordsList = []
for Line in WordsTXT:
    WordString = Line[:-1]
    AllWordsList.append(WordString)
# print(AllWordsList) testing if words show \n removed and are appending properly
WordsTXT.close()
print(f'The total number of words found is: {len(AllWordsList)}')

#stage 2
alphabet = ('abcdefghijklmnopqrstuvwxyz')
FiveCharList = []
SixCharList = []
SevenCharList = []

for Words in AllWordsList:
    LowerWords = Words.lower()
    for characters in LowerWords:
        if characters not in alphabet:
            break
    else:
        #print(LowerWords) testing if words were properly converted to lowercase and only contained alpha characters
        if len(LowerWords) == 5:
            FiveCharList.append(LowerWords)
        elif len(LowerWords) == 6:
            SixCharList.append(LowerWords)
        elif len(LowerWords) == 7:
            SevenCharList.append(LowerWords)
print(f'The total number of words with 5 characters is: {len(FiveCharList)}')
print(f'The total number of words with 6 characters is: {len(SixCharList)}')
print(f'The total number of words with 7 characters is: {len(SevenCharList)}')
#print(FiveCharList) test to confirm list is 5 characters
#print(SixCharList) test to confirm list is 6 characters
#print(SevenCharList) test to confirm list is 7 characters

#Stage 3
FiveCharList.sort()
SixCharList.sort()
SevenCharList.sort()
#print(FiveCharList[:5]) Test if sorting properly   
#print(SixCharList[:5]) Test if sorting properly   
#print(SevenCharList[:5]) Test if sorting properly   

#Stage 4
FiveCharFile = open('ArcosDFiveCharacterList.txt', 'w', encoding= 'utf-8')
for Word in FiveCharList:
    FiveCharFile.write(Word + '\n')
FiveCharFile.close()
SixCharFile = open('ArcosDSixCharacterList.txt', 'w', encoding= 'utf-8')
for Word in SixCharList:
    SixCharFile.write(Word + '\n')
SixCharFile.close()
SevenCharFile = open('ArcosDSevenCharacterList.txt', 'w', encoding= 'utf-8')
for Word in SevenCharList:
    SevenCharFile.write(Word + '\n')
SevenCharFile.close()

#Stage 5
#Part 1
Valid = False
while Valid == False:
    audit_letter= input(f'Lets audit the word list.\n'
                        f' What single letter of the alphabet would you like to audit words for?: ').lower()
    if audit_letter in alphabet and len(audit_letter) == 1:
        Valid = True
#Part 2
Five_Char_Audit = []
Six_Char_Audit = []
Seven_Char_Audit = []

for Word in FiveCharList:
    if audit_letter in Word:
        Five_Char_Audit.append(Word)
#print(Five_Char_Audit) Testing list audit
for Word in SixCharList:
    if audit_letter in Word:
        Six_Char_Audit.append(Word)
#print(Six_Char_Audit) Testing list audit
for Word in SevenCharList:
    if audit_letter in Word:
        Seven_Char_Audit.append(Word)
#print(Seven_Char_Audit) Testing list audit
print(f'Auditing the letter {audit_letter} found:\n{len(Five_Char_Audit)} Five letter words\n'
      f'{len(Six_Char_Audit)} Six letter words\n'
      f'{len(Seven_Char_Audit)} Seven letter words')

counter = 0

print(f"{'Words Found With 5 Letters:':^50}")
print('-' * 49)
for Word in Five_Char_Audit:
    print(f'{Word:<10}', end = ' ')
    counter = counter + 1
    if counter == 5:
        print()
        counter = 0
print()
counter = 0
print(f"{'Words Found With 6 Letters:':^51}")
print('-' * 50)
for Word in Six_Char_Audit:
    print(f'{Word:<10}', end = ' ')
    counter = counter + 1
    if counter == 5:
        print()
        counter = 0
print()
counter = 0
print(f"{'Words Found With 7 Letters:':^52}")
print('-' * 52)
for Word in Seven_Char_Audit:
    print(f'{Word:<10}', end = ' ')
    counter = counter + 1
    if counter == 5:
        print()
        counter = 0

# Stage 6:
# Part 1:
print()
Valid = False
while Valid == False:
    audit_letter_pos= input(f'Lets audit the word list with a letter in a specific position.\n'
                        f' What single letter of the alphabet would you like to audit words for?: ').lower()
    if audit_letter_pos in alphabet and len(audit_letter_pos) == 1:
        Valid = True
numbers = '1234567'
Valid = False
while Valid == False:
    audit_num_pos= input(f' What specific position would you like the audit letter to be?: ')
    if audit_num_pos in numbers and len(audit_num_pos) ==1:
        audit_num_pos = int(audit_num_pos)
        Valid = True

#Part 2:
Five_Char_Pos = []
Six_Char_Pos = []
Seven_Char_Pos = []

if audit_num_pos >5:
    print(f'The position is larger then the number of letter in the words found in the 5 Character List.\n'
          f'Moving on to next Character List.')
else:
    for Word in FiveCharList:
        if Word[audit_num_pos - 1] == audit_letter_pos:
            Five_Char_Pos.append(Word)
#print(Five_Char_Pos) #Testing list audit
if audit_num_pos >6:
    print(f'The position is larger then the number of letter in the words found in the 6 Character List.\n'
          f'Moving on to next Character List.')
else:
    for Word in SixCharList:
        if Word[audit_num_pos - 1] == audit_letter_pos:
            Six_Char_Pos.append(Word)
# #print(Six_Char_Pos) Testing list audit
if audit_num_pos >7:
    print(f'The position is larger then the number of letter in the words found in the 7 Character List.\n'
          f'Moving on to next Character List.')
else:
    for Word in SevenCharList:
        if Word[audit_num_pos - 1] == audit_letter_pos:
            Seven_Char_Pos.append(Word)
# #print(Seven_Char_Audit) Testing list audit
# print(f'Auditing the letter {audit_letter} found:\n{len(Five_Char_Audit)} Five letter words\n'
#       f'{len(Six_Char_Audit)} Six letter words\n'
#       f'{len(Seven_Char_Audit)} Seven letter words')

print(f'Auditing the letter {audit_letter_pos} at position {audit_num_pos} found:\n{len(Five_Char_Pos)} Five letter words\n'
      f'{len(Six_Char_Pos)} Six letter words\n'
      f'{len(Seven_Char_Pos)} Seven letter words')

if len(Five_Char_Pos) >0:
    counter = 0
    print(f"{'Words Found With 5 Letters in position ' + str(audit_num_pos):^50}")
    print('-' * 49)
    for Word in Five_Char_Pos:
        print(f'{Word:<10}', end = ' ')
        counter = counter + 1
        if counter == 5:
            print()
            counter = 0

if len(Six_Char_Pos) >0:
    print()
    counter = 0
    print(f"{'Words Found With 6 Letters in position ' + str(audit_num_pos):^51}")
    print('-' * 50)
    for Word in Six_Char_Pos:
        print(f'{Word:<10}', end = ' ')
        counter = counter + 1
        if counter == 5:
            print()
            counter = 0

if len(Seven_Char_Pos) >0:
    print()
    counter = 0
    print(f"{'Words Found With 7 Letters in position ' + str(audit_num_pos):^52}")
    print('-' * 52)
    for Word in Seven_Char_Pos:
        print(f'{Word:<10}', end = ' ')
        counter = counter + 1
        if counter == 5:
            print()
            counter = 0
          
print(f'\nWe have competed our audit of the Words.txt file.')