import sys, os
from random import randint

x1y1 = 0
x2y1 = 0
x3y1 = 0
x1y2 = 0
x2y2 = 0
x3y2 = 0
x1y3 = 0
x2y3 = 0
x3y3 = 0

T = False
P1 = 0
P2 = 0
B = False
player_name = input('player name = ')
bot_name = input('bot name = ')
print ('Easy(1) or normal(2) or hard(3) or impossible(4)')
raskus = int(input('>>>   '))
R = 0
if raskus == 1:
    R = randint(1, 8)
    pass
if raskus == 2:
    R = randint(1, 4)
    pass
if raskus == 3:
    R = randint(1, 2)
    pass
if raskus > 4:
    print ('ERROR')
    print ('vale raskus astme ID')
    print ('aborting')
    sys.exit()

def draw():
    global x1y1, x2y1, x3y1, x1y2, x2y2, x3y2, x1y3, x2y3, x3y3, P1, P2, B
    A = 1
    Y1 = []
    Y2 = []
    Y3 = []
    for _ in range(9):
        if A == 1:
            if x1y1 == 0:
                Y1.append('   |')
                A += 1
            elif x1y1 == 1:
                Y1.append(' x |')
                A += 1
            elif x1y1 == 2:
                Y1.append(' o |')
                A += 1
        elif A == 2:
            if x2y1 == 0:
                Y1.append('   |')
                A += 1
            elif x2y1 == 1:
                Y1.append(' x |')
                A += 1
            elif x2y1 == 2:
                Y1.append(' o |')
                A += 1
        elif A == 3:
            if x3y1 == 0:
                Y1.append('   ')
                A += 1
            elif x3y1 == 1:
                Y1.append(' x ')
                A += 1
            elif x3y1 == 2:
                Y1.append(' o ')
                A += 1
        elif A == 4:
            if x1y2 == 0:
                Y2.append('   |')
                A += 1
            elif x1y2 == 1:
                Y2.append(' x |')
                A += 1
            elif x1y2 == 2:
                Y2.append(' o |')
                A += 1
        elif A == 5:
            if x2y2 == 0:
                Y2.append('   |')
                A += 1
            elif x2y2 == 1:
                Y2.append(' x |')
                A += 1
            elif x2y2 == 2:
                Y2.append(' o |')
                A += 1
        elif A == 6:
            if x3y2 == 0:
                Y2.append('   ')
                A += 1
            elif x3y2 == 1:
                Y2.append(' x ')
                A += 1
            elif x3y2 == 2:
                Y2.append(' o ')
                A += 1
        elif A == 7:
            if x1y3 == 0:
                Y3.append('   |')
                A += 1
            elif x1y3 == 1:
                Y3.append(' x |')
                A += 1
            elif x1y3 == 2:
                Y3.append(' o |')
                A += 1
        elif A == 8:
            if x2y3 == 0:
                Y3.append('   |')
                A += 1
            elif x2y3 == 1:
                Y3.append(' x |')
                A += 1
            elif x2y3 == 2:
                Y3.append(' o |')
                A += 1
        elif A == 9:
            if x3y3 == 0:
                Y3.append('   ')
                A += 1
            elif x3y3 == 1:
                Y3.append(' x ')
                A += 1
            elif x3y3 == 2:
                Y3.append(' o ')
                A += 1
    
    os.system('cls')
    sep = ''
    print (sep.join(Y1))
    print ('-----------')
    print (sep.join(Y2))
    print ('-----------')
    print (sep.join(Y3))
    if not B:
        P1 += 1
        if P1 >= 3:
            B = True
            check()
        B = True
        control()
    elif B:
        P2 += 1
        if P2 >= 3:
            B = False
            check()
        B = False
        control()

def control():
    global T, x1y1, x2y1, x3y1, x1y2, x2y2, x3y2, x1y3, x2y3, x3y3, raskus, R
    
    if not T:
        y = input('Y = ')
        if y == ('1'):
            x = input('X = ')
            if x == ('1'):
                if x1y1 > 0:
                    control()
                x1y1 = 1
                T = True
                draw()
            elif x == ('2'):
                if x2y1 > 0:
                    control()
                x2y1 = 1
                T = True
                draw()
            elif x == ('3'):
                if x3y1 > 0:
                    control()
                x3y1 = 1
                T = True
                draw()
            while x not in ['1', '2', '3']:
                print ('please enter a valid command')
                x = input('X = ')
                if x == ('1'):
                    if x1y1 > 0:
                        control()
                    x1y1 = 1
                    T = True
                    draw()
                elif x == ('2'):
                    if x2y1 > 0:
                        control()
                    x2y1 = 1
                    T = True
                    draw()
                elif x == ('3'):
                    if x3y1 > 0:
                        control()
                    x3y1 = 1
                    T = True
                    draw()
        elif y == ('2'):
            x = input('X = ')
            if x == ('1'):
                if x1y2 > 0:
                    control()
                x1y2 = 1
                T = True
                draw()
            elif x == ('2'):
                if x2y2 > 0:
                    control()
                x2y2 = 1
                T = True
                draw()
            elif x == ('3'):
                if x3y2 > 0:
                    control()
                x3y2 = 1
                T = True
                draw()
            while x not in ['1', '2', '3']:
                print ('please enter a valid command')
                x = input('X = ')
                if x == ('1'):
                    if x1y2 > 0:
                        control()
                    x1y2 = 1
                    T = True
                    draw()
                elif x == ('2'):
                    if x2y2 > 0:
                        control()
                    x2y2 = 1
                    T = True
                    draw()
                elif x == ('3'):
                    if x3y2 > 0:
                        control()
                    x3y2 = 1
                    T = True
                    draw()
        elif y == ('3'):
            x = input('X = ')
            if x == ('1'):
                if x1y3 > 0:
                    control()
                x1y3 = 1
                T = True
                draw()
            elif x == ('2'):
                if x2y3 > 0:
                    control()
                x2y3 = 1
                T = True
                draw()
            elif x == ('3'):
                if x3y3 > 0:
                    control()
                x3y3 = 1
                T = True
                draw()
            while x not in ['1', '2', '3']:
                print ('please enter a valid command')
                x = input('X = ')
                if x == ('1'):
                    if x1y3 > 0:
                        control()
                    x1y3 = 1
                    T = True
                    draw()
                elif x == ('2'):
                    if x2y3 > 0:
                        control()
                    x2y3 = 1
                    T = True
                    draw()
                elif x == ('3'):
                    if x3y3 > 0:
                        control()
                    x3y3 = 1
                    T = True
                    draw()
        while y not in ['1', '2', '3']:
            print ('please enter a valid command')
            y = input('Y = ')
            if y == ('1'):
                x = input('X = ')
                if x == ('1'):
                    if x1y1 > 0:
                        control()
                    x1y1 = 1
                    T = True
                    draw()
                elif x == ('2'):
                    if x2y1 > 0:
                        control()
                    x2y1 = 1
                    T = True
                    draw()
                elif x == ('3'):
                    if x3y1 > 0:
                        control()
                    x3y1 = 1
                    T = True
                    draw()
                while x not in ['1', '2', '3']:
                    print ('please enter a valid command')
                    x = input('X = ')
                    if x == ('1'):
                        if x1y1 > 0:
                            control()
                        x1y1 = 1
                        T = True
                        draw()
                    elif x == ('2'):
                        if x2y1 > 0:
                            control()
                        x2y1 = 1
                        T = True
                        draw()
                    elif x == ('3'):
                        if x3y1 > 0:
                            control()
                        x3y1 = 1
                        T = True
                        draw()
            elif y == ('2'):
                x = input('X = ')
                if x == ('1'):
                    if x1y2 > 0:
                        control()
                    x1y2 = 1
                    T = True
                    draw()
                elif x == ('2'):
                    if x2y2 > 0:
                        control()
                    x2y2 = 1
                    T = True
                    draw()
                elif x == ('3'):
                    if x3y2 > 0:
                        control()
                    x3y2 = 1
                    T = True
                    draw()
                while x not in ['1', '2', '3']:
                    print ('please enter a valid command')
                    x = input('X = ')
                    if x == ('1'):
                        if x1y2 > 0:
                            control()
                        x1y2 = 1
                        T = True
                        draw()
                    elif x == ('2'):
                        if x2y2 > 0:
                            control()
                        x2y2 = 1
                        T = True
                        draw()
                    elif x == ('3'):
                        if x3y2 > 0:
                            control()
                        x3y2 = 1
                        T = True
                        draw()
            elif y == ('3'):
                x = input('X = ')
                if x == ('1'):
                    if x1y3 > 0:
                        control()
                    x1y3 = 1
                    T = True
                    draw()
                elif x == ('2'):
                    if x2y3 > 0:
                        control()
                    x2y3 = 1
                    T = True
                    draw()
                elif x == ('3'):
                    if x3y3 > 0:
                        control()
                    x3y3 = 1
                    T = True
                    draw()
                while x not in ['1', '2', '3']:
                    print ('please enter a valid command')
                    x = input('X = ')
                    if x == ('1'):
                        if x1y3 > 0:
                            control()
                        x1y3 = 1
                        T = True
                        draw()
                    elif x == ('2'):
                        if x2y3 > 0:
                            control()
                        x2y3 = 1
                        T = True
                        draw()
                    elif x == ('3'):
                        if x3y3 > 0:
                            control()
                        x3y3 = 1
                        T = True
                        draw()
    if T:
        if raskus == 1:
            if R == 1:
                if x1y1 == 1 and x2y1 == 1:
                    if x3y1 == 0:
                        x3y1 = 2
                        T = False
                        draw()
                    pass
                elif x1y2 == 1 and x2y2 == 1:
                    if x3y2 == 0:
                        x3y2 = 2
                        T = False
                        draw()
                    pass
                elif x1y1 == 0:
                    x1y1 = 2
                    T = False
                    draw()
                elif x2y1 == 0:
                    x2y1 = 2
                    T = False
                    draw()
                elif x3y1 == 0:
                    x3y1 = 2
                    T = False
                    draw()
                elif x1y2 == 0:
                    x1y2 = 2
                    T = False
                    draw()
                elif x2y2 == 0:
                    x2y2 = 2
                    T = False
                    draw()
                elif x3y2 == 0:
                    x3y2 = 2
                    T = False
                    draw()
                elif x1y3 == 0:
                    x1y3 = 2
                    T = False
                    draw()
                elif x2y3 == 0:
                    x2y3 = 2
                    T = False
                    draw()
                elif x3y3 == 0:
                    x3y3 = 2
                    T = False
                    draw()
            elif R == 2:
                if x1y3 == 1 and x2y3 == 1:
                    if x3y3 == 0:
                        x3y3 = 2
                        T = False
                        draw()
                    pass
                elif x1y1 == 1 and x1y2 == 1:
                    if x1y3 == 0:
                        x1y3 = 2
                        T = False
                        draw()
                    pass
                elif x1y1 == 0:
                    x1y1 = 2
                    T = False
                    draw()
                elif x2y1 == 0:
                    x2y1 = 2
                    T = False
                    draw()
                elif x3y1 == 0:
                    x3y1 = 2
                    T = False
                    draw()
                elif x1y2 == 0:
                    x1y2 = 2
                    T = False
                    draw()
                elif x2y2 == 0:
                    x2y2 = 2
                    T = False
                    draw()
                elif x3y2 == 0:
                    x3y2 = 2
                    T = False
                    draw()
                elif x1y3 == 0:
                    x1y3 = 2
                    T = False
                    draw()
                elif x2y3 == 0:
                    x2y3 = 2
                    T = False
                    draw()
                elif x3y3 == 0:
                    x3y3 = 2
                    T = False
                    draw()
            elif R == 3:
                if x2y1 == 1 and x2y2 == 1:
                    if x2y3 == 0:
                        x2y3 = 2
                        T = False
                        draw()
                    pass
                elif x3y1 == 1 and x3y2 == 1:
                    if x3y3 == 0:
                        x3y3 = 2
                        T = False
                        draw()
                    pass
                elif x1y1 == 0:
                    x1y1 = 2
                    T = False
                    draw()
                elif x2y1 == 0:
                    x2y1 = 2
                    T = False
                    draw()
                elif x3y1 == 0:
                    x3y1 = 2
                    T = False
                    draw()
                elif x1y2 == 0:
                    x1y2 = 2
                    T = False
                    draw()
                elif x2y2 == 0:
                    x2y2 = 2
                    T = False
                    draw()
                elif x3y2 == 0:
                    x3y2 = 2
                    T = False
                    draw()
                elif x1y3 == 0:
                    x1y3 = 2
                    T = False
                    draw()
                elif x2y3 == 0:
                    x2y3 = 2
                    T = False
                    draw()
                elif x3y3 == 0:
                    x3y3 = 2
                    T = False
                    draw()
            elif R == 4:
                if x1y1 == 1 and x2y2 == 1:
                    if x3y3 == 0:
                        x3y3 = 2
                        T = False
                        draw()
                    pass
                elif x1y3 == 1 and x2y2 == 1:
                    if x3y1 == 0:
                        x3y1 = 2
                        T = False
                        draw()
                    pass
                elif x1y1 == 0:
                    x1y1 = 2
                    T = False
                    draw()
                elif x2y1 == 0:
                    x2y1 = 2
                    T = False
                    draw()
                elif x3y1 == 0:
                    x3y1 = 2
                    T = False
                    draw()
                elif x1y2 == 0:
                    x1y2 = 2
                    T = False
                    draw()
                elif x2y2 == 0:
                    x2y2 = 2
                    T = False
                    draw()
                elif x3y2 == 0:
                    x3y2 = 2
                    T = False
                    draw()
                elif x1y3 == 0:
                    x1y3 = 2
                    T = False
                    draw()
                elif x2y3 == 0:
                    x2y3 = 2
                    T = False
                    draw()
                elif x3y3 == 0:
                    x3y3 = 2
                    T = False
                    draw()
            elif R == 5:
                if x2y1 == 1 and x3y1 == 1:
                    if x1y1 == 0:
                        x1y1 = 2
                        T = False
                        draw()
                    pass
                elif x2y2 == 1 and x3y2 == 1:
                    if x1y2 == 0:
                        x3y1 = 2
                        T = False
                        draw()
                    pass
                elif x1y1 == 0:
                    x1y1 = 2
                    T = False
                    draw()
                elif x2y1 == 0:
                    x2y1 = 2
                    T = False
                    draw()
                elif x3y1 == 0:
                    x3y1 = 2
                    T = False
                    draw()
                elif x1y2 == 0:
                    x1y2 = 2
                    T = False
                    draw()
                elif x2y2 == 0:
                    x2y2 = 2
                    T = False
                    draw()
                elif x3y2 == 0:
                    x3y2 = 2
                    T = False
                    draw()
                elif x1y3 == 0:
                    x1y3 = 2
                    T = False
                    draw()
                elif x2y3 == 0:
                    x2y3 = 2
                    T = False
                    draw()
                elif x3y3 == 0:
                    x3y3 = 2
                    T = False
                    draw()
            elif R == 6:
                if x2y3 == 1 and x3y3 == 1:
                    if x1y3 == 0:
                        x3y1 = 2
                        T = False
                        draw()
                    pass
                elif x1y2 == 1 and x1y3 == 1:
                    if x1y1 == 0:
                        x1y1 = 2
                        T = False
                        draw()
                    pass
                elif x1y1 == 0:
                    x1y1 = 2
                    T = False
                    draw()
                elif x2y1 == 0:
                    x2y1 = 2
                    T = False
                    draw()
                elif x3y1 == 0:
                    x3y1 = 2
                    T = False
                    draw()
                elif x1y2 == 0:
                    x1y2 = 2
                    T = False
                    draw()
                elif x2y2 == 0:
                    x2y2 = 2
                    T = False
                    draw()
                elif x3y2 == 0:
                    x3y2 = 2
                    T = False
                    draw()
                elif x1y3 == 0:
                    x1y3 = 2
                    T = False
                    draw()
                elif x2y3 == 0:
                    x2y3 = 2
                    T = False
                    draw()
                elif x3y3 == 0:
                    x3y3 = 2
                    T = False
                    draw()
            elif R == 7:
                if x2y2 == 1 and x2y3 == 1:
                    if x2y1 == 0:
                        x2y1 = 2
                        T = False
                        draw()
                    pass
                elif x3y2 == 1 and x3y3 == 1:
                    if x3y1 == 0:
                        x3y1 = 2
                        T = False
                        draw()
                    pass
                elif x1y1 == 0:
                    x1y1 = 2
                    T = False
                    draw()
                elif x2y1 == 0:
                    x2y1 = 2
                    T = False
                    draw()
                elif x3y1 == 0:
                    x3y1 = 2
                    T = False
                    draw()
                elif x1y2 == 0:
                    x1y2 = 2
                    T = False
                    draw()
                elif x2y2 == 0:
                    x2y2 = 2
                    T = False
                    draw()
                elif x3y2 == 0:
                    x3y2 = 2
                    T = False
                    draw()
                elif x1y3 == 0:
                    x1y3 = 2
                    T = False
                    draw()
                elif x2y3 == 0:
                    x2y3 = 2
                    T = False
                    draw()
                elif x3y3 == 0:
                    x3y3 = 2
                    T = False
                    draw()
            elif R == 8:
                if x2y2 == 1 and x3y3 == 1:
                    if x1y1 == 0:
                        x1y1 = 2
                        T = False
                        draw()
                    pass
                elif x2y2 == 1 and x3y1 == 1:
                    if x1y3 == 0:
                        x3y1 = 2
                        T = False
                        draw()
                    pass
                elif x1y1 == 0:
                    x1y1 = 2
                    T = False
                    draw()
                elif x2y1 == 0:
                    x2y1 = 2
                    T = False
                    draw()
                elif x3y1 == 0:
                    x3y1 = 2
                    T = False
                    draw()
                elif x1y2 == 0:
                    x1y2 = 2
                    T = False
                    draw()
                elif x2y2 == 0:
                    x2y2 = 2
                    T = False
                    draw()
                elif x3y2 == 0:
                    x3y2 = 2
                    T = False
                    draw()
                elif x1y3 == 0:
                    x1y3 = 2
                    T = False
                    draw()
                elif x2y3 == 0:
                    x2y3 = 2
                    T = False
                    draw()
                elif x3y3 == 0:
                    x3y3 = 2
                    T = False
                    draw()
        elif raskus == 2:
            if R == 1:
                if x1y1 == 1 and x2y2 == 1:
                    if x3y3 == 0:
                        x3y3 = 2
                        T = False
                        draw()
                    pass
                elif x2y1 == 1 and x3y1 == 1:
                    if x1y1 == 0:
                        x1y1 = 2
                        T = False
                        draw()
                    pass
                elif x1y1 == 1 and x1y2 == 1:
                    if x1y3 == 0:
                        x1y3 = 2
                        T = False
                        draw()
                    pass
                elif x1y3 == 1 and x2y3 == 1:
                    if x3y3 == 0:
                        x3y3 = 2
                        T = False
                        draw()
                    pass
                elif x1y1 == 0:
                    x1y1 = 2
                    T = False
                    draw()
                elif x2y1 == 0:
                    x2y1 = 2
                    T = False
                    draw()
                elif x3y1 == 0:
                    x3y1 = 2
                    T = False
                    draw()
                elif x1y2 == 0:
                    x1y2 = 2
                    T = False
                    draw()
                elif x2y2 == 0:
                    x2y2 = 2
                    T = False
                    draw()
                elif x3y2 == 0:
                    x3y2 = 2
                    T = False
                    draw()
                elif x1y3 == 0:
                    x1y3 = 2
                    T = False
                    draw()
                elif x2y3 == 0:
                    x2y3 = 2
                    T = False
                    draw()
                elif x3y3 == 0:
                    x3y3 = 2
                    T = False
                    draw()
            elif R == 2:
                if x2y2 == 1 and x3y3 == 1:
                    if x1y1 == 0:
                        x1y1 = 2
                        T = False
                        draw()
                    pass
                elif x1y2 == 1 and x2y2 == 1:
                    if x3y2 == 0:
                        x3y2 = 2
                        T = False
                        draw()
                    pass
                elif x1y2 == 1 and x1y3 == 1:
                    if x1y1 == 0:
                        x1y1 = 2
                        T = False
                        draw()
                    pass
                elif x3y2 == 1 and x3y3 == 1:
                    if x3y1 == 0:
                        x3y1 = 2
                        T = False
                        draw()
                    pass
                elif x1y1 == 0:
                    x1y1 = 2
                    T = False
                    draw()
                elif x2y1 == 0:
                    x2y1 = 2
                    T = False
                    draw()
                elif x3y1 == 0:
                    x3y1 = 2
                    T = False
                    draw()
                elif x1y2 == 0:
                    x1y2 = 2
                    T = False
                    draw()
                elif x2y2 == 0:
                    x2y2 = 2
                    T = False
                    draw()
                elif x3y2 == 0:
                    x3y2 = 2
                    T = False
                    draw()
                elif x1y3 == 0:
                    x1y3 = 2
                    T = False
                    draw()
                elif x2y3 == 0:
                    x2y3 = 2
                    T = False
                    draw()
                elif x3y3 == 0:
                    x3y3 = 2
                    T = False
                    draw()
            elif R == 3:
                if x1y3 == 1 and x2y2 == 1:
                    if x3y1 == 0:
                        x3y1 = 2
                        T = False
                        draw()
                    pass
                elif x2y2 == 1 and x3y2 == 1:
                    if x1y2 == 0:
                        x1y2 = 2
                        T = False
                        draw()
                    pass
                elif x2y1 == 1 and x2y2 == 1:
                    if x2y3 == 0:
                        x2y3 = 2
                        T = False
                        draw()
                    pass
                elif x2y3 == 1 and x3y3 == 1:
                    if x1y3 == 0:
                        x1y3 = 2
                        T = False
                        draw()
                    pass
                elif x1y1 == 0:
                    x1y1 = 2
                    T = False
                    draw()
                elif x2y1 == 0:
                    x2y1 = 2
                    T = False
                    draw()
                elif x3y1 == 0:
                    x3y1 = 2
                    T = False
                    draw()
                elif x1y2 == 0:
                    x1y2 = 2
                    T = False
                    draw()
                elif x2y2 == 0:
                    x2y2 = 2
                    T = False
                    draw()
                elif x3y2 == 0:
                    x3y2 = 2
                    T = False
                    draw()
                elif x1y3 == 0:
                    x1y3 = 2
                    T = False
                    draw()
                elif x2y3 == 0:
                    x2y3 = 2
                    T = False
                    draw()
                elif x3y3 == 0:
                    x3y3 = 2
                    T = False
                    draw()
            elif R == 4:
                if x2y2 == 1 and x3y1 == 1:
                    if x1y3 == 0:
                        x1y3 = 2
                        T = False
                        draw()
                    pass
                elif x1y1 == 1 and x2y1 == 1:
                    if x3y1 == 0:
                        x3y1 = 2
                        T = False
                        draw()
                    pass
                elif x2y2 == 1 and x2y3 == 1:
                    if x2y1 == 0:
                        x2y1 = 2
                        T = False
                        draw()
                    pass
                elif x3y1 == 1 and x3y2 == 1:
                    if x3y3 == 0:
                        x3y3 = 2
                        T = False
                        draw()
                    pass
                elif x1y1 == 0:
                    x1y1 = 2
                    T = False
                    draw()
                elif x2y1 == 0:
                    x2y1 = 2
                    T = False
                    draw()
                elif x3y1 == 0:
                    x3y1 = 2
                    T = False
                    draw()
                elif x1y2 == 0:
                    x1y2 = 2
                    T = False
                    draw()
                elif x2y2 == 0:
                    x2y2 = 2
                    T = False
                    draw()
                elif x3y2 == 0:
                    x3y2 = 2
                    T = False
                    draw()
                elif x1y3 == 0:
                    x1y3 = 2
                    T = False
                    draw()
                elif x2y3 == 0:
                    x2y3 = 2
                    T = False
                    draw()
                elif x3y3 == 0:
                    x3y3 = 2
                    T = False
                    draw()
        elif raskus == 3:
            if R == 1:
                if x1y1 == 1 and x2y1 == 1:
                    if x3y1 == 0:
                        x3y1 = 2
                        T = False
                        draw()
                    pass
                elif x2y1 == 1 and x3y1 == 1:
                    if x1y1 == 0:
                        x1y1 = 2
                        T = False                        
                        draw()
                    pass
                elif x1y2 == 1 and x2y2 == 1:
                    if x3y2 == 0:
                        x3y2 = 2
                        T = False
                        draw()
                    pass
                elif x1y1 == 1 and x1y2 == 1:
                    if x1y3 == 0:
                        x1y3 = 2
                        T = False
                        draw()
                    pass
                elif x1y2 == 1 and x1y3 == 1:
                    if x1y1 == 0:
                        x1y1 = 2
                        T = False
                        draw()
                    pass
                elif x2y1 == 1 and x2y2 == 1:
                    if x2y3 == 0:
                        x2y3 = 2
                        T = False
                        draw()
                    pass
                elif x1y1 == 1 and x2y2 == 1:
                    if x3y3 == 0:
                        x3y3 = 2
                        T = False
                        draw()
                    pass
                elif x2y2 == 1 and x3y3 == 1:
                    if x1y1 == 0:
                        x1y1 = 2
                        T = False
                        draw()
                    pass
                elif x1y1 == 0:
                    x1y1 = 2
                    T = False
                    draw()
                elif x2y1 == 0:
                    x2y1 = 2
                    T = False
                    draw()
                elif x3y1 == 0:
                    x3y1 = 2
                    T = False
                    draw()
                elif x1y2 == 0:
                    x1y2 = 2
                    T = False
                    draw()
                elif x2y2 == 0:
                    x2y2 = 2
                    T = False
                    draw()
                elif x3y2 == 0:
                    x3y2 = 2
                    T = False
                    draw()
                elif x1y3 == 0:
                    x1y3 = 2
                    T = False
                    draw()
                elif x2y3 == 0:
                    x2y3 = 2
                    T = False
                    draw()
                elif x3y3 == 0:
                    x3y3 = 2
                    T = False
                    draw()
            elif R == 2:
                if x2y2 == 1 and x3y2 == 1:
                    if x1y2 == 0:
                        x3y3 = 2
                        T = False
                        draw()
                    pass
                elif x1y3 == 1 and x2y3 == 1:
                    if x3y3 == 0:
                        x3y3 = 2
                        T = False
                        draw()
                    pass
                elif x2y3 == 1 and x3y3 == 1:
                    if x1y3 == 0:
                        x1y3 = 2
                        T = False
                        draw()
                    pass
                elif x2y2 == 1 and x2y3 == 1:
                    if x2y1 == 0:
                        x2y1 = 2
                        T = False
                        draw()
                    pass
                elif x3y1 == 1 and x3y2 == 1:
                    if x3y3 == 0:
                        x3y3 = 2
                        T = False
                        draw()
                    pass
                elif x3y2 == 1 and x3y3 == 1:
                    if x3y1 == 0:
                        x3y1 = 2
                        T = False
                        draw()
                    pass
                elif x1y3 == 1 and x2y2 == 1:
                    if x3y1 == 0:
                        x3y1 = 2
                        T = False
                        draw()
                    pass
                elif x2y2 == 1 and x3y1 == 1:
                    if x1y3 == 0:
                        x1y3 = 2
                        T = False
                        draw()
                    pass
                elif x1y1 == 0:
                    x1y1 = 2
                    T = False
                    draw()
                elif x2y1 == 0:
                    x2y1 = 2
                    T = False
                    draw()
                elif x3y1 == 0:
                    x3y1 = 2
                    T = False
                    draw()
                elif x1y2 == 0:
                    x1y2 = 2
                    T = False
                    draw()
                elif x2y2 == 0:
                    x2y2 = 2
                    T = False
                    draw()
                elif x3y2 == 0:
                    x3y2 = 2
                    T = False
                    draw()
                elif x1y3 == 0:
                    x1y3 = 2
                    T = False
                    draw()
                elif x2y3 == 0:
                    x2y3 = 2
                    T = False
                    draw()
                elif x3y3 == 0:
                    x3y3 = 2
                    T = False
                    draw()
        elif raskus == 4:
            if x1y1 == 1 and x2y1 == 1:
                if x3y1 == 0:
                    x3y1 = 2
                    T = False
                    draw()
                pass
            elif x2y1 == 1 and x3y1 == 1:
                if x1y1 == 0:
                    x1y1 = 2
                    T = False
                    draw()
                pass
            elif x1y2 == 1 and x2y2 == 1:
                if x3y2 == 0:
                    x3y2 = 2
                    T = False
                    draw()
                pass
            elif x2y2 == 1 and x3y2 == 1:
                if x1y2 == 0:
                    x1y2 = 2
                    T = False
                    draw()
                pass
            elif x1y3 == 1 and x2y3 == 1:
                if x3y3 == 0:
                    x3y3 = 2
                    T = False
                    draw()
                pass
            elif x2y3 == 1 and x3y3 == 1:
                if x1y3 == 0:
                    x1y3 = 2
                    T = False
                    draw()
                pass
            elif x1y1 == 1 and x1y2 == 1:
                if x1y3 == 0:
                    x1y3 = 2
                    T = False
                    draw()
                pass
            elif x1y2 == 1 and x1y3 == 1:
                if x1y1 == 0:
                    x1y1 = 2
                    T = False
                    draw()
                pass
            elif x2y1 == 1 and x2y2 == 1:
                if x2y3 == 0:
                    x2y3 = 2
                    T = False
                    draw()
                pass
            elif x2y2 == 1 and x2y3 == 1:
                if x2y1 == 0:
                    x2y1 = 2
                    T = False
                    draw()
                pass
            elif x3y1 == 1 and x3y2 == 1:
                if x3y3 == 0:
                    x3y3 = 2
                    T = False
                    draw()
                pass
            elif x3y2 == 1 and x3y3 == 1:
                if x3y1 == 0:
                    x3y1 = 2
                    T = False
                    draw()
                pass
            elif x1y1 == 1 and x2y2 == 1:
                if x3y3 == 0:
                    x3y3 = 2
                    T = False
                    draw()
                pass
            elif x2y2 == 1 and x3y3 == 1:
                if x1y1 == 0:
                    x1y1 = 2
                    T = False
                    draw()
                pass
            elif x1y3 == 1 and x2y2 == 1:
                if x3y1 == 0:
                    x3y1 = 2
                    T = False
                    draw()
                pass
            elif x2y2 == 1 and x3y1 == 1:
                if x1y3 == 0:
                    x1y3 = 2
                    T = False
                    draw()
                pass
            elif x1y1 == 0:
                x1y1 = 2
                T = False
                draw()
            elif x2y1 == 0:
                x2y1 = 2
                T = False
                draw()
            elif x3y1 == 0:
                x3y1 = 2
                T = False
                draw()
            elif x1y2 == 0:
                x1y2 = 2
                T = False
                draw()
            elif x2y2 == 0:
                x2y2 = 2
                T = False
                draw()
            elif x3y2 == 0:
                x3y2 = 2
                T = False
                draw()
            elif x1y3 == 0:
                x1y3 = 2
                T = False
                draw()
            elif x2y3 == 0:
                x2y3 = 2
                T = False
                draw()
            elif x3y3 == 0:
                x3y3 = 2
                T = False
                draw()


def check():
    global x1y1, x2y1, x3y1, x1y2, x2y2, x3y2, x1y3, x2y3, x3y3, player_name, bot_name, P1, P2
    A = P1 + P2
    if x1y1 == 1 and x2y1 == 1 and x3y1 == 1:
        print (player_name, ' won')
        reset()
    elif x1y2 == 1 and x2y2 == 1 and x3y2 == 1:
        print (player_name, ' won')
        reset()
    elif x1y3 == 1 and x2y3 == 1 and x3y3 == 1:
        print (player_name, ' won')
        reset()
    elif x1y1 == 1 and x1y2 == 1 and x1y3 == 1:
        print (player_name, ' won')
        reset()
    elif x2y1 == 1 and x2y2 == 1 and x2y3 == 1:
        print (player_name, ' won')
        reset()
    elif x3y1 == 1 and x3y2 == 1 and x3y3 == 1:
        print (player_name, ' won')
        reset()
    elif x1y1 == 1 and x2y2 == 1 and x3y3 == 1:
        print (player_name, ' won')
        reset()
    elif x3y1 == 1 and x2y2 == 1 and x1y3 == 1:
        print (player_name, ' won')
        reset()
    elif x1y1 == 2 and x2y1 == 2 and x3y1 == 2:
        print (bot_name, ' won')
        reset()
    elif x1y2 == 2 and x2y2 == 2 and x3y2 == 2:
        print (bot_name, ' won')
        reset()
    elif x1y3 == 2 and x2y3 == 2 and x3y3 == 2:
        print (bot_name, ' won')
        reset()
    elif x1y1 == 2 and x1y2 == 2 and x1y3 == 2:
        print (bot_name, ' won')
        reset()
    elif x2y1 == 2 and x2y2 == 2 and x2y3 == 2:
        print (bot_name, ' won')
        reset()
    elif x3y1 == 2 and x3y2 == 2 and x3y3 == 2:
        print (bot_name, ' won')
        reset()
    elif x1y1 == 2 and x2y2 == 2 and x3y3 == 2:
        print (bot_name, ' won')
        reset()
    elif x3y1 == 2 and x2y2 == 2 and x1y3 == 2:
        print (bot_name, ' won')
        reset()
    elif A == 9:
        print ("it's a draw")
        reset()
    else:
        control()


def reset():
    global x1y1, x2y1, x3y1, x1y2, x2y2, x3y2, x1y3, x2y3, x3y3, T, player_name, bot_name, P1, P2, B, raskus, R
    B = False
    P1 = 0
    P2 = 0
    T = False
    x1y1 = 0
    x2y1 = 0
    x3y1 = 0
    x1y2 = 0
    x2y2 = 0
    x3y2 = 0
    x1y3 = 0
    x2y3 = 0
    x3y3 = 0
    player_name = input('player name = ')
    bot_name = input('bot name = ')
    print ('Easy(1) or normal(2) or hard(3) or impossible(4)')
    raskus = int(input('>>>   '))
    if raskus == 1:
        R = randint(1, 8)
        pass
    if raskus == 2:
        R = randint(1, 4)
        pass
    if raskus == 3:
        R = randint(1, 2)
        pass
    if raskus > 4:
        print ('ERROR')
        print ('vale raskus astme ID')
        print ('aborting')
        sys.exit()
    control()

control()