import random

uwin = 0
Cwin = 0
while True:
    uc=int(input('''
Game Start...
1.Yes
2.No|Exit
'''))
    if uc==1:
        for i in range(1,6):

            while True:
                userinput=int(input('''
1.Rock
2.scissor
3.paper
'''))

                if userinput<=3 and userinput>=1:
                    break
                else:
                    print("invalid input")

            if userinput==1:
                uchoice = "Rock"
            elif userinput==2:
                uchoice = "Scissor"
            elif userinput==3:
                uchoice = "Paper"

            ComputerChoice= random.choice(["Rock","Paper","Scissor"])
            print(uchoice)
            print(ComputerChoice)

            if uchoice==ComputerChoice:
                print('game draw')
                uwin+=1
                Cwin+=1

            elif ((uchoice=='Rock' and ComputerChoice=='Scissor')
                  or (uchoice=='Paper' and ComputerChoice=='Rock')
                  or (uchoice=='Scissor' and ComputerChoice=='Paper')):
                print("uchoice", uchoice)
                print("ComputerChoice", ComputerChoice)
                uwin+=1
            else:
                print("uchoice",uchoice)
                print("ComputerChoice",ComputerChoice)
                Cwin+=1

        if uwin>Cwin:
            print('''
---------------------------------------------------------------------------------
| uwin: | {} |                                                                  |
| Cwin: | {} |                                                                  |
| final: | You Win |                                                           |
---------------------------------------------------------------------------------
'''.format(uwin,Cwin)),
            uwin = 0
            Cwin = 0

        elif Cwin>uwin:
            print('''
---------------------------------------------------------------------------------
| uwin: | {} |                                                                  |
| Cwin: | {} |                                                                  |
| final: | You loose Try One time |                                            |
---------------------------------------------------------------------------------
'''.format(uwin,Cwin))
            uwin = 0
            Cwin = 0
        elif Cwin == uwin:
            print('''
        ---------------------------------------------------------------------------------
        | uwin: | {} |                                                                  |
        | Cwin: | {} |                                                                  |
        | final: | Game is Draw   |                                                    |
        ---------------------------------------------------------------------------------
        '''.format(uwin, Cwin))
            uwin = 0
            Cwin = 0
    elif uc==2:
        break
    else:
        print("invalid input")
        continue
