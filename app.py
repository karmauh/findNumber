'''finding a pseudorandom number in cmd'''

from random import randrange
from os import system
from time import sleep


def randValue():
    n = randrange(firstNumber, secondNumber)
    return n

print("WELCOME~!\nIt's FIND NUMBER GAME")
print('I will think, about number and you have to guess what number it is.')
print('Oh, I almost forgot. You can create numeric range default will be 1 to 100')

'''number rang'''
firstNumber = 1
secondNumber = 100

try:
    firstNumber = int(input('Start:'))
    secondNumber = int(input('End:'))
    print(f'Your numeric range: {firstNumber}-{secondNumber}')
except ValueError:
    print('Your numeric range was not specified so, it will be 1 to 100, as I said before.')
''''''

findMe = randValue()
sleep(1)
system('cls')

'''number to find'''
#print(findMe) 
print("Lets's begin!")
value = int(input('Give me your number:'))

'''checking if player hit the right number'''
i = 1
while True:
    if value == findMe:
        print(f'Congrats! You won in {i} trys')
        break
    else:
        print('try once again...')
        i += 1
        sleep(1)
        system('cls')
        value = int(input(f"That's your {i} try.. Number -> "))
        
    '''checking if player enter too high or too low number'''
    if i >= 0: 
        if findMe-value < 0:
            print('Too BIG..!')
        elif findMe == value:
            pass
        else:
            print('Too small..!')
''''''