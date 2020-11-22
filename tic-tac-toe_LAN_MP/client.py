import socket, sys, threading, os

IP = input('IP = ')
port = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, port))

x1y1 = 0
x2y1 = 0
x3y1 = 0
x1y2 = 0
x2y2 = 0
x3y2 = 0
x1y3 = 0
x2y3 = 0
x3y3 = 0
your_turn = False
player_number = 0
win = False
lose = False

def game():
    global x1y1, x2y1, x3y1, x1y2, x2y2, x3y2, x1y3, x2y3, x3y3, your_turn, player_number, win, lose
    while True:
        data = client.recv(1024)
        string = data.decode()
        if '|' in string:
            part1 = string.split('|')[0]
            part2 = string.split('|')[1]
            exec(part1, globals())
            exec(part2, globals())
        else:
            exec(string, globals())
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
        
        if win:
            os.system('cls')
            print ('YOU WON!')
        elif lose:
            os.system('cls')
            print ('YOU LOSE!')
        
        elif your_turn:
            part1 = input('what are the coordinates?   ')
            part2 = part1 + ' = ' + str(player_number)
            exec(part2, globals())
            client.send(part2.encode())
            your_turn = False

thread1 = threading.Thread(target=game)
thread1.start()