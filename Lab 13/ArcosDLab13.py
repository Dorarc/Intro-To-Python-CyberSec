'''
Name: Dorian Arcos 
Class: CSEC 1436
Date: Apr 21,2026
Purpose:Create a very large data set of searchable data set (dictionaries) of fiels fromtelnumber, fromfirstname, fromlastname, totelnum, tofirstname, tolastname
    given a file of first names, and a files of lastnames
Purpose for Lab 13: Create a large set of records the include the above fields plus a state and zip code field. 
    The program should pick random create records with random state name from the provided state zip code webpage.
    The program should then create random valid zip code for each record based on the state randomly selected.
    The program should ask the user for the total number of records to create, and create that many records.
    The first 10 records will be displayed in a neat table format
    User will then be allowed to search for a valid zip code from a state and then asked for a name to search in the generated records that has the matching zip code.
    The results will be printed in a neat table format.
    The program will then ask the use for the log file name.
    With the valid log file name, the program with write the two generated tables into the log file with the same formatting as the console output.

English Language:
Ask user for number of records
open and read the firstnames
Open and read the lastnames
randomly pick a name from firstname and a name from lastnames to create a random fromfirstname and fromlastname
Randomly pick a name from firstname and a name from lastname to create a random tofirstname and tolastname
Create a random from phone number
create a random tophonenumber
accumulate this set of data into a dictionary
repeat steps 3 through 7 for the number of records we need.

Stage 1:Zip Code Dictionary
Create a Zip Code Dictionary called ZipDict
    Each key is the abbreviation of the state 
    Each Value is a list containing  the Name of the state, the Minimum Zip Code, and the Maximum zip code
Stage 2:
Pick a random state abbreviation form ZipDict
Use random abbreviation to look up state name
    Use index position
Use random abbreviation to look up minimum zip number
    Use index position
Use random abbreviation to look up maximum zip number
    Use index position
Generate a random zip from min and max zip codes
    Use zfill to ensure numbers are 5 digits long
Add zip code and state name to ValueList dictionary

Stage 3:
Count number of records to display
    If the the number of records is more then 10
        then display 10
    if less
        display that amount
Print a tile for table of 10 generated records 
Print a header with each value as column titles
print a separator
use a loop to print each record onto separate line
    use formatting to ensure each field is in correct position

Stage 4:
Ask user for a valid Zip Code zip code
Validate if zip code is a valid state zip code
Use loop through each state zip code range
        If users zip code falls state valid range, save the state name
        If users zip code does not fall in a valid range, try next states range
    If not state range match is found, users zip code is invalid
        keep asking until valid zip code is given
Print name of state validzip code belong to

Stage 5:
Ask the user for a name to search for in the created records
search the records
    Name should be found in FromFName, FromLName, ToFName, or ToLName
    Zip code of found name needs to match zip code entered in stage 4 by the user
        Ensure case insensitivity
    If a match is not found, repeat input question until a match is found
When match is found, display the records found in a neat table format
    
Stage 6:
Open a log file to write the tabulated records from stage 5 into.
    ask the user for the name ArcosDLab13.log as default.
        If invalid print file not found message and repeat asking for name until a valid name, ArcosDLab13.log is given
Write the tabulated records into the log file with same formatting as displayed in console.
    Log file will contain first 10 records from stage 3 and name search results from stage 5
close log file
end with closing message


Testing:
Stage 1:
Add test prints to confirm proper entries
    print(ZipDict['AL'])
    print(ZipDict['TX'])
    print(ZipDict['NY'])
Run code
    Does the state Texas generate a valid zip code? 
    Does the state New York generate a valid zip code?
Stage 2:
Add test print for random abbreviation
Add test print for look up of state name
Add test print for look up of min zip
Add test print for look up of max zip
Add test print for generated random zip
Add print of ValuesList
Run Code
    Does the state abbreviation print?
    Does the state name print?
    Does the min zip print?
    Does the max zip print?
    Does the random zip print with correct number of digits?
    Does ValuesList show the correct entries?
Stage 3:
Run Code
    Test with 5 records
        does the table show 5 records?
    Test with 10 records
        Does table show 10 records?
    Test with 100 records
        Does table Show 10 records?
    Does generated table display proper formatting
        Are columns aligned properly?
Stage 4:
Run code
    Test invalid zip code:
        00001, 01, 1
        Does code keep asking for valid zip code?
    Test valid zip codes:
        78249(TX), 07010(NJ), 00781(NY)
        Does code print name of state?
Stage 5:
Test case insensitivity of name, substring matching, and zip code matching
    Search for Name from previously generated record table.
        Use different cases for the name.
    Does the search find results?
    Are results in a table format?
Test no matches
    zzz
    does program handle no matches found?
Stage 6:
Run code
    test with invalid file name
        thisisatest.log
            Does code keep asking for valid file name?
    Test with valid file name
        ArcosDLab13.log
    Test by using enter for default name
        Does the log file get created with the correct name?
Does log file match the console output for stage 3 and stage 5?

Pseudo code:
Maxrecordcount - ask user for number for records to create 
Design of the dictionary is teldnary:
What should dictonary look lijke?
{key : Valule, key, valiue}
Key is an index nuber integer that begins with 1 and goes for the number of records
Value: list which has the fromtelnum, fromfname, fromlname, totelnum, tofirstname, tolastname

count of records = 0
Fnamelist reading the first names from the file (ask user for name or default to fnames.txt) into list
lnameslist - reading the last names for the file (ask user for name or default to lnames.txt)
While True (keep repeating):
    Fromname - randomly picked firstname from fnameslist
    Fromname - randomly picked Lastname from lnameslist
    Tofname - randomly pick firstname from fnameslist
    Tolname - randomly pick lastname from lnameslist
    Fromtelnum - generate a random tel number - format xxx-yyy-zzzz
    Totelnum - generate a random tel number - format xxx-yyy-zzzz
    increment the count
    create the list of all the items
    add record to dictionary designed as above - teldnary[count] = listof items
    if count has reached limit of records needed - break out of the loop

Stage 1: Zip Code Dictionary
Create a dictionary called ZipDict
    Create entries for each state
        Key = abbreviation
        Value = full name, min zip - max zip
    ZipDic = {
    'AL':['Alabama', 35004, 36925]
    'TX':['Texas', 73301, 88595]
    'NY':['New York', 501, 14925] 
    ...    
    }
Stage 2:
Into the RecordCount for loop add:
    RandomState variable for selecting a random state abbreviation
    StateName variable for random state name 
    MinZip variable for the random minimum zip code 
    MaxZip variable for the random maximum zip code
    Use MinZip and MaxZip to generate a random zip code with in states range
        use zfill to ensure generated zip has 5 digits
    Add the state abbreviation, name, and randomly generated zip to the ValuesList dictionary

Stage 3:
Determine the number of records to display
    if length of TelDnary is more then 10
        set the number of rows to display to 10
            RowCount = 10
    else
        set to number to records generated
Print the title of the table
print the header with each value spaced out with formatting
Print separator line
Begin printing table rows
    Use for loop
        for each record from RowCount
            Print each field from TelDnary
            use formatting to align columns 

Stage 4:
Ask the user for a Valid Zip code from any state
use a while True loop
   Ask for a valid zip code, Store as a string
   convert users input to an integer to compare to valid state zip codes
   Loop through ZipDict using .items 
        for each of the state abbreviations, key, and state information, the values
            if the users input is in the valid state zip codes
                save the state name
                break the loop
    If no match is found
        Repeat asking user for a valid zip code and repeat search of ZipDict until valid zip is found
Print the name of the State from the valid zip code

Stage 5:
Ask the user for a name substring
    Store as variable NameSearch
    Use lower() to store input name in lowercase for case insensitivity
Create an empty list to store matching records found
Loop through TelDnary using .items()
    For each of the records keys and values
        Check if the zip codes in records match users provided zipcode
            If zip code does not match, skip to the next record
            If zip code does match, check if the users input name matches the 4 name fields of the record
            If name match is found, add record to results list
If no match is found, display a message indicating this.
Once all records are searched, print the results in a neat table format

Stage 6:
While true loop to ask user for log file name
    try
        if user selects enter for default, set file name to ArcosDLab13.log
        if user manually enters ArcosDLab13.log, accept this as file name
        if user enters invalid file name
            print error message, file not found and continuously ask for file name until valid name is given 
open the log file in write mode
write the same table of records from stage 3 into the log file
write the same table of records from stage 5 into the log file
close the log file
print closing message for program
'''

import random#makesure the lnames.txt and fnames.txt is in the directory
#read the fnames file
TelDnary = {} #master telephone dictionary

#Stage 1 Dictionary:
ZipDict = {
    #WY must come before TX - discovered during testing that zip 82372
    #was returning Texas instead of Wyoming
    'WY':['Wyoming',        82001, 83128],
    #remaining states in alphabetical order
    'AL':['Alabama',        35004, 36925],
    'AK':['Alaska',         99501, 99950],
    'AZ':['Arizona',        85001, 86556],
    'AR':['Arkansas',       71601, 72959],
    'CA':['California',     90001, 96162],
    'CO':['Colorado',       80001, 81658],
    'CT':['Connecticut',     6001,  6928],
    'DE':['Delaware',       19701, 19980],
    'FL':['Florida',        32003, 34997],
    'GA':['Georgia',        30002, 39901],
    'HI':['Hawaii',         96701, 96898],
    'ID':['Idaho',          83201, 83888],
    'IL':['Illinois',       60001, 62999],
    'IN':['Indiana',        46001, 47997],
    'IA':['Iowa',           50001, 52809],
    'KS':['Kansas',         66002, 67954],
    'KY':['Kentucky',       40003, 42788],
    'LA':['Louisiana',      70001, 71497],
    'ME':['Maine',           3901,  4992],
    'MD':['Maryland',       20601, 21930],
    'MA':['Massachusetts',   1001,  5544],
    'MI':['Michigan',       48001, 49971],
    'MN':['Minnesota',      55001, 56763],
    'MS':['Mississippi',    38601, 39776],
    'MO':['Missouri',       63001, 65899],
    'MT':['Montana',        59001, 59937],
    'NE':['Nebraska',       68001, 69367],
    'NV':['Nevada',         88901, 89883],
    'NH':['New Hampshire',   3031,  3897],
    'NJ':['New Jersey',      7001,  8989],
    'NM':['New Mexico',     87001, 88441],
    'NC':['North Carolina', 27006, 28909],
    'ND':['North Dakota',   58001, 58856],
    'OH':['Ohio',           43001, 45999],
    'OK':['Oklahoma',       73001, 74966],
    'OR':['Oregon',         97001, 97920],
    'PA':['Pennsylvania',   15001, 19640],
    'RI':['Rhode Island',    2801,  2940],
    'SC':['South Carolina', 29001, 29945],
    'SD':['South Dakota',   57001, 57799],
    'TN':['Tennessee',      37010, 38589],
    'TX':['Texas',          73301, 88595],
    'UT':['Utah',           84001, 84791],
    'VA':['Virginia',       20101, 24658],
    'VT':['Vermont',         5001,  5907],
    'WA':['Washington',     98001, 99403],
    'WV':['West Virginia',  24701, 26886],
    'WI':['Wisconsin',      53001, 54990],
    #NY listed last, unusually wide range starting at 00501
    #listed last so smaller northeastern states match first
    'NY':['New York',         501, 14925],
}
while True:
    try:
        FNamesFile = input('Please enter the name of file which has first names (press enter for Fnames.txt as default): ')
        #print(f'{fnamesfile})
        if FNamesFile.strip() == "":
            FNamesFile= 'Fnames.txt'
        FNamesFileVar = open(FNamesFile, 'r', encoding= 'utf-8')
        break
    except FileNotFoundError:
        print (f'{FNamesFile} File not found. Please reenter correct name.')
FNamesList = FNamesFileVar.read().strip().split("\n") #read as string, remove beginning or trailing blank lines and split the line 
print(f'The number of first names are: {len(FNamesList)}')
    #for index in range (10)
        #print (f'{fnameslist[index]}')
    #read the lnames file
while True:
    try: 
        LNamesFile = input('Please enter the name of file which has last names (Press enter for Lnames.txt as default): ')
        #print(f'{LNamesFile}')
        if LNamesFile.strip() == '':
            LNamesFile= 'Lnames.txt'
        LNamesFileVar = open(LNamesFile, 'r', encoding= 'utf-8')
        break
    except FileNotFoundError:
        print (f'{LNamesFile} File not found. Please reenter correct name')
LNamesList = LNamesFileVar.read().strip().split('\n') #read as string, remove beginning or trailing blank lines and split the lines
print(f'The number of last names are: {len(LNamesList)}')
# for index in range (10):
#     print(f'{lnamelist[index]}')
while True: #updated to use Lab13 minimum of 10 requirement as directed by instructor
    try:
        MaxRecordsCount = (input('Please enter the integer greater than 9 to create that of records (Press enter for 10 as default): '))
        if MaxRecordsCount.strip() == '':
            MaxRecordsCount = 10
            break
        MaxRecordsCount = int(MaxRecordsCount)
        if MaxRecordsCount > 9:
            break
    except ValueError:
        pass
for RecordCount in range (1, MaxRecordsCount+1):
    #create one record
    #fromfname - randomy picked firstname from fnamelist
    FromFName = random.choice(FNamesList)
    #fromlname -randomly pikced lastname from lnamelist
    FromLName = random.choice(LNamesList)
    #print (f'{fromfname} {fromlname})
    # tofname - randomly picked firstname from fnameslist
    ToFName = random.choice(FNamesList)
    #tolname - randomly picked lastname from lnameslist
    ToLName = random.choice(LNamesList)
    #print(f'{tofname}{tolname})
    #fromtelnum - generate a random tel number - format xxx-yyy-zzzz
    FromTelNum = f'{random.randint(100,999)}-{str(random.randint(0,999)).zfill(3)}-{str(random.randint(0,9999)).zfill(4)}'
    #print (f'{fromtalnum})
    #totelnum - generate a random tel number - format xxx-yyy-zzz
    TotelNum = f'{random.randint(100,999)}-{str(random.randint(0,999)).zfill(3)}-{str(random.randint(0,9999)).zfill(4)}'

#Stage 2:
    RandomState = random.choice(list(ZipDict.keys()))
    StateName = ZipDict[RandomState][0]
    MinZip = ZipDict[RandomState][1]
    MaxZip = ZipDict[RandomState][2]
    RandomZip = str(random.randint(MinZip,MaxZip)).zfill(5)
    #ValuesList = [FromTelNum, FromFName, FromLName, TotelNum, ToFName, ToLName]

#Stage 2 Updated ValuesList:
    ValuesList = [FromTelNum, FromFName, FromLName, TotelNum, ToFName, ToLName, RandomState, StateName, RandomZip]
    # Stage 2 Testing:
    # print(RandomState)
    # print(StateName)
    # print(MinZip)
    # print(MaxZip)
    # print(RandomZip)
    # print(ValuesList)

    TelDnary[RecordCount] = ValuesList
    #print (f'{teldnary}')
print(f'The number of records created are: {len(TelDnary)}')
#for k,v in teldnary.items():
    #print(f'{k}:{v}')
print(f'teldnary creation fun ended')

#Stage 1:
print(f'\nStart of lab 13')

#testing
# print(ZipDict['AL'])
# print(ZipDict['TX'])
# print(ZipDict['NY'])

#Stage 3:
if len(TelDnary) >= 10:
    RowCount = 10
else:
    RowCount = len(TelDnary)
print(f'Table of Records:')
print(f"{'Number From':^12} | {'First Name From':^15} | {'Last Name From':^14} | {'Number To':^12} | {'First Name To':^13} | {'Last Name To':^13} | {'ST':^2} | {'State Name':^14} | {'Zip Code'}")
print('-' * 127)
for Rows in range (1, RowCount+1):
    print(f"{TelDnary[Rows][0]:^12} | {TelDnary[Rows][1]:^15} | {TelDnary[Rows][2]:^14} | {TelDnary[Rows][3]:^12} | {TelDnary[Rows][4]:^13} | {TelDnary[Rows][5]:^13} | {TelDnary[Rows][6]:^2} | {TelDnary[Rows][7]:^14} | {TelDnary[Rows][8]:^8}")

#Stage 4:
while True: 
    try:
        UserZip = (input('Please enter a valid zip code from a state in the USA: '))
        UserZip = int(UserZip)
        for StateAbbr, StateValues in ZipDict.items():
            if UserZip >= StateValues[1] and UserZip <= StateValues[2]:
                Foundstate = StateValues[0]
                break
        else:
            continue
        print(f'This zip code belongs the state of {Foundstate}')
        break
    except ValueError:
            
            pass
#Stage 5:
while True:
    Namesearch = input(f'Enter a name to search for in created records: ').lower()  
    MatchList = []
    for RecordedKey, RecordedValues in TelDnary.items():
        if RecordedValues[8] == str(UserZip).zfill(5):
            if Namesearch in RecordedValues[1].lower() or Namesearch in RecordedValues[2].lower() or Namesearch in RecordedValues[4].lower() or Namesearch in RecordedValues[5].lower():
                MatchList.append(RecordedValues)
    if len(MatchList) == 0:
        continue
    else:
        print(f'Matching Records:')
        print(f"{'Number From':^12} | {'First Name From':^15} | {'Last Name From':^14} | {'Number To':^12} | {'First Name To':^13} | {'Last Name To':^13} | {'ST':^2} | {'State Name':^14} | {'Zip Code'}")
        print('-' * 127)
        for Record in MatchList:
            print(f'{Record[0]:^12} | {Record[1]:^15} | {Record[2]:^14} | {Record[3]:^12} | {Record[4]:^13} | {Record[5]:^13} | {Record[6]:^2} | {Record[7]:^14} | {Record[8]:^8}')
        break
while True:
        LogFile = input('Please enter the name of Log File, ArcosDLab13.log (press enter for ArcosDLab13.log as default): ')
        #print(f'{LogFile})
        if LogFile.strip() == "":
            LogFile= 'ArcosDLab13.log'
        if LogFile != 'ArcosDLab13.log':
            print (f'{LogFile} File not found. Please enter the name of Log File, ArcosDLab13.log (press enter for ArcosDLab13.log as default): ')
            continue
        LogFileFinal = open(LogFile, 'w', encoding= 'utf-8')
        break
#test code to confirm log file is created with proper name

LogFileFinal.write(f'Table of Records:\n')
LogFileFinal.write(f"{'Number From':^12} | {'First Name From':^15} | {'Last Name From':^14} | {'Number To':^12} | {'First Name To':^13} | {'Last Name To':^13} | {'ST':^2} | {'State Name':^14} | {'Zip Code'}\n")
LogFileFinal.write('-' * 127 + '\n')
for Rows in range (1, RowCount+1):
    LogFileFinal.write(f"{TelDnary[Rows][0]:^12} | {TelDnary[Rows][1]:^15} | {TelDnary[Rows][2]:^14} | {TelDnary[Rows][3]:^12} | {TelDnary[Rows][4]:^13} | {TelDnary[Rows][5]:^13} | {TelDnary[Rows][6]:^2} | {TelDnary[Rows][7]:^14} | {TelDnary[Rows][8]:^8}\n")
#test code to confirm first table is propely written to log file 
LogFileFinal.write(f'Matching Records:\n')
LogFileFinal.write(f"{'Number From':^12} | {'First Name From':^15} | {'Last Name From':^14} | {'Number To':^12} | {'First Name To':^13} | {'Last Name To':^13} | {'ST':^2} | {'State Name':^14} | {'Zip Code'}\n")
LogFileFinal.write('-' * 127 + '\n')
for Record in MatchList:
    LogFileFinal.write(f'{Record[0]:^12} | {Record[1]:^15} | {Record[2]:^14} | {Record[3]:^12} | {Record[4]:^13} | {Record[5]:^13} | {Record[6]:^2} | {Record[7]:^14} | {Record[8]:^8}\n')
LogFileFinal.close()
print(f'Log file {LogFile} has been created with the tabulated information written to it. End of Lab 13.')
        

