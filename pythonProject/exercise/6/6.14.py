import string
import random

resultTurple=(['shitou','jiandao','You Win'],['shitou','bu','You Lose'],['shitou','shitou','Deuce'],
              ['jiandao','shitou','You Lose'],['jiandao','jiandao','Deuce'],['jiandao','bu','You Win'],
              ['bu','shitou','You Win'],['bu','jiandao','You Lose'],['bu','bu','Deuce'])
aList=['shitou','jiandao','bu']

def judgeWin(youChoice,machineChoice):
    for i in range(len(resultTurple)):
        if resultTurple[i][0]==youChoice and resultTurple[i][1]==machineChoice:
            return resultTurple[i][2]

def judgeWinIf(youChoice,machineChoice):
    if youChoice==machineChoice:
        return 'Deuce'
    elif youChoice=='shitou':
        if machineChoice=='jiandao':
            return 'You Win'
        else:
            return 'You Lose'
    elif youChoice=='jiandao':
        if machineChoice=='bu':
            return 'You Win'
        else:
            return 'You Lose'
    elif youChoice=='bu':
        if machineChoice=='shitou':
            return 'You Win'
        else:
            return 'You Lose'


if __name__=='__main__':
    i=0

    dict={"shitou":0,"jiandao":0,"bu":0}
    while True:
        if i<20:
           youChoice=random.choice(aList)
           machineChoice=random.choice(aList)
           #print(youChoice,' & ',machineChoice,',',judgeWin(youChoice,machineChoice))
           # print(youChoice,' & ',machineChoice,',',judgeWinIf(youChoice,machineChoice))

           if youChoice in dict:
               dict[youChoice]+=1
           i+=1

        else:
            print(dict)
            break
