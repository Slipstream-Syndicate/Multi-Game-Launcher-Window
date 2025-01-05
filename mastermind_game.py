# MASTERMIND GAME

import random
levels=['Easy', 'Hard']
def menu():
    Light='Green'
    while Light=='Green':
        UC=input('Do you wish to continue? [Y/N]')
        try:
            if UC.lower()=='n':
                Light='Red'
                break
        except:
            print('Enter Valid Input')
        for I in levels:
            print(I)
        LC=input('Choose level difficulty  >')
        if LC.lower()=='easy':
            play_e()
        elif LC.lower()=='hard':
            play_h()
def play_e():
    global C
    global T
    Comp_Num=random.randint(1000,10000)
    UG=int(input('Enter Guess of the chosen Computer Number  >'))
    if UG==Comp_Num:
        print('Excellent you guessed it in 1 try! You proved to be a MASTERMIND!')
    else:
        T=0 # number of trials/attempts
        while UG!=Comp_Num:
            T+=1
            C=0 # Number of correctly guessed digits
            UG=str(UG)
            Comp_Num=str(Comp_Num)
            right=['X']*4
            for I in range(0,4):
                if UG[I]==Comp_Num[I]:
                    C+=1
                    right[I]=UG[I]
                else:
                    continue
            if C==0:
                print('None of the numbers match!')
                print('\n'*2)
                UG=int(input('Enter Guess of the chosen Computer Number  >'))
            elif C==4:
                print("You're a mastermind!")
                print('Number of attempts  >', T)
            elif C!=0 and C!=4:
                print('You have guessed', C,'digits correct!')
                print('Your guess status  >')
                for I in right:
                    print(I, end=' ')
                print('\n'*2)
                UG=int(input('Enter Guess of the chosen Computer Number  >'))
def play_h():
    Comp_Num=random.randint(1000,10000)
    UG=int(input('Enter Guess of the chosen Computer Number  >'))
    if UG==Comp_Num:
        print('Excellent you guessed it in 1 try! You proved to be a MASTERMIND!')
    else:
        T=0 # number of trials/attempts
        while UG!=Comp_Num:
            T+=1
            C=0 # Number of correctly guessed digits
            UG=str(UG)
            Comp_Num=str(Comp_Num)
            for I in range(0,4):
                if UG[I]==Comp_Num[I]:
                    C+=1
                else:
                    continue
            if C==0:
                print('None of the numbers match!')
                print('\n'*2)
                UG=int(input('Enter Guess of the chosen Computer Number  >'))
            elif C==4:
                print("You're a mastermind!")
                print('Number of attempts  >', T)
            elif C!=0 and C!=4:
                print('You have guessed', C,'digits correct!')
                UG=int(input('Enter Guess of the chosen Computer Number  >'))        
# --MAIN--           
print('Welcome to MASTERMIND GAME')
print('Can you prove to be a mastermind?')
for I in levels:
    print(I)
LC=input('Choose level difficulty  >')
if LC.lower()=='easy':
    play_e()
elif LC.lower()=='hard':
    play_h()  
menu()

