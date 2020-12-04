# Import libraries
import os
import time
import random
# import mysql.connector # For multiplayer
# Global variables
inputFields = ['1','2','3','4','5','6','7','8','9']
mode = 0
player = 'o'
i = 0

# Before game starts, select mode
def menu():
    os.system('cls')
    global mode, inputFields
    print('\nTicTacToe by Vassili\n')
    print('Choose game mode:')
    print('1. Player vs player')
    print('2. Singleplayer')
    mode = int(input('--->'))
    draw(inputFields)

# After start, draw gamefield
def draw(i):
    os.system('cls')
    print('|---|---|---|')
    print('|',i[6],'|',i[7],'|',i[8],'|')
    print('|---|---|---|')
    print('|',i[3],'|',i[4],'|',i[5],'|')
    print('|---|---|---|')
    print('|',i[0],'|',i[1],'|',i[2],'|')
    print('|---|---|---|')
    # If game mode is choosed
    if mode == 1: pvp()
    if mode == 2: singleplayer()
    else: menu()

# Player vs player logic
def pvp():
    global player, inputFields
    if player == 'x': player = 'o'
    else: player = 'x'

    i = int(input('Input field (1-9): '))

    # If game field is empty
    if inputFields[i - 1] != 'x' and inputFields[i - 1] != 'o': inputFields[i - 1] = player
    else: 
        print('Select another field')
        time.sleep(3)
        if player == 'x': player = 'o'
        else: player = 'x'

    check()

# Singleplayer logic
def singleplayer():
    global player, inputFields, i
    if player == 'x':

        if inputFields[0] == 'x' and inputFields[1] == 'x' and inputFields[2] == '3': i = 3
        elif inputFields[3] == 'x' and inputFields[4] == 'x' and inputFields[5] == '6': i = 6
        elif inputFields[6] == 'x' and inputFields[7] == 'x' and inputFields[8] == '9': i = 9
        elif inputFields[8] == 'x' and inputFields[7] == 'x' and inputFields[5] == '6': i = 7
        elif inputFields[5] == 'x' and inputFields[4] == 'x' and inputFields[3] == '4': i = 4
        elif inputFields[2] == 'x' and inputFields[1] == 'x' and inputFields[0] == '1': i = 1
        elif inputFields[0] == 'x' and inputFields[3] == 'x' and inputFields[6] == '7': i = 7
        elif inputFields[1] == 'x' and inputFields[5] == 'x' and inputFields[7] == '8': i = 8
        elif inputFields[2] == 'x' and inputFields[6] == 'x' and inputFields[7] == '8': i = 9
        # 1-3
        elif inputFields[i - 1] == inputFields[0] and inputFields[1] == '2' and inputFields[3] == '4': i = random.choices([2,4])
        elif inputFields[i - 1] == inputFields[1] and inputFields[0] == '1' and inputFields[4] == '5' and inputFields[2] == '3': i = random.choices([1,5,3])
        elif inputFields[i - 1] == inputFields[2] and inputFields[0] == '1' and inputFields[1] == '2' and inputFields[5] == '6': i = random.choices([1,2,6])
        # 4-6
        elif inputFields[i - 1] == inputFields[3] and inputFields[0] == '1' and inputFields[6] == '7' and inputFields[4] == '5': i = random.choices([1,7,5])
        elif inputFields[i - 1] == inputFields[4] and inputFields[1] == '2' and inputFields[3] == '4' and inputFields[5] == '6' and inputFields[7] == '8': i = random.choices([2,4,6,8])
        elif inputFields[i - 1] == inputFields[5] and inputFields[2] == '3' and inputFields[4] == '5' and inputFields[8] == '9': i = random.choices([3,5,9])
        # 7-9
        elif inputFields[i - 1] == inputFields[6] and inputFields[3] == '4' and inputFields[7] == '8': i = random.choices([4,8])
        elif inputFields[i - 1] == inputFields[7] and inputFields[4] == '5' and inputFields[6] == '7' and inputFields[8] == '9': i = random.choice([5,7,8])
        elif inputFields[i - 1] == inputFields[8] and inputFields[5] == '6' and inputFields[7] == '8': i = random.choice([6,8]) 
        else: i = random.randrange(1,9)

        player = 'o'
    else: 
        i = int(input('Input field (1-9): '))
        player = 'x'

    i -= 1
    if inputFields[i] != 'x' and inputFields[i] != 'o': inputFields[i] = player
    else:
        print('Select another field')
        time.sleep(3)
        if player == 'x': player = 'o'
        else: player = 'x'
    check()

def check():
    global player
    # If row is full
    if inputFields[0] == 'x' and inputFields[1] == 'x' and inputFields[2] == 'x' or inputFields[0] == 'o' and inputFields[1] == 'o' and inputFields[2] == 'o': reset()
    if inputFields[3] == 'x' and inputFields[4] == 'x' and inputFields[5] == 'x' or inputFields[3] == 'o' and inputFields[4] == 'o' and inputFields[5] == 'o': reset()
    if inputFields[6] == 'x' and inputFields[7] == 'x' and inputFields[8] == 'x' or inputFields[6] == 'o' and inputFields[7] == 'o' and inputFields[8] == 'o': reset()
    if inputFields[0] == 'x' and inputFields[3] == 'x' and inputFields[6] == 'x' or inputFields[0] == 'o' and inputFields[3] == 'o' and inputFields[6] == 'o': reset()
    if inputFields[1] == 'x' and inputFields[4] == 'x' and inputFields[7] == 'x' or inputFields[1] == 'o' and inputFields[4] == 'o' and inputFields[7] == 'o': reset()
    if inputFields[2] == 'x' and inputFields[5] == 'x' and inputFields[8] == 'x' or inputFields[2] == 'o' and inputFields[5] == 'o' and inputFields[8] == 'o': reset()
    if inputFields[0] == 'x' and inputFields[4] == 'x' and inputFields[8] == 'x' or inputFields[0] == 'o' and inputFields[4] == 'o' and inputFields[8] == 'o': reset()
    if inputFields[6] == 'x' and inputFields[4] == 'x' and inputFields[2] == 'x' or inputFields[6] == 'o' and inputFields[4] == 'o' and inputFields[2] == 'o': reset()
    draw(inputFields)

# Reset game
def reset():
    global inputFields, player, i
    inputFields = ['1','2','3','4','5','6','7','8','9']
    print('Player ',player,' won')
    i = 0
    time.sleep(2)
    menu()

menu()
