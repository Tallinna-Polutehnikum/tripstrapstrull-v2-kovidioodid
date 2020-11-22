import socket, threading

IP = '172.18.15.2'
port = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, port))
server.listen()

people = []
addr_list = []
player1 = ''
player2 = ''
game_start = False
x1y1 = 0
x2y1 = 0
x3y1 = 0
x1y2 = 0
x2y2 = 0
x3y2 = 0
x1y3 = 0
x2y3 = 0
x3y3 = 0
T = 1
P1 = 0
P2 = 0

def connect():
    global people, addr_list
    while True:
        conn, addr = server.accept()
        people.append(conn)
        addr_list.append(addr)
        print ('new connection from ', addr)
        if len(people) > 2:
            print ('game was full')
            print (addr, ' disconnected')
            people.remove(conn)
            addr_list.remove(addr)
            conn.close()
        if len(people) == 2:
            thread2.start()
            
            
def pre_game():
    global people, player1, player2, game_start
    while True:
        if not game_start:
            if len(people) == 2:
                player1 = people[0]
                player2 = people[1]
                thread3.start()
                game_start = True

def game():
    global player1, player2, x1y1, x2y1, x3y1, x1y2, x2y2, x3y2, x1y3, x2y3, x3y3, T, P1, P2, people, addr_list, game_start
    while True:
        if T == 1:
            player1.send('your_turn = True|player_number = 1'.encode())
            data = player1.recv(1024)
        elif T == 2:
            player2.send('your_turn = True|player_number = 2'.encode())
            data = player2.recv(1024)
        exec(data.decode(), globals())
        if T == 1:
            P1 += 1
            player2.send(data)
            T = 2
        else:
            P2 += 1
            player1.send(data)
            T = 1
        if P1 >= 3:
            if x1y1 == 1 and x2y1 == 1 and x3y1 == 1:
                print (player1, ' won')
                player1.send('win = True'.encode())
                player2.send('lose = True'.encode())
                reset = input('do you want to reset the game?   ')
                if reset == 'yes':
                    x1y1 = 0
                    x2y1 = 0
                    x3y1 = 0
                    x1y2 = 0
                    x2y2 = 0
                    x3y2 = 0
                    x1y3 = 0
                    x2y3 = 0
                    x3y3 = 0
                    T = 1
                    P1 = 0
                    P2 = 0
                    player1 = ''
                    player2 = ''
                    for con in people:
                        con.close()
                    for adr in addr_list:
                        print (adr, ' disconnected')
                    people = []
                    addr_list = []
                    game_start = False
                    thread3.join()
                    break
            elif x1y2 == 1 and x2y2 == 1 and x3y2 == 1:
                print (player1, ' won')
                player1.send('win = True'.encode())
                player2.send('lose = True'.encode())
                reset = input('do you want to reset the game?   ')
                if reset == 'yes':
                    x1y1 = 0
                    x2y1 = 0
                    x3y1 = 0
                    x1y2 = 0
                    x2y2 = 0
                    x3y2 = 0
                    x1y3 = 0
                    x2y3 = 0
                    x3y3 = 0
                    T = 1
                    P1 = 0
                    P2 = 0
                    player1 = ''
                    player2 = ''
                    for con in people:
                        con.close()
                    for adr in addr_list:
                        print (adr, ' disconnected')
                    people = []
                    addr_list = []
                    game_start = False
                    thread3.join()
                    break
            elif x1y3 == 1 and x2y3 == 1 and x3y3 == 1:
                print (player1, ' won')
                player1.send('win = True'.encode())
                player2.send('lose = True'.encode())
                reset = input('do you want to reset the game?   ')
                if reset == 'yes':
                    x1y1 = 0
                    x2y1 = 0
                    x3y1 = 0
                    x1y2 = 0
                    x2y2 = 0
                    x3y2 = 0
                    x1y3 = 0
                    x2y3 = 0
                    x3y3 = 0
                    T = 1
                    P1 = 0
                    P2 = 0
                    player1 = ''
                    player2 = ''
                    for con in people:
                        con.close()
                    for adr in addr_list:
                        print (adr, ' disconnected')
                    people = []
                    addr_list = []
                    game_start = False
                    thread3.join()
                    break
            elif x1y1 == 1 and x1y2 == 1 and x1y3 == 1:
                print (player1, ' won')
                player1.send('win = True'.encode())
                player2.send('lose = True'.encode())
                reset = input('do you want to reset the game?   ')
                if reset == 'yes':
                    x1y1 = 0
                    x2y1 = 0
                    x3y1 = 0
                    x1y2 = 0
                    x2y2 = 0
                    x3y2 = 0
                    x1y3 = 0
                    x2y3 = 0
                    x3y3 = 0
                    T = 1
                    P1 = 0
                    P2 = 0
                    player1 = ''
                    player2 = ''
                    for con in people:
                        con.close()
                    for adr in addr_list:
                        print (adr, ' disconnected')
                    people = []
                    addr_list = []
                    game_start = False
                    thread3.join()
                    break
            elif x2y1 == 1 and x2y2 == 1 and x2y3 == 1:
                print (player1, ' won')
                player1.send('win = True'.encode())
                player2.send('lose = True'.encode())
                reset = input('do you want to reset the game?   ')
                if reset == 'yes':
                    x1y1 = 0
                    x2y1 = 0
                    x3y1 = 0
                    x1y2 = 0
                    x2y2 = 0
                    x3y2 = 0
                    x1y3 = 0
                    x2y3 = 0
                    x3y3 = 0
                    T = 1
                    P1 = 0
                    P2 = 0
                    player1 = ''
                    player2 = ''
                    for con in people:
                        con.close()
                    for adr in addr_list:
                        print (adr, ' disconnected')
                    people = []
                    addr_list = []
                    game_start = False
                    thread3.join()
                    break
            elif x3y1 == 1 and x3y2 == 1 and x3y3 == 1:
                print (player1, ' won')
                player1.send('win = True'.encode())
                player2.send('lose = True'.encode())
                reset = input('do you want to reset the game?   ')
                if reset == 'yes':
                    x1y1 = 0
                    x2y1 = 0
                    x3y1 = 0
                    x1y2 = 0
                    x2y2 = 0
                    x3y2 = 0
                    x1y3 = 0
                    x2y3 = 0
                    x3y3 = 0
                    T = 1
                    P1 = 0
                    P2 = 0
                    player1 = ''
                    player2 = ''
                    for con in people:
                        con.close()
                    for adr in addr_list:
                        print (adr, ' disconnected')
                    people = []
                    addr_list = []
                    game_start = False
                    thread3.join()
                    break
            elif x1y1 == 1 and x2y2 == 1 and x3y3 == 1:
                print (player1, ' won')
                player1.send('win = True'.encode())
                player2.send('lose = True'.encode())
                reset = input('do you want to reset the game?   ')
                if reset == 'yes':
                    x1y1 = 0
                    x2y1 = 0
                    x3y1 = 0
                    x1y2 = 0
                    x2y2 = 0
                    x3y2 = 0
                    x1y3 = 0
                    x2y3 = 0
                    x3y3 = 0
                    T = 1
                    P1 = 0
                    P2 = 0
                    player1 = ''
                    player2 = ''
                    for con in people:
                        con.close()
                    for adr in addr_list:
                        print (adr, ' disconnected')
                    people = []
                    addr_list = []
                    game_start = False
                    thread3.join()
                    break
            elif x3y1 == 1 and x2y2 == 1 and x1y3 == 1:
                print (player1, ' won')
                player1.send('win = True'.encode())
                player2.send('lose = True'.encode())
                reset = input('do you want to reset the game?   ')
                if reset == 'yes':
                    x1y1 = 0
                    x2y1 = 0
                    x3y1 = 0
                    x1y2 = 0
                    x2y2 = 0
                    x3y2 = 0
                    x1y3 = 0
                    x2y3 = 0
                    x3y3 = 0
                    T = 1
                    P1 = 0
                    P2 = 0
                    player1 = ''
                    player2 = ''
                    for con in people:
                        con.close()
                    for adr in addr_list:
                        print (adr, ' disconnected')
                    people = []
                    addr_list = []
                    game_start = False
                    thread3.join()
                    break
        if P2 >= 3:
            if x1y1 == 2 and x2y1 == 2 and x3y1 == 2:
                print (player1, ' won')
                player2.send('win = True'.encode())
                player1.send('lose = True'.encode())
                reset = input('do you want to reset the game?   ')
                if reset == 'yes':
                    x1y1 = 0
                    x2y1 = 0
                    x3y1 = 0
                    x1y2 = 0
                    x2y2 = 0
                    x3y2 = 0
                    x1y3 = 0
                    x2y3 = 0
                    x3y3 = 0
                    T = 1
                    P1 = 0
                    P2 = 0
                    player1 = ''
                    player2 = ''
                    for con in people:
                        con.close()
                    for adr in addr_list:
                        print (adr, ' disconnected')
                    people = []
                    addr_list = []
                    game_start = False
                    thread3.join()
                    break
            elif x1y2 == 2 and x2y2 == 2 and x3y2 == 2:
                print (player1, ' won')
                player2.send('win = True'.encode())
                player1.send('lose = True'.encode())
                reset = input('do you want to reset the game?   ')
                if reset == 'yes':
                    x1y1 = 0
                    x2y1 = 0
                    x3y1 = 0
                    x1y2 = 0
                    x2y2 = 0
                    x3y2 = 0
                    x1y3 = 0
                    x2y3 = 0
                    x3y3 = 0
                    T = 1
                    P1 = 0
                    P2 = 0
                    player1 = ''
                    player2 = ''
                    for con in people:
                        con.close()
                    for adr in addr_list:
                        print (adr, ' disconnected')
                    people = []
                    addr_list = []
                    game_start = False
                    thread3.join()
                    break
            elif x1y3 == 2 and x2y3 == 2 and x3y3 == 2:
                print (player1, ' won')
                player2.send('win = True'.encode())
                player1.send('lose = True'.encode())
                reset = input('do you want to reset the game?   ')
                if reset == 'yes':
                    x1y1 = 0
                    x2y1 = 0
                    x3y1 = 0
                    x1y2 = 0
                    x2y2 = 0
                    x3y2 = 0
                    x1y3 = 0
                    x2y3 = 0
                    x3y3 = 0
                    T = 1
                    P1 = 0
                    P2 = 0
                    player1 = ''
                    player2 = ''
                    for con in people:
                        con.close()
                    for adr in addr_list:
                        print (adr, ' disconnected')
                    people = []
                    addr_list = []
                    game_start = False
                    thread3.join()
                    break
            elif x1y1 == 2 and x1y2 == 2 and x1y3 == 2:
                print (player1, ' won')
                player2.send('win = True'.encode())
                player1.send('lose = True'.encode())
                reset = input('do you want to reset the game?   ')
                if reset == 'yes':
                    x1y1 = 0
                    x2y1 = 0
                    x3y1 = 0
                    x1y2 = 0
                    x2y2 = 0
                    x3y2 = 0
                    x1y3 = 0
                    x2y3 = 0
                    x3y3 = 0
                    T = 1
                    P1 = 0
                    P2 = 0
                    player1 = ''
                    player2 = ''
                    for con in people:
                        con.close()
                    for adr in addr_list:
                        print (adr, ' disconnected')
                    people = []
                    addr_list = []
                    game_start = False
                    thread3.join()
                    break
            elif x2y1 == 2 and x2y2 == 2 and x2y3 == 2:
                print (player1, ' won')
                player2.send('win = True'.encode())
                player1.send('lose = True'.encode())
                reset = input('do you want to reset the game?   ')
                if reset == 'yes':
                    x1y1 = 0
                    x2y1 = 0
                    x3y1 = 0
                    x1y2 = 0
                    x2y2 = 0
                    x3y2 = 0
                    x1y3 = 0
                    x2y3 = 0
                    x3y3 = 0
                    T = 1
                    P1 = 0
                    P2 = 0
                    player1 = ''
                    player2 = ''
                    for con in people:
                        con.close()
                    for adr in addr_list:
                        print (adr, ' disconnected')
                    people = []
                    addr_list = []
                    game_start = False
                    thread3.join()
                    break
            elif x3y1 == 2 and x3y2 == 2 and x3y3 == 2:
                print (player1, ' won')
                player2.send('win = True'.encode())
                player1.send('lose = True'.encode())
                reset = input('do you want to reset the game?   ')
                if reset == 'yes':
                    x1y1 = 0
                    x2y1 = 0
                    x3y1 = 0
                    x1y2 = 0
                    x2y2 = 0
                    x3y2 = 0
                    x1y3 = 0
                    x2y3 = 0
                    x3y3 = 0
                    T = 1
                    P1 = 0
                    P2 = 0
                    player1 = ''
                    player2 = ''
                    for con in people:
                        con.close()
                    for adr in addr_list:
                        print (adr, ' disconnected')
                    people = []
                    addr_list = []
                    game_start = False
                    thread3.join()
                    break
            elif x1y1 == 2 and x2y2 == 2 and x3y3 == 2:
                print (player1, ' won')
                player2.send('win = True'.encode())
                player1.send('lose = True'.encode())
                reset = input('do you want to reset the game?   ')
                if reset == 'yes':
                    x1y1 = 0
                    x2y1 = 0
                    x3y1 = 0
                    x1y2 = 0
                    x2y2 = 0
                    x3y2 = 0
                    x1y3 = 0
                    x2y3 = 0
                    x3y3 = 0
                    T = 1
                    P1 = 0
                    P2 = 0
                    player1 = ''
                    player2 = ''
                    for con in people:
                        con.close()
                    for adr in addr_list:
                        print (adr, ' disconnected')
                    people = []
                    addr_list = []
                    game_start = False
                    thread3.join()
                    break
            elif x3y1 == 2 and x2y2 == 2 and x1y3 == 2:
                print (player1, ' won')
                player2.send('win = True'.encode())
                player1.send('lose = True'.encode())
                reset = input('do you want to reset the game?   ')
                if reset == 'yes':
                    x1y1 = 0
                    x2y1 = 0
                    x3y1 = 0
                    x1y2 = 0
                    x2y2 = 0
                    x3y2 = 0
                    x1y3 = 0
                    x2y3 = 0
                    x3y3 = 0
                    T = 1
                    P1 = 0
                    P2 = 0
                    player1 = ''
                    player2 = ''
                    for con in people:
                        con.close()
                    for adr in addr_list:
                        print (adr, ' disconnected')
                    people = []
                    addr_list = []
                    game_start = False
                    thread3.join()
                    break

thread1 = threading.Thread(target=connect)
thread2 = threading.Thread(target=pre_game)
thread3 = threading.Thread(target=game)

thread1.start()