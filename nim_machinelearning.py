#!/usr/bin/python3
import random

def initialize():
    '''
    This function initializes the computer's strategy vector.
    '''
    strategy=[[] for i in range(754)]
    for i in range(754):
        val = str(i).zfill(3)
        if int(val[0]) < 8 and int(val[1]) < 6 and int(val[2]) < 4:
            for j in range(1, int(val[0])+1):
                strategy[i].append([1, j, 50])
            for j in range(1, int(val[1])+1):
                strategy[i].append([2, j, 50])
            for j in range(1, int(val[2])+1):
                strategy[i].append([3, j, 50])
    return strategy


def player(n,position):
    '''
    This is the function that runs for a human player to make a move.
    Its input is the player number, and the position of the game.
    At the end, if the position is [0,0,0], it announces the winner.
    '''
    pile = 0
    take = 0
    w = True
    while w:
        move = input(f'Player {n}, what move would you like to make?')
        if len(move) != 3:
            print("Invalid move, input your move by first putting which pile you want to take from and then how many. Example: 1 3 to take 3 from the first pile.")
        pile, take = int(move[0]), int(move[2])
        if pile > 3 or pile < 1:
            print('Invalid move')
        elif take > position[pile - 1]:
            print('Invalid move')
        else:
            w = False
    position[pile - 1] -= take
    if position == [0,0,0]:
        print("Player ",n," wins!  Congratulations!")


def computer(n,position,moves,strategy):
    '''
    This function runs when the computer makes a move.
    It appends the move that it makes to the variable "moves",
    and adjusts the value of "position" accordingly.
    '''
    s = [str(i) for i in position]
    posvector = int("".join(s))

    bestmoves = []
    mx = max([l[2]for l in strategy[posvector]])
    for j in range(len(strategy[posvector])):
        if strategy[posvector][j][2] == mx:
            bestmoves.append(j)
    m = random.choice(bestmoves)
    pile = strategy[posvector][m][0]
    take = strategy[posvector][m][1]
    position[pile - 1] -= take
    if take == 1:
        print(f"Computer player {n} takes {take} object from pile {pile}")
    else:
        print(f"Computer player {n} takes {take} objects from pile {pile}")
    moves.append([posvector, m])
    if position == [0,0,0]:
        print("Computer Player ",n," wins!")
        pass


def computertrainer(n,position,moves,strategy):
    '''
    This is similar to the function computer, but is used by the
    traincomputer2 function to implement the move chosen
    '''
    s = [str(i) for i in position]
    posvector = int("".join(s))

    bestmoves = []
    mx = max([l[2]for l in strategy[posvector]])
    for j in range(len(strategy[posvector])):
        if strategy[posvector][j][2] > mx - 90:
            bestmoves.append(j)
    m = random.choice(bestmoves)
    pile = strategy[posvector][m][0]
    take = strategy[posvector][m][1]
    position[pile - 1] -= take
    moves[n - 1].append([posvector, m])
    if position == [0,0,0]:
        pass
    pass


def playgame(strategy):
    '''
    This is the function that coordinates the game playing.
    It determines which of players one and two are human,
    and which are computers.
    It continues to run until the user answers no to the
    question "Would you like to play a game? (Y/N) "
    If two computer players are selected, it asks how many games
    the computer players should play.
    '''
    YN = input("Would you like to play a game? (Y/N) ")
    while YN=="Y" or YN=="y":
        P1 = input('Player 1: Computer (C) or Human (H)? (C/H)')
        while P1 not in 'Cc' and P1 not in 'Hh':
            print('invalid input')
            P1 = input('Player 1: Computer (C) or Human (H)? (C/H)')
        P2 = input('Player 2: Computer (C) or Human (H)? (C/H)')
        while P2 not in 'Cc' and P2 not in 'Hh':
            print('invalid input')
            P2 = input('Player 2: Computer (C) or Human (H)? (C/H)')
        if P1 in "Cc" and P2 in "Cc":
            moves = []
            games = input("How many games?")
            counter = 0
            for i in range(int(games)):
                n = 1
                print(f'--Beginning Game {i+1}--')
                position = [7, 5, 3]
                while position != [0, 0, 0]:
                    print(f'The three piles have {position[0]}, {position[1]}, {position[2]}' )
                    computer(n, position, moves, strategy)
                    if n == 1:
                        n = 2
                    else:
                        n = 1
                if n == 1:
                    counter += 1
            print(f'--Completed {games} games--')
            print(f'PLayer 2 won {counter} games')
        if P1 in "Hh" and P2 in "Hh":
            n = 1
            position = [7, 5, 3]
            while position != [0, 0, 0]:
                print(f'The three piles have {position[0]}, {position[1]}, {position[2]}' )
                player(n, position)
                if n == 1:
                    n = 2
                else:
                    n = 1
            YN=input("Would you like to play again? (Y/N) ")
        elif P1 in "Hh" and P2 in "Cc":
            n = 1
            position = [7, 5, 3]
            moves = []
            while position != [0, 0, 0]:
                if n == 1:
                    print(f'The three piles have {position[0]}, {position[1]}, {position[2]}' )
                    player(n, position)
                    n = 2
                else:
                    print(f'The three piles have {position[0]}, {position[1]}, {position[2]}' )
                    computer(n, position, moves, strategy)
                    n = 1
            YN=input("Would you like to play again? (Y/N) ")
        elif P1 in "Cc" and P2 in "Hh":
            n = 1
            position = [7, 5, 3]
            moves = []
            while position != [0, 0, 0]:
                if n == 1:
                    print(f'The three piles have {position[0]}, {position[1]}, {position[2]}' )
                    computer(n, position, moves, strategy)
                    n = 2
                else:
                    print(f'The three piles have {position[0]}, {position[1]}, {position[2]}' )
                    player(n, position)
                    n = 1
            YN=input("Would you like to play again? (Y/N) ")


def traincomputer2(strategy):
    '''
    Sets the amount of trial games for the computer to use to learn to player
    Adjust the use of each move according to its effectiveness at winning
    the game
    '''
    for i in range(15000):
        position = [7, 5, 3]
        playernumber = 2
        moves = [[], []]
        h = []
        while position != [0, 0, 0]:
            if playernumber == 2:
                playernumber = 1
            else:
                playernumber = 2
            computertrainer(playernumber, position, moves, strategy)
        if playernumber == 1:
            winner = 0
            loser = 1
        else:
            winner = 1
            loser = 0
        for i in moves[winner]:
            strategy[i[0]][i[1]][2] += 29
            if strategy[i[0]][i[1]][2] > 100:
                strategy[i[0]][i[1]][2] = 100
            h = [i[0], i[1]]
        strategy[h[0]][h[1]][2] = 1000
        for j in moves[loser]:
            strategy[j[0]][j[1]][2] -= 11
            if strategy[j[0]][j[1]][2] < 0:
                strategy[j[0]][j[1]][2] = 0
            h = [j[0], j[1]]
        strategy[h[0]][h[1]][2] = -1000

    print("")
if __name__ == '__main__':
    strategy=initialize()
    traincomputer2(strategy)
    playgame(strategy)
