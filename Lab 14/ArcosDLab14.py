'''
Name: Dorian Arcos 
Class: CSEC 1436
Date: Apr 28,2026
Purpose: Lab 14 Assignment - Chapter 6 "Try It" assessments.
Cinema concession stand under Try it of section 6.1
Updated terms and conditions prompt under Try it of section 6.2
Battle royale game launch under Try it, section 6.3
Curving scores under Try it, section 6.4. Use your own lists and add value
Averaging lists under Try it of section 6.5. Use your own lists
Stream donations under Try it of section 6.6
.
'''
def main():
    #Cinema concession stand under Try it of section 6.1:
    # Define concessions()
    def concessions():
        print('Food/Drink Options:')
        print('Popcorn: $8-10')
        print('Candy: $3-5')
        print('Soft drink: $5-7')

    print('6.1')
    print("Welcome to the cinema.")
    concessions()
    print('-'*45) #empty line for formatting

    #Updated terms and conditions prompt under Try it of section 6.2:
    # Define accepted()
    def accepted():
        print('Thank you for acceptiong the terms.')

    # Define rejected()
    def rejected():
        print('You have rejected the terms. Thank you.')
    # Define terms()
    def terms():
        responce = input('Do you accept the terms and conditions? Y?')
        if responce == 'Y':
            accepted()
        else:
            rejected()
    print('6.2')
    terms()
    print('-'*45) #empty line for formatting

    #Battle royale game launch under Try it, section 6.3
    def find_teammates(num):
        print("Finding", num, "players...")

    # Define battle_royale() and practice()
        def battle_royal():
            playernums = int(input("how many player in party?"))
            need = 3 - playernums
            find_teammates(need)
            print('Match starting...')

    def practice():
        map = input('Which map do you want to use? ')
        print('Launching practice on', map)

    print('6.3')
    game_mode = input('input info: ')
    if game_mode == 'br':
        battle_royal()
    else:
        practice()
    # Launch selected game mode
    print('-'*45) #empty line for formatting

    #Curving scores under Try it, section 6.4. Use your own lists and add value
    # Define print_scores()
    def print_scores(scores, add):
        for score in scores:
            print(score, 'would be updated to', score + add)
    print('6.4')
    print_scores([12, 56, 3, 89, 12], 5)
    print() # Print newline
    print_scores([50, 11, 44, 45, 75], 15)
    print('-'*45) #empty line for formatting

    #Averaging lists under Try it of section 6.5. Use your own lists
    # Define avg_list()
    def avg_list(avg_sum):
        sum = 0
        count = 0
        for num in avg_sum:
            sum += num
            count += 1
        return sum/count
            

    print('6.5')
    list1 = [12, 3, 5, 38, 66, 100]
    print(list1)
    print(f"Avg is: {avg_list(list1):.1f}")
    list2 = [6, 1, 55, 75, 32]
    print(list2)
    print(f"Avg is: {avg_list(list2):.1f}")
    print('-'*45) #empty line for formatting

    #Stream donations under Try it of section 6.6
    def donate(amount=5, name='Anonymous', msg=''):
        print(name, 'donated', amount, 'credits:', msg)
    print('6.6')
    donate()
    donate(25, 'Dorian', 'GG!')
    donate(100, msg='You suck at this game \U0001F923 ', name='Ludwig')

main()