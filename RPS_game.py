# Rock, Paper, Scissors Game

import random

print('Welcome to Rock, Paper, Scissors Game'.center(170))
print()
Moves=['Rock', 'Paper', 'Scissors']
print('Options:'.center(190))
print()
for I in Moves:
    print(I.center(190))
T=0
# Computer and Player Points
CP=0 
PP=0

def PLAY():
    global CP
    global PP
    Flag='Green'
    while Flag=='Green':
        try:
            Player=input('Play your move >')
            while Player.lower()=='rock' or Player.lower()=='paper' or Player.lower()=='scissors':
                Flag='Red'
                break
            else:
                print('Enter Valid Choice')
        except:
            print('Enter Valid Choice')
    Computer=Moves[random.randint(0,2)]
    print('Computer Plays >', Computer)
    if Computer==Player.title():
        print("Tie!")
    else:
        if Computer=='Rock':
            if Player.lower()=='paper':
                print('You win!', Player, 'wraps', Computer)
                PP+=1
            elif Player.lower()=='scissors':
                print('You Lose!', Computer, 'breaks', Player)
                CP+=1
        elif Computer=='Paper':
            if Player.lower()=='rock':
                print('You Lose!', Computer, 'wraps', Player)
                CP+=1
            elif Player.lower()=='scissors':
                print('You Win!', Player, 'cuts', Computer)
                PP+=1
        elif Computer=='Scissors':
            if Player.lower()=='rock':
                print('You Win!', Player, 'breaks', Computer)
                PP+=1
            elif Player.lower()=='paper': 
                print('You Lose!', Computer, 'cuts', Player)
                CP+=1


Light='Green'
while Light!='Red':
    if T==0:
        print()
        UC=input('Do you want to play? [Y/N] >')
        while UC.lower()=='y' or UC.lower()=='n':
            if UC.lower()=='n':
                Light='Red'
                break
            else:
                PLAY()
                T+=1
                break
        else:
            print('Enter Valid Choice')
    elif T!=0:
        print()
        UC=input('Do you want to continue? [Y/N] >')
        while UC.lower()=='y' or UC.lower()=='n':
            if UC.lower()=='n':
                Light='Red'
                break
            else:
                PLAY()
                T+=1
                break


if Light=='Red' and T!=0:
    print('GAME RESULT:'.center(170))
    if PP>CP:
        print('PLAYER WINS!'.center(170))
        print('PLAYER :'.center(170), PP)
        print('COMPUTER:'.center(170), CP)
    elif CP>PP:
        print('COMPUTER WINS!'.center(170))
        print('PLAYER :'.center(170), PP)
        print('COMPUTER:'.center(170), CP)
    elif CP==PP:
        print('GAME DRAWN'.center(170))
        print('PLAYER :'.center(170), PP)
        print('COMPUTER:'.center(170), CP)
