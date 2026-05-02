'''
Name: Dorian Arcos 
Class: CSEC 1436
Date: May 01,2026
Purpose: Assignment 2 - Menu-based port scanner - Create a menu-based port scanner that reads port numbers
from a file, scans IP addresses from open ports using the socket library, 
and displays, saves, and views the scan results.

English language:
Stage 1:
Display main menu titled "Main Menu".
    Main menu give user two options to select from.
        1: Port Scanning submenu
        2: Exit application
Ask user to choose an option, must be either option 1 or option 2.
If user inputs invalid entry, an error message is given.
User is asked to select option 1 or option 2. 
    This will repeat until user selects a valid option, 1 or 2.
If user selects option 1, display Port Scanning Submenu.
If user selects option 2, program ends.
    goodbye message given
    program ends
When on the main menu screen, the menu will continue to display until the user selects option to the end program.
When user accesses the Port Scanner Submenu, 8 options will be displayed.
    Read Ports from file
    Set Timeout
    Scan IPs from file
    Scan one IP Number
    Display Scan Results
    Save Scan Results
    View Scan Results from File
    Return to Main Menu
Ask user what menu item they would like to select.
If users entry is invalid, an error message is given
    Ask user to select a valid option
If user selects options 1-7
    calls to the selected options function
    function prints testing message
    Return to submenu
If option 8 is selected, return to main menu.
Submenu will continue to display until the user selects option to return to main menu.
Main Menu action repeat for user.

Stage 2:
Create GetPortName function
    uses the port number generated when user selects option 1 to in the Submenu
        uses getservby port to find associated port name
            if name is available, return name to read ports from file function
            if no name is available, return NoName to read ports from file function

When user selects option 1 in the Submenu
    Open PNs.txt file
        if txt file is not found
            print error message
            return to the submenu
    read all port numbers form the file
    store port numbers in a list
    randomly select 100 port numbers from the list and store in PNList
    generate 100 random port numbers between 1 and 65535
        for each of the generated port number
            check if the number already in in PNList
                if not in list, add the PNList
                if already in the list, generate a new port number
        Continue until PNList has all 200 unique port numbers
    Create a dictionary of the port numbers from the list
        use port numbers as keys and names as values
            call GetPortName function pull name of port number
    print all 200 ports in a 15 column table format
        use counter to track columns
        after every 15 ports, start new line
    return to submenu

Stage 3:
Create function for float input used by Timeout function
GetAFloat function ask the user for a valid input in float format.
the function then validates if the input is a float.
    if not a valid float, less then or greater then the min and max values
        error message is given 
            repeats asking for valid input
    if a valid float
    returns a valid float

When a user selects option 2 in the submenu, SetTimeout function is called.
The user is asked for a timeout between 0.1 and 3.0 seconds.
SetTime functions calls GetAFloat function with the min, max, and prompt values.
GetAFloat returns a valid float that is then stored in the global variable TimeOut.

When user selects option 3 from submenu, ScanIPsFromFile is called
    Function validates that option 1 has been completed
        checks port numbers are stored in list.
            if list is empty, error message is given and user is sent back to submenu
            if list has saved port number.
                function continues
    tries to open IPS.txt file.
        If not found
            Error message is given and users is returned to submenu
        if text file is opened
            open in read mode and IP numbers are read and added to the IP Numbers list.
    2 IP numbers are randomly selected from the list and added to another list
    in new list. 
    4 additional random non repeated IP number will be generated and added to IPNumbersList.
    IPlist of 6 unique IP numbers is printed to the screen.
    ScanIPlist function is called with IPList.
        List of IP addresses is passed to be scanned.
        Each IP address in list is scanned on at a time
            every port in PortNumber List is checked to confirm it it is open for IP address.
        While scan is occurring, current IP address and appropriate information will be displayed.
            with each new port scan, printed information will update displayed information
        if a port is found open it is added to a dictonary.
            Keys are IP numbers and values are the list of open ports found, the portname, and timeout value.
        If port os not found open.
            it is skipped.
    User is is taken back to submenu

When user selects option 4 from submenu, ScanOneIPNumber is called.
    function validates that option 1 has been completed
        checks port numbers are stored in list.
            if list is empty, error message is given and user is sent back to submenu
            if list has saved port number.
                function continues
    function ask user for valid IP Address input
        if not valid
            error message is given and question is repeated.
        if valid
            call ScanIPList function with IPadress to scan ports.


Stage 4:
DisplayScanResults function
When a user selects number 5
    check if user has run number 3 first
        is ResultsDnary empty
            if empty print error message and ask user to first run option 3 or 4.
        if not empty
            continue
    Print ResultsDnary in table format on screen.
    then return back to submenu

SaveScanResults function
When a user selects number 6
    check if user has run number 3 first
        is ResultsDnary empty
            if empty print error message and ask user to first run option 3 or 4.
        if not empty
            continue
        Save the printed table to file named ArcosDA02.txt
            If file is not available
                create file 
        print confirmation information has been saved to file
        return to submenu

ViewScanResultsFromFile function
When user selects number 7
    check that user has run number 6
        if ArcosDA02.txt is not found
            print error message asking user to run number 6
        if ArcosDA02.txt is found
            is file empty?
                if empty
                    print error message asking user to run number 6
        if text file is not empty
            print saved table to screen
        return to submenu

    
    



Testing:
Stage 1:
Testing for main menu:
    invalid test inputs:
    0, a, 10, Hello, -1
        Should provide error message and continue asking for valid input
    Valid test inputs:
    1 or 2
        1 should navigate to submenu
        2 should exit program
Testing for Submenu:
    Invalid test inputs:
    0, a, 9, -1
        Should provide error message and continue asking for valid input
    Valid test inputs:
    1,2,3,4,5,6,7,8
        1-7 should provide stage 1 testing message
        8 should return back to main menu
Stage 2:
testing for Read ports in file function
Run Option 2 of Submenu with PNS.txt file removed
    Expected error message displayed and return to submenu
Run Option 2 of Submenu with PNS.txt file present
    200 port table with 15 columns should be displayed

Stage 3    
Float function testing
invalid inputs:
a, -1, 0.0 3.1
valid inputs
.1, 1, .25, 3


Test Timeout function
does global variable update?


Test ScanIPsFromFile function
run with empty PNList
    error code should be given
Move IPS.txt file
    error code should be given
If all is valid 
    IPList of 6 IP address is printed on screen
    scanning progress is displayed on screen
    returned to Submenu

Test ScanOneIPNumber function
run with empty PNList
    error code should be given
Enter invalid IP adress
    abc.def.ghi.jkl
    256.0.0.1
    999.999.999.999
        Error message should be given and user asked for valid IP adress
Enter valid IP address
    192.168.1.1
    8.8.8.8
        IP port scan function is called

Stage 4 testing
Test DisplayScanResults function
    run option 5 without running option 3 or 4 first
        is error message given?
    run option 3 or 4 first then run option 5
        results should be displayed in table format

Test SaveScanResults function
    run option 6 without running option 3 and 4 first
        is error message given?
    run option 3 or 4 first then run option 6
        confirmation message should be displayed
        ArcosDA02.txt file opened or created is not found
        File should contain same table as DisplayScanResults function

Test ViewScanResultsFromFile function
    run option 7 without running option 6 first
        is error message given?
    run option 6 then run option 7
        contents of ArcosDA02.txt should be displayed
        Table should match DisplayScanResults output

 

Pseudocode:
Stage 1:
global variables
Default Timeout value
    Timeout = 0.2

integer input value validation function
    GetAnInt(MinV variable, MaxV variable, Prompt variable)
        check if the prompt value is empty
            if empty keep as an empty string
            if text is included, add 'as' to the end of the text
        While True loop to ask for a valid input
            ask the user for a valid integer between MinV and MaxV integers
                use the prompt in the input question
            Convert input to an integer
                if unable to convert 
                    print error message
                    continue loop to ask for a valid integer input
            confirm if input is equal to or between MinV and MaxV
                if valid
                    break out of loop
                if invalid
                    print error message 
                    continue loop to ask for a valid integer input
        Return the valid input integer

function for menu options
    DisplayMenuAndChoice(MenuTitle variable, menu list variable)
        print MenuTitle
        set a counter starting at 0
        for each item in the MenuList
            increase the counter by 1
            print the counter value and the matching menu item
        Call GetAnInt function (1, max counter value, "your choice")
        Store returned GetAnInt value in MenuChoice variable
        return the list item indexed in [MenuChoice minus 1] 

function for ReadPortsFromFile submenu item
    ReadPortsFromFile()
        print testing message
function for SetTimeout submenu item
    SetTimeout()
        print testing message
function for ScanIPsFromFile submenu item
    ScanIPsFromFile()
        print testing message
function for ScanOneIPNumber submenu item
    ScanOneIPNumber()
        print testing message
function for DisplayScanResults submenu item
    DisplayScanResults()
        print testing message
function for SaveScanResults submenu item
    SaveScanResults()
        print testing message
function for ViewScanResultsFromFile submenu item
    ViewScanResultsFromFile()
        print testing message


function for users choice in Port Scanning Submenu
    SubMenuAction(Chosen)
        Dictionary for MenuActions:{
        'Read Ports from file': ReadPortsFromFile
        'Set Timeout': SetTimeout
        'Scan IPs from file': ScanIPsFromFile
        'Scan one IP Number': ScanOneIPNumber
        'Display Scan Results': DisplayScanResults
        'Save Scan Results': SaveScanResults
        'View Scan Results from File': ViewScanResultsFromFile
        }
    if statement to call function for submenu actions
        if chosen is in MenuActions dictionary
            call the chosen function at MenuAction[chosen]
        

Function for Port Scanning Submenu
    PortScanningMenu()
    create list for SubMenu - 'Read Ports from file', ... (all 8 options)
    start while true loop for submenu
        print line break for formatting
        call DisplayMenuAndChoice function with "Port Scanning Menu" and SubMenu list
        store returned value as Chosen variable
        call SubMenuAction with Chosen variable
        if Chosen is 'Return to Main Menu' 
            break out of while loop
    
        
Function for users input for Main Menu
    MainMenuAction(Chosen)
        if Chosen is 'Port Scanning'
            call PortScanningMenu Function 
        else 
            do nothing and return to main menu function


Start function MainMenu()
    Create list for MainMenuList - 'Port Scanning', 'Exit the Program'
    Start while True loop for main menu
        print line break for formatting
        call DisplayMenuAndChoice With "Main Menu" and MainMenuList list
        store returned variable as Chosen
        call MainMenuAction with Chosen variable
        if Chosen is 'Exit the Program'
            break the while loop
    print closing message

Main function 
    Main()
        call MainMenu function

Stage 2:
Global variables created:
list to hold Port number
    PNList = []
Dictionary for port numbers and names
    PortDnary = {}

create GetPortName function with Port Number input
    GetPortName(PortNumber)
        try to retrieve port name using socket.getservbyport(portnumber, 'tcp')
            if name is available
                return retrieved name
            if no name is available 
                return 'NoName'

create ReadPortFromFile function
When user selects option 1
    Call ReadPortsFromFile()
        try to opens PNs.txt file in read mode
            if file is not found give error and error message
                FileNotFoundError
                print error message
                return to submenu
        read all port number from text file
            store all in ports number list, FilePortsList
            randomly select 100 port number from list using random function
                add selected 100 to PNList
        generate 100 random port numbers between 1 and 65535
            for each of the generated port numbers
                check if they already exist in PNList
                    if not in list, add the PNList
                    if in list, generate new port number
            Continue until PNList has 200 unique ports
        Create dictionary for port numbers and port names
            for each port number in PNList
                call GetPortName function inputting the port number to get port name
                store port numbers as key
                store port names as values
        print all 200 ports in a 15 column table 
            start a counter at 0
            for each port in PNList
                print the port number
                then increase counter by 1
                if the counter equals 15
                    start new line of table
                    reset counter to 0

Stage 3:
Global Variables created:
Dictionary for scan results    
    ResultsDnary = {}

float value validation function
    GetAFloat(MinV variable, MaxV variable, Prompt variable)
        check if the prompt value is empty
            if empty keep as an empty string
            if text is included, add 'as' to the end of the text
        While True loop to ask for a valid input
            ask the user for a valid float between MinV and MaxV floats
                use the prompt in the input question
            Convert input to a float value
                if unable to convert 
                    print error message
                    continue loop to ask for a valid float value input
            confirm if input is equal to or between MinV and MaxV
                if valid
                    break out of loop
                if invalid
                    print error message 
                    continue loop to ask for a valid float input
        Return the valid input float value

create SetTimeout function
When user selects option 2
    call SetTimeout()
    declare Timeout variable as global
    call  GetAFloat function with 0.1, 3.0 and prompt values
        valid float value returned and stored in global Timeout variable
    print confirmation that Timeout has been updated

create ScanIPsFromFile function
    when user selects option 3
    call ScanIPsFromFile()
        Validate PortNumer list is not empty
            if empty
                print error message
                return to submenu
            if not empty
                continue ScanIPsFromFile function
        try to open IPS.txt file in read mode
            if file is not found
                FileNotFoundError
                    print error message
                    return
            if file is found
                read all IP numbers and store in IPNumbersList
            randomly select 2 IP numbers from IPNumersList using random.choice
                store in IPlist
            While the list length is less than 6
                generate a random ip using random.randint
                    first part random.randint(1,255)
                    parts 2,3,and 4 use random.randint(0,255)
                if generated IP is not in IPList
                    add to IPList
            Print IPlist 
            call ScanIPlist function with IPList

Create ScanIPList function this IPList as input
   Call ScanIPList(IPlist)
        For loop goes through each IP address in IPList one at a time
            for each IP address a second loop runs
                second for loop goes through each port in the PNList
                checks each if each port is open for the current IP address
                display current scan status to user on a single line
                    print ip address, port number, port name, and timeout value
                        use \r to overwrite same line with each new scan
                create socket for the connection attempt for ip number
                    use socket.socket with AF_INET for IP protocol
                        use SOCK_STREAM for TCP protocol
                    Store in SocketScan variable
                    set the SocketScan timeout using the Global Timeout variable
                        SocketScan.settimeout(Timeout)
                    try connections to IP address and port
                        use SocketScan.connect_ex((IPAddress, port))
                        store the results in ConnectionResults variable
                        if ConnectionResults == 0
                            port is open
                            If IP address is not in ResultsDnary
                                add IPAddress as key with empty list as value
                            append the port, port name and timeout to ResultsDnary[IPAdress]
                        if ConnectionResults is not 0
                            port is closed, skip
                    Close SocketScan after each port scan
                        SocketScan.close()

create ScanOneIPNumer function
When user selects option 4
    call ScanOneIPNumber()
        Validate PortNumer list is not empty
            if empty
                print error message
                return to submenu
            if not empty
            while true loop to ask use for vaild ip address
                ask the user to enter am IP address
                store IP in IPAddress variable
                try to validate IP address 
                    use socket.inet_aton(IPAddress) to validate 
                    if valid
                        break out of while loop
                    if not valid
                        print error message
                        continue loop
                    except error
                        print error message
                        continue loop
                store IPAdress in a list called IPList
                call ScanIPList function with IPList as input

Stage 4:

create DisplayScanResults function
  When user selects option 5
    call DisplayScanResults()
        validate ResultDnary dictonary is not empty
            if empty
                print error message
                return to submenu
            if not empty
            continue
        print table title
        print table header wit ip address, port number, port name, and timeout
        print '-' separator
        for loop to go through each IPAdress in and OpenPorts in ResultsDnary one at a time
            use .item() to access each IPAdress key and OpenPorts value
            for each IPAdress found, run a second for loop
                for loop goes through each PortEntry in OpenPorts one at a time
                    print IPAddress, PortEntry[0] for port number, PortEntry[1] for port name, and PortEntry[2] for timeout in a table format

        
create SaveScanResults function
When user selects option  6
    Call SaveScanResults()
        Validate ResultDnary dictonary is not empty
            if empty
                print error message
                return to submenu
            if not empty
            continue
        open ArcosDA02.txt file in write mode
            write table title to file
            write table header with IP address, port number, portname, and timeout to file
            write '-' seperator to file
            for loop to go through each IPAdress in and OpenPorts in ResultsDnary one at a time
                use .item() to access each IPAdress key and OpenPorts value
                for each IPAdress found, run a second for loop
                    for loop goes through each PortEntry in OpenPorts one at a time
                        write IPAddress, PortEntry[0] for port number, PortEntry[1] for port name, and PortEntry[2] for timeout in a table format
        close ArcosDA02.txt file
        print confirmation message that result have bee saved to ArcosDA02.txt

create ViewScanResultsFromFile function
when user selects option 7
    call ViewScanResultsFromFile()
    Try to open ArcosDA02
         if not found
            print error message asking user to run option 6
            return to submenu
        if found
            continue
        read all contents from file and store in ScanResultsFile variable
        validate ScanResultFile is not empty
            if empty
                print error message asking user to run option 6
                return to submenu
            if not empty
                print ScanResultsFile to screen
        close ArcosDA02.txt file


'''
import socket #Stage 2
import random #Stage 1

#global variables
#Stage 1
Timeout = 0.2 
#Stage 2
PNList = [] 
PortDnary = {}
#Stage 3
ResultsDnary = {}

def GetAnInt(MinV, MaxV, Prompt):
    '''
    This function is used validate the inputs for the menu and submenu
    and returns the valid input as an integer
    Its inputs are the Minimum value, Maximum value and the text prompt
    of the  menu or submenu list.
    '''
    if Prompt == "":
        Prompt
    else:
        Prompt = Prompt + ' as '
    while True:
        try:
            UserInt = int(input(f'Enter {Prompt}an integer between {MinV} and {MaxV}: '))
            if UserInt >= MinV and UserInt <= MaxV:
                break
            else:
                print(f'Invalid selection.')
                continue
        except ValueError:
            print(f'Invalid selection, not an integer.')
            continue
    return UserInt
#Stage 3
def  GetAFloat(MinV, MaxV, Prompt):
    '''
    This function is used validate float inputs
    and returns the valid input as a float value.
    Its inputs are the Minimum value, Maximum value and the text prompt.
    '''
    if Prompt == "":
        Prompt
    else:
        Prompt = Prompt + ' as '
    while True:
        try:
            UserFlt = float(input(f'Enter {Prompt}a time in seconds between {MinV} and {MaxV}: '))
            if UserFlt >= MinV and UserFlt <= MaxV:
                break
            else:
                print(f'Invalid selection.')
                continue
        except ValueError:
            print(f'Invalid selection, not a valid time entry.')
            continue
    return UserFlt

def DisplayMenuAndChoice(MenuTitle, MenuList):
    '''
    This function displays the main or submenu with the title and numbered options.
    and returns the users selected menu item.
    The inputs are the Menu Title and the List of the Menu options.    
    '''
    print(MenuTitle)
    Counter = 0
    for item in MenuList:
        Counter = Counter + 1
        print(Counter, item)
    MenuChoice= GetAnInt(1, Counter, 'your choice')
    return MenuList[MenuChoice-1]

#Stage 2 GetPortName function
def GetPortName(PortNumber):
    '''
    This function is called to retrieve the name of the given port number
    The input is the port number.
    The output is either the retrieved port name if available or "NoName" if no name is available
    '''
    try:
        PortName = socket.getservbyport(PortNumber, 'tcp')
        return PortName
    except:
        return "NoName"

#stage 3 ScanIPList function
def ScanIPList(IPList):
    '''
    This function is called by ScanIPFromFile function and ScanOneIPNumber function.
    It accepts IPList as the input.
    It scans each IP address in IPList for all port in PNList.
    It displays scan progress on a single line using a carriage return character.
    If a port is found open, it is saved to ResultsDnary dictionary.    
    '''
    global ResultsDnary

    for IPAddress in IPList:                                                                     #empty space left her to ensure new line prints
        for Port in PNList:                                                                    #of shorter lines do not contain remnants of longer line
            print(f'\rScanning IP: {IPAddress} Port: {Port} Port Name: {PortDnary[Port]} Timeout: {Timeout}                    ', end='')
            try:
                SocketScan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                SocketScan.settimeout(Timeout)
                ConnectionResult = SocketScan.connect_ex((IPAddress, Port))
                if ConnectionResult == 0:
                    if IPAddress not in ResultsDnary:
                        ResultsDnary[IPAddress] = []
                    ResultsDnary[IPAddress].append([Port, PortDnary[Port], Timeout])
                SocketScan.close()
            except:
                pass
    print(f'\nScanning Complete')


#stage 2 ReadPortsFromFile function
def ReadPortsFromFile():
    '''
    Stage 1 ---Place holder for stage 1---
    Stage 2 --- This function is called to read the PNs.txt file
    and generate 200 unique ports in a dictionary and print into a 15 column table
    This calls on the GetPortName function providing the port number. 
    The port name is returned and added to the dictionary
    the input is the PNs.txt file and the output is printed table
    '''
    #Stage 1 --- print(f'testing stage 1 Read Ports')
    #stage 2---
    global PortDnary
    global PNList
    try:
        PNsFile = open('PNs.txt', 'r', encoding= 'utf-8')
    except FileNotFoundError:
        print(f'File Not Found')
        return
    FilePortsList = PNsFile.read().strip().split("\n")
    CleanPortsList = []
    for port in FilePortsList:
        if port.strip() != '':
            CleanPortsList.append(port)
    FilePortsList = CleanPortsList
    PNsFile.close()
    while len(PNList) < 100:
        port = int(random.choice(FilePortsList))
        if port not in PNList:
            PNList.append(port)
    while len(PNList) <200:
        port = random.randint(1, 65535)
        if port not in PNList:
            PNList.append(port)
    
    for port in PNList:
        PortName = GetPortName(port)
        PortDnary[port] = PortName
    print(f'\nPort Number Table:') #this is the table for the port numbers
    print('-' * 120)
    Counter = 0
    for port in PNList:
        Counter = Counter + 1
        if Counter == 15:
            print(f"{port:^7}")
            Counter = 0
        else: 
            print(f"{port:^7}", end = '|')

#Stage 3 SetTimeOut function
def SetTimeout():
    '''
    Stage 1 ---Place holder for stage 1---
    Stage 3 --- This function is called when the user selects option 2 from the Submenu.
    It calls the GetAFloat function to ask the user a valid timeout value 
    between 0.1 and 3.0 seconds.
    The validated value is stored in the Global variable Timeout.

    '''
    #Stage 1 print(f'testing stage 1 Timeout')
    #stage 3
    global Timeout
    Timeout = GetAFloat(0.1, 3.0, 'timeout')
    print(f'Timeout is now set to {Timeout} seconds.')

#Stage 3 ScanIPsFromFile
def ScanIPsFromFile():
    '''
    Stage 1---Place holder for stage 1---
    Stage 3---This function is called when the user selects option 3 from the submenu.
    It first validates that PNList is not empty.
    It then opens IPS.txt file to read IP addresses.
    It randomly selects 2 IP addresses from the file and generates 4 more random IPs.
    It then prints the IPList of 6 IP adresses to the screen
    It then calls ScanIPList to scan all IP adresses
    '''
    #Stage 1 print(f'testing stage 1 IP Scan')
    #Stage 3
    global ResultsDnary

    if len(PNList) == 0:
        print(f'Please run Option 1 first to Read Ports From File.')
        return
    try:
        IPFile = open('IPS.txt', 'r', encoding= 'utf-8')
    except FileNotFoundError:
        print(f'File Not Found')
        return
    FileIPList = IPFile.read().strip().split("\n")
    IPNumbersList = []
    for port in FileIPList:
        if port.strip() != '':
            IPNumbersList.append(port)
    FileIPList = IPNumbersList
    IPFile.close()
    IPList = []
    while len(IPList) < 2:
        IP = random.choice(IPNumbersList)
        if IP not in IPList:
            IPList.append(IP)
    while len(IPList) <6:          
        IP = (f'{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}')
        if IP not in IPList:
            IPList.append(IP)
    print(IPList)
    ScanIPList(IPList)
    #print(f'results saved: {ResultsDnary}')
    if len(ResultsDnary) == 0: #used to confim if open ports are found
        print(f'No open ports found for any of the scanned IP addresses.')



#Stage 3 ScanOneIPNumber
def ScanOneIPNumber():
    '''
   Stage 1 --- Place holder for stage 1 ---
   Stage 3 ---This function is called when user selects option 4 from the Submenu.
   It first validates that PNList is not empty.
   It ask the user for one valid IP address.
   It the calls ScanIPList with the IP address to scan all ports.
    '''
    #Stage 1 ---print(f'testing stage 1 One IP Scan')
    #Stage 3---
    global ResultsDnary
    if len(PNList) ==0:
         print(f'Please run Option 1 first to Read Ports From File.')
         return
    while True:
        try:
            IPAddress = input(f'Please enter a valid IP address to scan: ')
            socket.inet_aton(IPAddress)
            break
        except:
            print(f'Invalid IP address. Please try again.')
    IPList = [IPAddress]
    ScanIPList(IPList)
    #print(f'Results: {ResultsDnary}')
    if IPAddress not in ResultsDnary: #used to confim if open ports are found
        print(f'No open ports found for {IPAddress}.')


#Stage 4
def DisplayScanResults():
    '''
    Stage 1 ---Place holder for stage 1---
    Stage 4 --- This function is called when the user selects option 5 from the submenu
    it first validates that ResultDnary dictionary is not empty.
    It then prints the scan results in a table format showing only open ports.
    '''
    #Stage 1 ---print(f'testing stage 1 Display Scan')
    #stage 4 ---
    if len(ResultsDnary) == 0:
        print(f'Please run option 3 or 4 first.')
        return
    else:
        print(f'Scan Results:')
        print(f"{'IP Adress':^20} | {'Port Number':^12} | {'Port Name':^15} | {'Timeout':^10}")
        print('-' * 65)
        for IPAddress, OpenPorts in ResultsDnary.items():
            for PortEntry in OpenPorts:
                print(f'{IPAddress:^20} | {PortEntry[0]:^12} | {PortEntry[1]:^15} | {PortEntry[2]:^10}')



def SaveScanResults():
    '''
    stage 1 ---Place holder for stage 1---
    Stage 4--- This function is called when the user selects option 6 from the submenu.
    It first validates that ResultsDnary is not empty.
    It then saves the scan results to ArcosDA02.txt in a table format showing only open ports.
    It prints a confirmation message when the file has been saved.
    '''
    #stage 1 ---print(f'testing stage 1 Save Scan')
    #Stage 4 ---
    if len(ResultsDnary) == 0:
        print(f'Please run option 3 or 4 first.')
        return
    else:
        ScanFile = open('ArcosDA02.txt', 'w', encoding='utf-8')
        ScanFile.write(f'Scan Results:\n')
        ScanFile.write(f"{'IP Address':^20} | {'Port Number':^12} | {'Port Name':^15} | {'Timeout':^10}\n")
        ScanFile.write('-' * 65 + '\n')
        for IPAddress, OpenPorts in ResultsDnary.items():
            for PortEntry in OpenPorts:
                ScanFile.write(f'{IPAddress:^20} | {PortEntry[0]:^12} | {PortEntry[1]:^15} | {PortEntry[2]:^10}\n')
        ScanFile.close()
        print(f'Scan results have been saved to ArcosDA02.txt')

def ViewScanResultsFromFile():
    '''
    Stage 1 ---Place holder for stage 1---
    Stage 4 --- This function is called when the user selects option 7 from the submenu.
    It opens ArcosDA02.txt and displays the content in a table format.
    If the file is not found or is empty, an error message is given
    '''
    #stage 1 ---print(f'testing stage 1 View Scan')
    #stage 4 ---
    try:
        ScanFile = open('ArcosDA02.txt', 'r', encoding='utf-8')
    except FileNotFoundError:
        print(f'File not found. Please run option 6 first.')
        return
    FileContents = ScanFile.read()
    ScanFile.close()
    if len(FileContents) == 0:
        print(f'File is empty. Please run option 6 first.')
        return
    print(FileContents)

def SubMenuAction(Chosen):
    '''
    This function processes the users choice from the Port Scanning Submenu.
    It uses a dictionary to match the choice of the user to the correct Submenu item/
    Its input is the Chosen option of the user. 
    '''
    MenuActions = {
        'Read Ports from file': ReadPortsFromFile,
        'Set Timeout': SetTimeout,
        'Scan IPs from file': ScanIPsFromFile,
        'Scan one IP Number': ScanOneIPNumber,
        'Display Scan Results': DisplayScanResults,
        'Save Scan Results': SaveScanResults,
        'View Scan Results from File': ViewScanResultsFromFile,
        }
    if Chosen in MenuActions:
        MenuActions[Chosen]()

def PortScanningMenu():
    '''
    This function displays the Sub menu and loops until
    the user selects return to the Main Menu.
    It calls the DisplayMenuAndChoice function to display the menu and get the users choice
    and calls the SubMenuAction function to process the users choice.
    '''
    SubMenu = ['Read Ports from file', 'Set Timeout', 'Scan IPs from file', 'Scan one IP Number', 'Display Scan Results', 'Save Scan Results', 'View Scan Results from File', 'Return to Main Menu']
    while True:
        print()
        Chosen= DisplayMenuAndChoice('Port Scanning Menu', SubMenu)
        SubMenuAction(Chosen)
        if Chosen == 'Return to Main Menu':
            break

def MainMenuAction(Chosen):
    '''
    This function processes the users input choice from the DisplayMenuAndChoice function.
    It checks if the user selected a valid menu item and calls the PortScanningMenu function if selected.
    Its input is Chosen which is the users selected menu item.
    '''
    if Chosen == 'Port Scanning':
        PortScanningMenu()

def MainMenu():
    '''
    This function displays the Main Menu and loops until the user selects the menu option to exit the program.
    It calls DisplayMenuAndChoice function to display the menu and get the users choice input
    and calls MainMenuAction function to process the users choice.    
    '''
    MainMenuList = ['Port Scanning', 'Exit the Program']
    while True:
        print()
        Chosen = DisplayMenuAndChoice('Main Menu', MainMenuList)
        MainMenuAction(Chosen)
        if Chosen == 'Exit the Program':
            break
    print(f'Program has Ended')
  
def main():
    '''
    This is used to begin the program.
    '''
    MainMenu()
   #Stage 2 testing --- ReadPortsFromFile()

main()

