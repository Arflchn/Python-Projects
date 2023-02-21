import emoji
import random
print('\033[1;30;44mJokenpo Game\033[m')
print(emoji.emojize(':page_facing_up: :scissors: :rock:', language='alias'))
r = 'rock'
s = 'scissors'
p = 'paper'
pc_choice = random.choice([r, s, p])
#There's two modes, the fair and unfair
n = int(input('\033[1;30;42mType 1 to play a fair game\033[m \n\033[1;30;41mType 2 to play an unfair game:\033[m '))
if n == 1:
    choice = str(input('What do you choose: rock, scissors or paper? '))
    print(f'I have chosen {pc_choice}')
#Draws results
    if choice == 'rock' and pc_choice == 'rock':
        print('Oh, its a draw.')
    elif choice == 'scissors' and pc_choice == 'scissors':
        print('Well, as I see, its a draw')
    elif choice == 'paper' and pc_choice == 'papper':
        print('A draw with a computer LOL')
#Lose and win results
    elif choice == 'paper' and pc_choice == 'rock':
        print('You won buddy')
    elif choice == 'paper' and pc_choice == 'scissors':
        print('As I see, I WON!!!!')
    elif choice == 'rock' and pc_choice == 'scissors':
        print('Ive lost, can you believe in that?')
    elif choice == 'rock' and pc_choice == 'paper':
        print('You have lost, obviously')
    elif choice == 'scissors' and pc_choice == 'paper':
        print('Were you cheating? How can i lose?')
    elif choice == 'scissors' and pc_choice == 'rock':
        print('And computer wins!!!')
if n == 2:
    choice2 = str(input('What do you choose: rock, scissors or paper? '))
    if choice2 == 'rock':
        print('I have chosen paper')
        print('and of course I won')
    elif choice2 == 'paper':
        print('I have chosen scissors')
        print('COMPUTER WINS!!!')
    elif choice2 == 'scissors':
        print('I have chosen rock')
        print('I win, you lose')
