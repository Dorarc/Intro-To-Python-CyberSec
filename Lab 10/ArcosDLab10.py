'''
Name: Dorian Arcos 
Class: CSEC 1436
Date: Mar 26, 2026
Purpose: Lab 10 Assignment - Forensic application: Given a text file(log file) which has line of english text, search the file to see if it has know words. 
If words are found, it will save those words to a different file.

English Language Steps:
1 Open the text file and read it and read entire file as sting the split into lines.
2 Get know words from the user or read from a file or create a list of Know Words.
3 For each word in the know word, check to see if the word is found in the file.
    If word is found, word is saved to another file then stop searching in the remaining file.
    If not, do nothing.
4 Repeat with remaining Know Words.
5 After going through all know words, we will have a file of all found words.

testing:
Run script and provide correct found word log
expected output is if words in the know words list if found in the web text log file, they will be added to a found words log file

Pseudo Code:
Step 1
Create the log file - notepad.exe or notepad++ to create log file and name it appropriately
Must have a valid log file name - ask user for log file name (ith the extension) - same directory as python file
FileContent - read the entire file as a string
Break the string into a list of lines - use the .split method of the string.split('\n')
Split each line into words - separate with .split(' ') to split line into words - will create a list of words
Keep adding the words of each line into a list 
remove the duplicate words using convert to set and back
step 2
Create a list of know words - call it "KnowWordsList.log"
step 3
For each word in know word list 
    is it in wordlist
    if it is add to the foundswords file
Step 4 
repeat step 3 until all word are checked
step 5
create and Open FoundWords.log in write mode
for each word in the foundwords list
    write the word to the log file followed by '\n'
close the log file
print confirmation of completion message

'''
#create the log file 
#log file was created and named "WebText.log"

logfilename = input(f'please enter the logfile name with the extension .log: ')

print(logfilename)
#read file content as a string
filehandle = open(logfilename, 'r', encoding= 'utf-8')
filecontent =  filehandle.read()
#print(f'length is: {len(filecontent)} file content is: {filecontent}')
filehandle.close()

#Break the string into a list of lines - use the .split method of the string.split('\n')
listoflines = filecontent.split('\n')
#print(f'the number of line is: {len(listoflines)}')
# for index, aline in enumerate(listoflines, start=1):
#     print(f'{index}.{aline}')
#Split each line into words - separate with .split(' ') to split line into words - will create a list of words
wordslist = []
for aline in listoflines:
    wordinaline = aline.split(' ') #split the line into words
    for aword in wordinaline:      #for each word in the line
        wordslist.append(aword)    #adding it to the wordlist

#print(f'The number of words is: {len(wordslist)}')
# for index, aword in enumerate(wordslist):
#     print(f'{index}.{aword}')

#remove the duplicate words using convert to set and back

wordslist = list(set(wordslist))
#print(f'The number of unique words is: {len(wordslist)}')
# for index, aword in enumerate(wordslist):
#     print(f'{index}.{aword}')

knowwordlist = ['the','Musk', 'war', 'peace', 'money', 'cyber', 'SpaceX', 'humor', 'Satellite']

# For each word in know word list 
    # is it in wordlist
    # if it is add to the foundswords filest

foundwordlist = []
for aword in knowwordlist:
    if aword in wordslist:
        foundwordlist.append(aword)

# print(f'the number of founds word are: {len(foundwordlist)} They are: ')
# for aword in foundwordlist:
#     print(f'{aword}')
#open the log file that found words will be writen to
wordsfoundlog = open('FoundWords.log', 'w', encoding='utf-8')
for aword in foundwordlist:
    wordsfoundlog.write(aword + '\n') #adds found words to the found words log file
wordsfoundlog.close() #closes found words log file.

print('File scan has been completed. View generated FoundWords.log file to view found words from provided log file.')
#print(f'App has ended')